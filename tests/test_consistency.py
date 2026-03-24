# 测试脚本：Data Reconciliation - 数据对账/一致性校验。

import pytest
import requests
from playwright.sync_api import sync_playwright
from utils.ai_engine import analyze_failure

def test_schneider_data_sync():
    # 1. 启动 Playwright (UI 自动化层)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # 调试时设为 False 可见界面
        context = browser.new_context()
        page = context.new_page()

        # 2. 访问 Web 监控页面
        # 可以用一个简单的本地 HTML 模拟
        page.goto("http://localhost:5000/dashboard") 

        # 3. 获取协议层原始数据 (Southbound Data / 南向数据)
        protocol_res = requests.get("http://localhost:5000/mms/dataset/read").json()
        raw_val = protocol_res["Value"]

        # 4. 获取 Web 界面显示的数据 (Northbound Data / 北向数据)
        # 假设页面上电压显示的 ID 是 'current-display'
        web_val_text = page.inner_text("#current-display")
        web_val = float(web_text.replace("A", ""))

        # 5. 断言与 AI 分析 (Assertion & AI Analysis)
        try:
            # 允许 0.01 的精度误差 (Tolerance)
            assert abs(raw_val - web_val) < 0.01
            print(f"✅ Success: Data match! Value: {raw_val}")
        except AssertionError as e:
            print("❌ Failure: Data Mismatch detected. Consulting AI...")
            # 如果失败，调用 AI 引擎分析根本原因
            report = analyze_failure(raw_val, web_val)
            print(f"\n--- AI RCA Report ---\n{report}")
            raise e
        
        browser.close()