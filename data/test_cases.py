# data/test_cases.py

""" 在自动化测试中，将数据与逻辑分离（Data-Driven Testing）是标准做法。每个字段的含义如下：
id: 唯一标识符，方便在测试报告中定位。
type: 测点类型（如电压、电流、开关状态）。
point: IEC 61850 标准中的逻辑节点 (Logical Node)。在实际硬件中，这是你通过 MMS 协议访问的具体地址。
expected_min / max: 模拟量的正常波动范围。如果硬件传回的值超出此范围，Web 端应显示告警。
expected: 状态量（开关/报警）的预期值。如果实际值与预期不符，说明数据未正确传输或显示。
"""

"""
这里定义 20 个测试用例，涵盖了 IEC 61850 常见的监控点。
我们将它们分为：模拟量(Analog)、状态量(Status) 和 异常类(Anomaly)。
"""

# data/test_cases.py

"""
此文件定义 20 个测试用例。
每个用例代表一个电力系统 IED (Intelligent Electronic Device) 的监测点。
"""

TEST_CASES = [
    # 1-10: 模拟量监控 (Analog Values) - 验证数值精度和实时同步
    {"id": 1, "type": "Voltage", "point": "TEM_LLN0_V_PhaseA", "expected_min": 210, "expected_max": 235},
    {"id": 2, "type": "Voltage", "point": "TEM_LLN0_V_PhaseB", "expected_min": 210, "expected_max": 235},
    {"id": 3, "type": "Voltage", "point": "TEM_LLN0_V_PhaseC", "expected_min": 210, "expected_max": 235},
    {"id": 4, "type": "Current", "point": "TEM_LLN0_I_PhaseA", "expected_min": 0, "expected_max": 50},
    {"id": 5, "type": "Current", "point": "TEM_LLN0_I_PhaseB", "expected_min": 0, "expected_max": 50},
    {"id": 6, "type": "Current", "point": "TEM_LLN0_I_PhaseC", "expected_min": 0, "expected_max": 50},
    {"id": 7, "type": "Freq", "point": "TEM_LLN0_Hz", "expected_min": 49.8, "expected_max": 50.2},
    {"id": 8, "type": "Power", "point": "TEM_LLN0_P", "expected_min": 0, "expected_max": 10000},
    {"id": 9, "type": "Temp", "point": "TEM_TTMP_1", "expected_min": 25, "expected_max": 75},
    {"id": 10, "type": "Humid", "point": "TEM_HUM_1", "expected_min": 10, "expected_max": 60},

    # 11-15: 状态量监控 (Status Values) - 验证 Web 端的图标/状态切换
    {"id": 11, "type": "Switch", "point": "POS_CSWI_1", "expected": "ON"},
    {"id": 12, "type": "Switch", "point": "POS_CSWI_2", "expected": "OFF"},
    {"id": 13, "type": "Alarm", "point": "ALM_GGIO_1", "expected": "NORMAL"},
    {"id": 14, "type": "Lock", "point": "LCK_GGIO_1", "expected": "UNLOCKED"},
    {"id": 15, "type": "Mode", "point": "MOD_LLN0", "expected": "REMOTE"},

    # 16-20: 异常与安全性测试 (Anomaly & Security) - 触发 AI 分析的关键点
    {"id": 16, "type": "Error", "point": "ERR_SIG_1", "expected": "NONE"},
    {"id": 17, "type": "Comm", "point": "LATENCY_MS", "expected_max": 100},
    {"id": 18, "type": "Auth", "point": "FAILED_ATTEMPTS", "expected": "0"},
    {"id": 19, "type": "Relay", "point": "RLY_STAT", "expected": "READY"},
    {"id": 20, "type": "Health", "point": "BAT_SOC", "expected_min": 90, "expected_max": 100}
]