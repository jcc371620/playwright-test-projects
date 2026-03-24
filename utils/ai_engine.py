# RCA (Root Cause Analysis) - 根本原因分析。当 UI 和协议数据对不上时，调用 OpenAI/Claude 接口进行错误诊断

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def analyze_failure(protocol_val, web_val):
    """
    使用 AI 进行错误诊断 (Diagnostic Analysis)
    """
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = f"""
    Context: Industrial Automation Testing for Schneider Electric.
    Issue: Data Mismatch (数据不一致).
    - Protocol Value (61850协议值): {protocol_val}A
    - Web UI Value (前端显示值): {web_val}A
    
    Task: Provide 3 possible reasons (Network latency, Scaling error, or Frontend cache) 
    and a fix suggestion in Chinese.
    """
    
    response = client.chat.completions.create(
        model="gpt-4o", # 或使用 gpt-3.5-turbo
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content