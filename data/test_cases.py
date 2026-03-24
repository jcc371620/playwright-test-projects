# data/test_cases.py
# 描述：定义电力监控系统 20 个核心测点的 I/O 预期模型

"""
这里定义 20 个测试用例，涵盖了 IEC 61850 常见的监控点。
我们将它们分为：模拟量(Analog)、状态量(Status) 和 异常类(Anomaly)。
"""

# data/test_cases.py
# -------------------------------------------------------------------------
# [MNC 专业级测试用例库] - 电力监控系统端到端一致性校验
# 在自动化测试中，将数据与逻辑分离（Data-Driven Testing）是标准做法。每个字段的含义如下：
# 字段解释 (Field Definitions):
# 1. id:              用例唯一编号 (Unique ID)，用于 Traceability Matrix (需求跟踪矩阵)。唯一标识符，方便在测试报告中定位。
# 2. point:           硬件测点名称 (Tag Name)，对应 61850 变电站配置中的 IED 逻辑节点。
# 3. type:            数据类型 (Data Category)，用于报表分类汇总（模拟量、状态量、告警等）。
# 4. scenario:        测试场景描述 (Test Scenario)，描述该测试对业务或安全的影响，满足审计合规性。
# 5. expected_input:  期望输入 (Expected Input)，协议层预期发送的原始指令内容（如 MMS/TCP 报文）。
# 6. expected_output: 期望结果 (Expected Output)，UI 界面层预期的显示状态或数值描述。
# 7. expected_min/max:数值判定区间，定义了硬件采样值映射到网页后的合法波动范围。
# 8. expected:        状态判定标准，针对开关量 (ON/OFF) 的字符串精确匹配标准。
# -------------------------------------------------------------------------

# data/test_cases.py
# 描述：电力监控系统 20 核心测点验证方案 (含 I/O 预期定义)

