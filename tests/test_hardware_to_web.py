# 测试脚本：定义 20 个测试用例的循环执行逻辑。包含硬件读取、网页交互、数据比对以及 AI 报错分析。

import pytest
import os
from dotenv import load_dotenv
from lib.iec61850_client import IEC61850Client
from lib.ai_analyzer import AIAnalyzer
from data.test_cases import TEST_CASES

# 加载 .env 配置文件（里面存放了你的 OpenAI Key 和硬件 IP 地址）
# 这样做是为了数据安全，防止敏感信息直接暴露在代码中
load_dotenv()

class Test硬件数据一致性:
    """
    [测试套件]
    主要目的：验证硬件设备通过 IEC 61850 协议传输的数据是否正确显示在 Web 监控页面上。
    """

    # 这是一个“夹具”，会在每个 test 方法执行前运行
    @pytest.fixture(autouse=True)
    def 初始化客户端(self):
        """
        [初始化]
        在每条测试开始前，实例化 AI 分析器和 61850 硬件客户端。
        """
        self.ai = AIAnalyzer()
        # 从环境变量获取硬件设备的 IP
        硬件IP = os.getenv("HARDWARE_IP")
        self.客户端 = IEC61850Client(硬件IP)

    # 这是一个“参数化”装饰器，它会根据 data/test_cases.py 里的 20 条数据自动跑 20 次测试
    @pytest.mark.parametrize("用例", TEST_CASES)
    def test_数据同步校验(self, 用例, page):
        """
        [核心逻辑]
        1. 调用 61850 接口获取硬件值
        2. 使用 Playwright 访问网页获取 UI 显示值
        3. 对比两者，如果不一致则调用 AI 诊断
        """
        
        # --- 步骤 1: 硬件交互 ---
        # 模拟通过逻辑节点路径读取硬件实时数据
        硬件响应 = self.客户端.fetch_data(用例['point'])
        硬件数值 = 硬件响应['value']

        # --- 步骤 2: 网页交互 (Playwright) ---
        # 导航到监控系统的实时数据页面
        page.goto("https://your-monitor-system.com/live-view")
        
        # 根据用例中的 ID 寻找页面上的对应元素
        网页元素 = page.locator(f"id={用例['point']}")
        
        # [肉眼可见增强]：让当前正在检查的网页元素闪烁红框，方便调试时观察
        网页元素.highlight() 
        
        # 获取网页上显示的文本（例如 "220.5V"）
        网页文本 = 网页元素.inner_text()

        # --- 步骤 3: 结果比对 (断言) ---
        try:
            # 如果用例中有“预期最小值”，说明是模拟量（如电压、电流）
            if "expected_min" in 用例:
                # 去掉单位并转为浮点数进行范围对比
                网页纯数值 = float(网页文本.replace("V", "").replace("A", "").strip())
                assert 用例['expected_min'] <= 网页纯数值 <= 用例['expected_max'], \
                    f"数值超出安全范围! 网页显示: {网页纯数值}, 硬件实际: {硬件数值}"
            else:
                # 否则说明是状态量（如开关 ON/OFF）
                assert str(用例['expected']) == 网页文本.strip(), \
                    f"状态不一致! 网页显示: {网页文本}, 预期应该是: {用例['expected']}"
            
            print(f"✅ 用例 {用例['id']} 校验通过。")

        except Exception as 报错原因:
            # --- 步骤 4: AI 诊断逻辑 ---
            print(f"❌ 用例 {用例['id']} 失败，正在请求 AI 进行根因分析...")
            
            # 整理发送给 AI 的上下文信息，越详细 AI 分析越准
            故障上下文 = {
                "测试点位": 用例['point'],
                "硬件端原始值": 硬件数值,
                "网页端显示值": 网页文本,
                "代码报错详情": str(报错原因)
            }
            
            # 调用 AI 分析器，获取针对该报错的中文解释和解决方案
            AI诊断建议 = self.ai.analyze_error(str(故障上下文))
            
            # 使用 pytest.fail 强制标记测试失败，并把 AI 的专业建议显示在报告里
            pytest.fail(f"一致性校验失败！AI 诊断结果：{AI诊断建议}")