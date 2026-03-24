# 项目运行入口
# 负责启动 Playwright 自动化测试并生成精美报告

import pytest
import os
import sys
from datetime import datetime

def 准备测试环境():
    """
    [环境初始化]
    确保项目根目录下存在存放报告和结果的文件夹。
    如果文件夹不存在则自动创建，防止程序运行中报错。
    """
    必要的文件夹 = ['reports', 'test-results']
    for 文件夹 in 必要的文件夹:
        if not os.path.exists(文件夹):
            os.makedirs(文件夹)
            print(f"[系统信息] 已创建文件夹: {文件夹}")

def 执行自动化测试():
    """
    [运行主逻辑]
    配置 Pytest 插件参数并启动测试套件。
    """
    准备测试环境()

    # 使用当前时间生成唯一的文件名 (例如: 20260324_083015)
    # 这样每次运行的报告都会被保留，不会被覆盖
    当前时间 = datetime.now().strftime("%Y%m%d_%H%M%S")
    报告路径 = f"reports/硬件监控测试报告_{当前时间}.html"

    print(f"🚀 自动化测试开始执行，当前时间: {当前时间}...")

    # Pytest 运行参数详细说明:
    # 1. "tests/test_hardware_to_web.py": 指定执行哪一个测试脚本文件
    # 2. "-v": 详细模式，在终端显示每一个测试用例的运行结果（成功或失败）
    # 3. "--headed": 开启“有头模式”，运行时你会看到浏览器自动弹出并操作
    # 4. "--browser=chromium": 使用谷歌内核浏览器执行测试
    # 5. "--slowmo=800": 每个动作（如点击、输入）停顿 800 毫秒，确保肉眼能跟上节奏
    # 6. "--html": 指定生成的 HTML 报告存放位置
    # 7. "--self-contained-html": 把所有的样式表(CSS)都打包进 HTML 文件，方便直接发给领导看
    运行参数 = [
        "tests/test_hardware_to_web.py",
        "-v",
        "--headed",
        "--browser=chromium",
        "--slowmo=800",
        f"--html={报告路径}",
        "--self-contained-html"
    ]

    # 调用 pytest 的主函数开始跑用例，并获取返回码 (0 代表全部成功，1 代表有失败)
    返回码 = pytest.main(运行参数)
    
    print(f"\n📊 测试任务结束，返回码: {返回码}")
    print(f"📂 测试报告已生成，请查看: {os.path.abspath(报告路径)}")

if __name__ == "__main__":
    执行自动化测试()