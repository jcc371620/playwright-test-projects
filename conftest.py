# Pytest 全局配置文件及 Fixtures，专门负责在测试失败时，自动捕获网页截图并将其嵌入到 HTML 报告中。

import pytest
from datetime import datetime
import base64

# 这个装饰器表示这是一个 Pytest 的“钩子”函数，用于干涉测试报告的生成过程
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    [报告增强逻辑]
    当某个测试用例执行失败时，自动调用 Playwright 截图，
    并将图片以 Base64 编码的方式直接嵌入到 HTML 报告的“错误日志”部分。
    """
    # 获取 HTML 报告插件对象
    pytest_html = item.config.pluginmanager.getplugin("html")
    结果 = yield
    报告 = 结果.get_result()
    额外信息 = getattr(报告, "extra", [])

    # 只有在用例真正执行(call)阶段且结果为失败(failed)时，才触发截图
    if 报告.when == "call" and 报告.failed:
        # 从测试函数的参数中提取出当前的浏览器页面对象 (page)
        网页对象 = item.funcargs.get("page")
        if 网页对象:
            # 执行截图并返回二进制数据
            截图字节流 = 网页对象.screenshot(type="png", full_page=False)
            # 将图片二进制数据转为 Base64 字符串（这样 HTML 报告不需要附件图片也能显示）
            图片编码 = base64.b64encode(截图字节流).decode("ascii")
            
            # 构造 HTML 代码段，用于在报告中展示这张图片
            # 设置了图片宽度为 500 像素，并加上红色边框，点击图片可直接打开原图
            图片标签 = (
                f'<div><img src="data:image/png;base64,{图片编码}" '
                f'style="width:500px; border:2px solid red;" '
                f'onclick="window.open(this.src)" align="right"/></div>'
            )
            # 将构造好的 HTML 标签加入到报告的额外信息列表里
            额外信息.append(pytest_html.extras.html(图片标签))
            报告.extra = 额外信息