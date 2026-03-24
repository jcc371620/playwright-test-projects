# data/test_cases.py

"""
这里定义 20 个测试用例，涵盖了 IEC 61850 常见的监控点。
我们将它们分为：模拟量(Analog)、状态量(Status) 和 异常类(Anomaly)。
"""

TEST_CASES = [
    # --- 模拟量监控 (Analog Values) ---
    {"id": 1, "type": "Voltage", "point": "Phase_A_Volt", "expected_min": 210, "expected_max": 230},
    {"id": 2, "type": "Voltage", "point": "Phase_B_Volt", "expected_min": 210, "expected_max": 230},
    {"id": 3, "type": "Voltage", "point": "Phase_C_Volt", "expected_min": 210, "expected_max": 230},
    {"id": 4, "type": "Current", "point": "Phase_A_Curr", "expected_min": 0, "expected_max": 100},
    {"id": 5, "type": "Current", "point": "Phase_B_Curr", "expected_min": 0, "expected_max": 100},
    {"id": 6, "type": "Current", "point": "Phase_C_Curr", "expected_min": 0, "expected_max": 100},
    {"id": 7, "type": "Frequency", "point": "Grid_Freq", "expected_min": 49.5, "expected_max": 50.5},
    {"id": 8, "type": "Power", "point": "Active_Power", "expected_min": 0, "expected_max": 5000},
    {"id": 9, "type": "Power", "point": "Reactive_Power", "expected_min": 0, "expected_max": 1000},
    {"id": 10, "type": "Temperature", "point": "Transformer_Temp", "expected_min": 20, "expected_max": 85},

    # --- 状态量监控 (Status/Digital Values) ---
    {"id": 11, "type": "Switch", "point": "Main_Breaker_Status", "expected": "ON"},
    {"id": 12, "type": "Switch", "point": "Isolator_Status", "expected": "OFF"},
    {"id": 13, "type": "Alarm", "point": "Door_Open_Sensor", "expected": "CLOSED"},
    {"id": 14, "type": "Alarm", "point": "Fire_Alarm_Sensor", "expected": "NORMAL"},
    {"id": 15, "type": "Comm", "point": "Heartbeat_Signal", "expected": "ACTIVE"},

    # --- 异常与边界测试 (Anomaly & Boundary) ---
    {"id": 16, "type": "Overload", "point": "Emergency_Stop", "expected": "INACTIVE"},
    {"id": 17, "type": "Integrity", "point": "Packet_Loss_Rate", "expected_max": 0.01},
    {"id": 18, "type": "Sync", "point": "Time_Sync_Offset", "expected_max": 500}, # 毫秒
    {"id": 19, "type": "Security", "point": "Unauthorized_Access_Log", "expected": "0"},
    {"id": 20, "type": "Maintenance", "point": "Battery_Health", "expected_min": 80}
]