TEST_CASES = [
    # --- 组 1：模拟量遥测 (Analog Measurement) ---
    {
        "id": "TC-001", "point": "MET_L1_Volt", "type": "Voltage", 
        "scenario": "验证 A 相母线电压实时同步，确保输电稳定性",
        "expected_input": "MMS_READ_VAL:MET_L1_Volt", 
        "expected_output": "显示值应在 220V 左右 (误差 <5%)",
        "expected_min": 209.0, "expected_max": 231.0
    },
    {
        "id": "TC-002", "point": "MET_L2_Volt", "type": "Voltage", 
        "scenario": "验证 B 相母线电压平衡度，防止设备因三相不平衡受损",
        "expected_input": "MMS_READ_VAL:MET_L2_Volt", 
        "expected_output": "显示值应在 220V 左右 (误差 <5%)",
        "expected_min": 209.0, "expected_max": 231.0
    },
    {
        "id": "TC-003", "point": "MET_L3_Volt", "type": "Voltage", 
        "scenario": "验证 C 相母线电压对称性，符合变电站运行规程",
        "expected_input": "MMS_READ_VAL:MET_L3_Volt", 
        "expected_output": "显示值应在 220V 左右 (误差 <5%)",
        "expected_min": 209.0, "expected_max": 231.0
    },
    {
        "id": "TC-004", "point": "MET_L1_Curr", "type": "Current", 
        "scenario": "监控 A 相馈线电流负荷，校验 Web 端实时曲线同步性",
        "expected_input": "MMS_READ_VAL:MET_L1_Curr", 
        "expected_output": "显示值应匹配硬件采样 (0~100A)",
        "expected_min": 0.0, "expected_max": 100.0
    },
    {
        "id": "TC-005", "point": "MET_FREQ", "type": "Frequency", 
        "scenario": "监测系统频率 (50Hz)，验证频率波动的还原精度",
        "expected_input": "MMS_READ_VAL:MET_FREQ", 
        "expected_output": "显示值应稳定在 50.0Hz 附近",
        "expected_min": 49.5, "expected_max": 50.5
    },
    {
        "id": "TC-006", "point": "MET_PF", "type": "PowerFactor", 
        "scenario": "校验功率因数，确保无功补偿系统数据正确",
        "expected_input": "MMS_READ_VAL:MET_PF", 
        "expected_output": "数值应在 0.85 ~ 1.0 之间",
        "expected_min": 0.85, "expected_max": 1.0
    },

    # --- 组 2：开关状态遥信 (Binary Status) ---
    {
        "id": "TC-007", "point": "POS_CB_01", "type": "Switch", 
        "scenario": "验证 1 号断路器分合闸状态，确保 UI 映射物理位置准确",
        "expected_input": "MMS_GET_STATUS:POS_CB_01", 
        "expected_output": "Web 状态应显示: ON",
        "expected": "ON"
    },
    {
        "id": "TC-008", "point": "POS_CB_02", "type": "Switch", 
        "scenario": "验证 2 号备用断路器状态，防止备自投系统误判定",
        "expected_input": "MMS_GET_STATUS:POS_CB_02", 
        "expected_output": "Web 状态应显示: OFF",
        "expected": "OFF"
    },
    {
        "id": "TC-009", "point": "POS_DISC_01", "type": "Switch", 
        "scenario": "确认隔离刀闸物理位置，确保远程调度安全",
        "expected_input": "MMS_GET_STATUS:POS_DISC_01", 
        "expected_output": "Web 状态应显示: OFF",
        "expected": "OFF"
    },
    {
        "id": "TC-010", "point": "POS_EARTH_01", "type": "Switch", 
        "scenario": "验证接地刀闸状态，关键安全点位校验",
        "expected_input": "MMS_GET_STATUS:POS_EARTH_01", 
        "expected_output": "Web 状态应显示: OFF",
        "expected": "OFF"
    },

    # --- 组 3：告警越限 (Alarm/Event) ---
    {
        "id": "TC-011", "point": "ALM_OV", "type": "Alarm", 
        "scenario": "模拟过电压告警，验证 Web 端红色高亮提示功能",
        "expected_input": "MMS_GET_ALM:ALM_OV", 
        "expected_output": "状态应为: NORMAL (未越限)",
        "expected": "NORMAL"
    },
    {
        "id": "TC-012", "point": "ALM_UV", "type": "Alarm", 
        "scenario": "模拟欠电压报警，验证告警事件推送及时性",
        "expected_input": "MMS_GET_ALM:ALM_UV", 
        "expected_output": "状态应为: NORMAL",
        "expected": "NORMAL"
    },
    {
        "id": "TC-013", "point": "ALM_OC", "type": "Alarm", 
        "scenario": "验证过流三段保护告警在 UI 的实时显示",
        "expected_input": "MMS_GET_ALM:ALM_OC", 
        "expected_output": "状态应为: NORMAL",
        "expected": "NORMAL"
    },
    {
        "id": "TC-014", "point": "ALM_TEMP", "type": "Alarm", 
        "scenario": "监测变压器温控告警映射逻辑",
        "expected_input": "MMS_GET_ALM:ALM_TEMP", 
        "expected_output": "状态应为: NORMAL",
        "expected": "NORMAL"
    },
    {
        "id": "TC-015", "point": "ALM_COM", "type": "Alarm", 
        "scenario": "通讯心跳监测，验证 61850 链路存活状态",
        "expected_input": "MMS_GET_ALM:ALM_COM", 
        "expected_output": "状态应为: NORMAL",
        "expected": "NORMAL"
    },

    # --- 组 4：能耗与电能质量 (Energy Quality) ---
    {
        "id": "TC-016", "point": "ENG_ACTIVE", "type": "Energy", 
        "scenario": "校验累计有功电量，用于月底计费结算依据",
        "expected_input": "MMS_GET_ENG:ACTIVE", 
        "expected_output": "数值应 > 0 且持续增长",
        "expected_min": 0.0, "expected_max": 999999.0
    },
    {
        "id": "TC-017", "point": "ENG_REACTIVE", "type": "Energy", 
        "scenario": "校验累计无功电量，分析功率因数奖惩指标",
        "expected_input": "MMS_GET_ENG:REACTIVE", 
        "expected_output": "数值应在合理电费计费范围内",
        "expected_min": 0.0, "expected_max": 500000.0
    },
    {
        "id": "TC-018", "point": "THD_VOLT", "type": "Quality", 
        "scenario": "验证电压总谐波畸变率 (THD)，确保电能质量符合标准",
        "expected_input": "MMS_GET_PQ:THD_V", 
        "expected_output": "数值应 < 5.0%",
        "expected_min": 0.0, "expected_max": 5.0
    },
    {
        "id": "TC-019", "point": "UNB_VOLT", "type": "Quality", 
        "scenario": "验证电压不平衡度，防止电机发热损耗",
        "expected_input": "MMS_GET_PQ:UNB_V", 
        "expected_output": "数值应 < 2.0%",
        "expected_min": 0.0, "expected_max": 2.0
    },
    {
        "id": "TC-020", "point": "MET_TEMP", "type": "Temp", 
        "scenario": "验证环境温湿度同步，监控机房运行环境",
        "expected_input": "MMS_GET_ENV:TEMP", 
        "expected_output": "显示应在 10℃~45℃ 之间",
        "expected_min": 10.0, "expected_max": 45.0
    }
]