# IEC 61850 客户端模块
# 由于真实的 61850 协议非常复杂，我们使用 Scapy 来模拟一个“伪造”的 61850 MMS 报文。这样你在没有真实硬件的情况下，也能模拟出数据抓取的过程。
"""
技术重点解释
Scapy 的作用：在代码的 _模拟发送61850报文 中，我们使用了 IP() / TCP() / Raw()。这在网络安全测试和工业协议仿真中非常常见。它允许你跳过标准的 Socket 库，直接控制每一个数据包的层级。

异常触发逻辑：我在代码里加了一个 random.random() < 0.05。这意味着平均每跑 20 个用例（正好是你的一组用例数量），就可能会出现一次随机失败。

这非常重要！ 只有这样，你运行 run.py 时，才能看到 Playwright 截取失败图片，并看到 AI 介入分析报错原因的整个闭环流程。

数据安全性：所有的操作都基于 self.硬件ip。在真实环境中，如果你的测试机器没有连接到真实的 61850 控制网，send() 函数会自动被操作系统的防火墙或路由协议拦截，保证了测试的物理边界安全。
"""

import random
import time
from scapy.all import IP, TCP, Raw, send, sniff

class IEC61850Client:
    """
    [协议客户端]
    使用 Scapy 模拟 IEC 61850 MMS 协议的数据交互。
    该类负责向硬件发送请求并解析返回的报文。
    """

    def __init__(self, 硬件ip):
        """
        [初始化]
        :param 硬件ip: 目标 IED (智能电子设备) 的 IP 地址
        """
        self.硬件ip = 硬件ip
        # 默认的 MMS 端口通常是 102 (ISO-TSAP)
        self.端口 = 102 

    def _模拟发送61850报文(self, 点位路径):
        """
        [底层方法]
        使用 Scapy 构造一个模拟的 MMS 读取请求报文。
        在真实的电力系统中，这里会包含复杂的 ASN.1 编码。
        """
        # 构造一个简单的 TCP 负载，模拟 MMS 的 Read-Request
        # 包含点位信息，例如 "TEM_LLN0_V_PhaseA"
        模拟载荷 = f"MMS_READ_REQ: {点位路径}".encode('utf-8')
        
        # 构造 IP 层和 TCP 层报文
        报文 = IP(dst=self.硬件ip) / TCP(dport=self.端口) / Raw(load=模拟载荷)
        
        # 发送报文 (verbose=0 表示不打印发送细节)
        # 在实际测试环境中，这一步会将数据包发送到网络中
        # send(报文, verbose=0) 
        
        print(f"[协议层] 已发送 61850 读取请求 -> {点位路径}")

    def fetch_data(self, 点位名称):
        """
        [核心接口]
        模拟从硬件读取实时数据的过程。
        :param 点位名称: 对应 test_cases.py 里的 point 字段
        :return: 包含状态和数值的字典
        """
        # 1. 模拟网络请求过程
        self._模拟发送61850报文(点位名称)
        
        # 2. 模拟网络延迟 (电力系统中通常要求在几毫秒到几十毫秒)
        time.sleep(0.05) 

        # 3. 模拟数据解析逻辑
        # 针对不同类型的点位，生成合理的模拟随机数
        try:
            # 随机模拟：有 5% 的概率发生硬件接口超时或数据非法，用于触发 AI 分析
            if random.random() < 0.05:
                return {
                    "status": "error",
                    "message": "MMS 通讯响应超时 (Timeout)",
                    "value": None
                }

            # 根据点位关键字生成不同的模拟值
            if "Volt" in 点位名称 or "V_Phase" in 点位名称:
                # 模拟 220V 左右的电压波动
                结果值 = round(random.uniform(215.0, 235.0), 2)
            elif "Curr" in 点位名称 or "I_Phase" in 点位名称:
                # 模拟电流值
                结果值 = round(random.uniform(5.0, 45.0), 2)
            elif "POS" in 点位名称 or "CSWI" in 点位名称:
                # 模拟开关状态 (0 为 OFF, 1 为 ON)
                结果值 = "ON" if random.random() > 0.5 else "OFF"
            elif "ALM" in 点位名称:
                # 模拟报警状态
                结果值 = "NORMAL"
            else:
                # 默认数值
                结果值 = round(random.uniform(0, 100), 2)

            return {
                "status": "success",
                "value": 结果值,
                "timestamp": time.time()
            }

        except Exception as e:
            return {
                "status": "error",
                "message": f"解析 61850 报文失败: {str(e)}",
                "value": None
            }

# --- 调试代码 ---
if __name__ == "__main__":
    # 可以在这里单独运行这个文件进行测试
    测试客户端 = IEC61850Client("192.168.1.100")
    结果 = 测试客户端.fetch_data("TEM_LLN0_V_PhaseA")
    print(f"模拟抓取结果: {结果}")