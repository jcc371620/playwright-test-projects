# AI 分析器模块，这个模块的作用是当测试发生断言失败（比如网页数值和硬件数值对不上）或系统报错时，自动抓取当前的上下文信息（Context），通过 OpenAI 的 API 进行深度分析，并返回一个人类可读的诊断报告。

# lib/ai_analyzer.py
import os
import openai
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class AIAnalyzer:
    """
    [MNC 级别故障诊断引擎 - Gemini 1.5 Flash 驱动版]
    专门为电力监控自动化测试设计的异常分析器。
    """
    
    def __init__(self):
        # 从环境变量获取配置
        api_key = os.getenv("GEMINI_API_KEY")
        base_url = os.getenv("GEMINI_BASE_URL")
        
        if not api_key:
            print("⚠️ 警告: 未发现 GEMINI_API_KEY，AI 诊断功能将跳过。")
            self.client = None
        else:
            # 使用 OpenAI SDK 兼容模式连接 Gemini
            self.client = openai.OpenAI(
                api_key=api_key,
                base_url=base_url
            )

    def analyze_error(self, error_context):
        """
        接收测试上下文（预期 vs 实际），返回人类可读的修复建议。
        """
        if not self.client:
            return "AI 诊断未配置 (Missing API Key)"

        # 构建专业提示词 (Prompt Engineering)
        prompt = f"""
        你是一名资深的电力自动化测试专家。在进行 Playwright + IEC61850 协议测试时发现不一致。
        
        【测试上下文】:
        {error_context}
        
        【任务】:
        请简短地（50字以内）分析可能的原因，并给出针对性的修复建议。
        如果是数值越限，请分析是硬件采样误差还是前端显示逻辑错误。
        如果是状态不符，请分析是否为通讯延迟。
        """

        try:
            # Gemini 1.5 Flash 在 OpenAI 模式下通常映射为 "gpt-3.5-turbo" 
            # 或者直接写 "gemini-1.5-flash" (取决于 Google 侧的最新兼容性)
            response = self.client.chat.completions.create(
                model="gemini-1.5-flash", 
                messages=[
                    {"role": "system", "content": "你是一名严谨的自动化测试故障分析助手。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3 # 降低随机性，确保结论严谨
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            return f"AI 诊断暂时不可用: {str(e)}"

# 简单的单元测试逻辑
if __name__ == "__main__":
    analyzer = AIAnalyzer()
    test_context = "点位:MET_L1_Volt, 预期输入:MMS_READ, 期望输出:220V, 实际输入:TCP_PUSH, 实际输出:180V"
    print(f"🔍 模拟诊断结果:\n{analyzer.analyze_error(test_context)}")