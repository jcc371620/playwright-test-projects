# test_hardware_to_web.py
# 测试脚本
# 定义 20 个测试用例的循环执行逻辑。包含硬件读取、网页交互、数据比对以及 AI 报错分析。

# tests/test_hardware_to_web.py
import pytest
import allure
import os
from lib.ai_analyzer import AIAnalyzer
from data.test_cases import TEST_CASES

class TestPowerSystemSync:
    def setup_class(self):
        # 初始化 AI 分析器
        self.ai = AIAnalyzer()

    @pytest.mark.parametrize("case", TEST_CASES)
    def test_sync_process(self, case, page):
        # 记录实际发送的模拟指令
        case['actual_input'] = f"MMS_SENT -> {case['expected_input']}"
        
        try:
            # 尝试访问页面（即使地址是假的，AI 也会分析报错原因）
            page.goto("/Users/jc/git/playwright-test-projects/playwright-test-projects/mock_site/index.html", timeout=5000)
            
            # 抓取数据
            element = page.locator(f"#{case['point']}")
            case['actual_output'] = element.inner_text().strip()
            
            # 校验逻辑
            if "expected_min" in case:
                val = float(case['actual_output'].replace("V", "").strip())
                assert case['expected_min'] <= val <= case['expected_max']
            else:
                assert case['expected'] == case['actual_output']
            
            case['status'] = "PASSED"
            case['ai_suggestion'] = "校验通过"

        except Exception as e:
            case['status'] = "FAILED"
            case['actual_output'] = "ERR_CONNECTION"
            
            # --- 关键：触发 AI 诊断并将分析结果存入 case 字典 ---
            error_ctx = f"用例:{case['id']}, 测点:{case['point']}, 预期:{case['expected_output']}, 错误详情:{str(e)}"
            case['ai_suggestion'] = self.ai.analyze_error(error_ctx)
            
            # 在 Allure 报告中也记录一份
            allure.attach(case['ai_suggestion'], name="Gemini AI 诊断建议")
            pytest.fail(f"测试失败 | AI 建议: {case['ai_suggestion']}")