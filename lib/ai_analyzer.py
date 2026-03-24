# AI 分析器模块
# 这个模块的作用是当测试发生断言失败（比如网页数值和硬件数值对不上）或系统报错时，自动抓取当前的上下文信息（Context），通过 OpenAI 的 API 进行深度分析，并返回一个人类可读的诊断报告。

import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
# 这样可以确保你的 API Key 不会直接写在代码里，提高项目的安全性
load_dotenv()

class AIAnalyzer:
    """
    [AI 故障分析器]
    专门负责对接大语言模型（OpenAI），对测试过程中出现的报错进行智能化分析。
    """

    def __init__(self):
        """
        [初始化]
        从环境变量中获取 API Key 并初始化 OpenAI 客户端。
        """
        # 从 .env 文件中读取名为 'OPENAI_API_KEY' 的变量
        self.api_key = os.getenv("OPENAI_API_KEY")
        
        # 基础安全性检查：如果没有配置 Key，程序应提前预警而不是崩掉
        if not self.api_key:
            print("[警告] 未在 .env 文件中检测到 OPENAI_API_KEY，AI 分析功能将无法正常使用。")
        
        # 初始化 OpenAI 客户端对象
        # 注意：这里使用的是 OpenAI Python SDK v1.0+ 的标准写法
        self.client = OpenAI(api_key=self.api_key)

    def analyze_error(self, 故障上下文数据):
        """
        [核心分析接口]
        将测试失败的详细信息发送给 AI，并获取专业的诊断方案。
        
        :param 故障上下文数据: 包含报错信息、硬件数值、网页数值的字符串或字典
        :return: AI 给出的中文分析建议
        """
        # 如果没有 Key，直接返回原始报错，不执行 AI 调用
        if not self.api_key:
            return "AI 分析不可用：请先配置 API Key。"

        # 构造发送给 AI 的“提示词 (Prompt)”
        # 这里的角色设定非常重要，我们要求 AI 扮演一名“资深电力自动化测试专家”
        系统指令 = (
            "你是一名资深的电力系统自动化测试专家，擅长 IEC 61850 协议和 Web 前端监控系统。"
            "我会给你一段自动化测试失败的日志，请你分析是‘硬件传输问题’、‘网络延迟’、‘前端显示 Bug’还是‘逻辑计算错误’。"
            "请直接给出简练的中文诊断结论和具体的修复建议。"
        )

        用户请求 = f"请分析以下测试故障：\n{故障上下文数据}"

        try:
            # 调用 OpenAI Chat Completion 接口
            # 使用 gpt-3.5-turbo 足够处理这类文本分析，且速度快、成本低
            响应 = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": 系统指令},
                    {"role": "user", "content": 用户请求}
                ],
                temperature=0.3, # 较低的温度值表示输出更严谨、不乱发挥
                max_tokens=500   # 限制返回长度，防止 AI 太啰嗦
            )

            # 提取 AI 返回的文本内容
            诊断结果 = 响应.choices[0].message.content
            
            # 在返回结果前加上小图标，方便在 HTML 报告中一眼识别
            return f"🤖 AI 诊断报告：\n{诊断结果}"

        except Exception as e:
            # 异常处理：如果网络不通或 API 额度不足，捕获报错
            return f"AI 分析请求失败，原因：{str(e)}"

# --- 独立调试逻辑 ---
if __name__ == "__main__":
    # 如果你单独运行这个文件，可以快速测试 AI 是否配置正确
    分析器 = AIAnalyzer()
    
    # 模拟一个典型的电力系统同步错误上下文
    模拟故障 = (
        "用例ID: 1, 测点: 相电压A, "
        "硬件端读取值: 220.5, "
        "网页端显示值: 0.0, "
        "报错信息: AssertionError: 0.0 不在 210-230 范围内"
    )
    
    print("正在测试 AI 分析功能...")
    结果 = 分析器.analyze_error(模拟故障)
    print("-" * 30)
    print(结果)
    print("-" * 30)
