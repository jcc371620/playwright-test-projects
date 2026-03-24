# 测试脚本
# 定义 20 个测试用例的循环执行逻辑。包含硬件读取、网页交互、数据比对以及 AI 报错分析。

import pytest
import allure
import os
from lib.iec61850_client import IEC61850Client
from lib.ai_analyzer import AIAnalyzer
from data.test_cases import TEST_CASES

class TestPowerSystemSync:
    """
    [电力系统端到端测试类]
    负责模拟 61850 报文发送、Playwright UI 抓取及数据比对。
    """

    def setup_class(self):
        # 初始化协议客户端和 AI 分析器
        self.hw_client = IEC61850Client(os.getenv("HARDWARE_IP", "192.168.1.100"))
        self.ai = AIAnalyzer()

    @allure.feature("硬件与Web端数据一致性校验")
    @pytest.mark.parametrize("case", TEST_CASES)
    def test_sync_process(self, case, page):
        """
        [主测试方法]
        1. 模拟协议指令发送 -> 2. 获取硬件值 -> 3. 抓取Web UI值 -> 4. I/O 溯源记录
        """
        
        # --- 步骤 1: 硬件层操作 (模拟发送与接收) ---
        with allure.step(f"协议指令下发: {case['expected_input']}"):
            # 记录【实际输入】内容
            case['actual_input'] = f"MMS_READ_REQ_SENT -> {case['point']}"
            
            # 获取硬件模拟返回值
            hw_response = self.hw_client.fetch_data(case['point'])
            hw_value = hw_response['value']
            allure.attach(str(hw_value), name="硬件原始数据")

        # --- 步骤 2: Web 层操作 (Playwright) ---
        with allure.step(f"Web UI 实时数据抓取: {case['point']}"):
            # 模拟页面跳转与定位
            page.goto("https://your-power-system.com/dashboard")
            
            # 定位点位元素（假设 ID 与点位名称一致）
            element = page.locator(f"#{case['point']}")
            element.highlight() # 高亮显示操作，方便录制
            
            # 获取【实际输出】内容
            raw_ui_text = element.inner_text()
            case['actual_output'] = raw_ui_text.strip()
            allure.attach(case['actual_output'], name="Web界面实时数值")

        # --- 步骤 3: 严谨性校验与异常处理 ---
        try:
            with allure.step("逻辑一致性判定"):
                if "expected_min" in case:
                    # 模拟量校验：转换为 float 进行范围比对
                    actual_num = float(case['actual_output'].replace("V", "").replace("A", "").strip())
                    assert case['expected_min'] <= actual_num <= case['expected_max'], \
                        f"数值越限！实际: {actual_num}"
                else:
                    # 状态量校验：字符串比对
                    assert case['expected'] == case['actual_output'], \
                        f"状态不匹配！实际: {case['actual_output']}"
                
                # 记录状态为 PASS
                case['status'] = "PASSED"

        except Exception as e:
            # 记录状态为 FAIL
            case['status'] = "FAILED"
            
            # 触发 AI 诊断分析
            with allure.step("❌ 故障 AI 深度诊断"):
                error_context = f"点位:{case['point']}, 预期:{case['expected_output']}, 实际:{case['actual_output']}, 错误:{str(e)}"
                case['ai_suggestion'] = self.ai.analyze_error(error_context)
                
                # 截图存证
                screenshot_path = f"reports/error_{case['id']}.png"
                page.screenshot(path=screenshot_path)
                allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG)
                
                # 抛出异常以记录 Pytest 结果
                pytest.fail(f"校验失败: {str(e)} | AI建议: {case['ai_suggestion']}")