# playwright-test-projects

本项目用于学习Pytest + Playwright 自动化测试, 目的是能看到模拟硬件测试设备通过61850接口传输到web的数据，如果报错的话则用ai分析报错原因并返回ai告知到结果，同时保证数据的安全性，并且可以维护测试用例。

---

## Project Structure

<!-- TREE_START -->
<details>
<summary>📂 Project Structure</summary>

```text
├── .gitignore        # Python项目通用忽视规则 (1.0 KB, 2026-03-25)
├── README.md         # playwright-test-projects (11.0 KB, 2026-03-25)
├── allure-results/   (dir, 2026-03-25)
│   ├── 00f70011-7af3-42c4-ad7b-e64595fea835-result.json     (5.5 KB, 2026-03-25)
│   ├── 0e3a124c-f4c5-4263-ba40-0a7553404707-result.json     (5.5 KB, 2026-03-25)
│   ├── 151ab4af-1b19-4ef9-b2aa-753ac05badae-result.json     (5.5 KB, 2026-03-25)
│   ├── 26015d3c-8aa8-46f5-b2de-a15f189ddfc8-container.json  (1.0 KB, 2026-03-25)
│   ├── 26b45482-14d5-4ed1-b779-757138b59225-container.json  (1.0 KB, 2026-03-25)
│   ├── 2b3ffb28-126f-451e-8ced-7a306b63a719-result.json     (5.5 KB, 2026-03-25)
│   ├── 30ece776-8eaf-4b2b-b7fa-177cf16eb23b-container.json  (1.0 KB, 2026-03-25)
│   ├── 31c427ab-5036-4fe5-9cf3-aa32a279735b-result.json     (5.5 KB, 2026-03-25)
│   ├── 382d60f5-1d9e-42c5-826b-31153f89f7dd-result.json     (5.5 KB, 2026-03-25)
│   ├── 3c485231-c191-4363-b9ce-159292917155-result.json     (5.5 KB, 2026-03-25)
│   ├── 4161ac9c-e3bb-4015-ac8f-7c67f5377468-result.json     (5.5 KB, 2026-03-25)
│   ├── 43de6a46-45bb-4b85-9b12-862f19eede54-container.json  (0.2 KB, 2026-03-25)
│   ├── 4a8f6b59-edce-40ba-aedc-f0e0140394e2-container.json  (1.0 KB, 2026-03-25)
│   ├── 560ac27b-edcc-4974-bb8b-f17771cea6a8-container.json  (1.0 KB, 2026-03-25)
│   ├── 5ab7d9c5-6127-4d9b-9982-1401a0e205f7-container.json  (5.8 KB, 2026-03-25)
│   ├── 6b0d24ad-8767-4d2e-8f7b-072b2d6f33c1-result.json     (5.5 KB, 2026-03-25)
│   ├── 6da673e9-d949-491e-8206-5cfd99069857-result.json     (5.5 KB, 2026-03-25)
│   ├── 6e8448ae-7f54-4e70-b9d5-0b122fb6a10c-result.json     (5.5 KB, 2026-03-25)
│   ├── 788c54eb-14ce-4836-add3-0233d6aba168-result.json     (5.5 KB, 2026-03-25)
│   ├── 7c70acb2-fce4-46de-baa4-61b7baf9ae3c-result.json     (5.5 KB, 2026-03-25)
│   ├── 86d1a4ea-5384-4ca9-847c-b0777fa3027e-result.json     (5.5 KB, 2026-03-25)
│   ├── 98bd553a-bf38-412f-a9f0-5018029266a8-container.json  (1.0 KB, 2026-03-25)
│   ├── 9c0c9f4d-7980-46a4-9a66-d4aba8ecaf95-result.json     (5.5 KB, 2026-03-25)
│   ├── a39d2a29-ce62-4582-b00a-82850b06a55d-result.json     (5.5 KB, 2026-03-25)
│   ├── b0ebf0f2-6345-4fd6-83a0-2071cc82a2aa-container.json  (1.0 KB, 2026-03-25)
│   ├── d8104905-401f-47ff-9231-a92dd985ed95-container.json  (1.1 KB, 2026-03-25)
│   ├── d83e88de-ecbd-4687-a168-58b407d29a96-result.json     (5.5 KB, 2026-03-25)
│   ├── df8fb4bc-b024-439f-8725-b6234a9bc09b-container.json  (1.0 KB, 2026-03-25)
│   ├── edce175f-6e44-4265-873a-1558de02301e-result.json     (5.5 KB, 2026-03-25)
│   ├── fb21616f-e6cb-4b61-87aa-2a1cde40f4a5-result.json     (5.5 KB, 2026-03-25)
│   └── fe676af1-5e9d-49ad-a3c3-7c97d818f388-result.json     (5.5 KB, 2026-03-25)
├── conftest.py       # Pytest 全局配置文件及 Fixtures (2.0 KB, 2026-03-25)
├── data/             (dir, 2026-03-25)
│   └── test_cases.py  # data/test_cases.py (8.1 KB, 2026-03-25)
├── generate_tree.py  # 每次 git commit 自动更新 README (6.0 KB, 2026-03-25)
├── lib/              (dir, 2026-03-25)
│   ├── ai_analyzer.py      # AI 分析器模块 (4.1 KB, 2026-03-25)
│   └── iec61850_client.py  # IEC 61850 客户端模块 (4.8 KB, 2026-03-25)
├── reports/          (dir, 2026-03-25)
│   ├── Execution_Summary_20260325_011944.html      (120.1 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_012715.xlsx  (7.1 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_012717.xlsx  (7.1 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_013012.xlsx  (7.1 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_015339.xlsx  (6.6 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_020159.xlsx  (7.4 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_020611.xlsx  (7.4 KB, 2026-03-25)
│   ├── Quality_Report_20260325_011944.xlsx         (5.9 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_012715.html     (31.0 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_012717.html     (120.1 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_013012.html     (119.7 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_015339.html     (119.3 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_020159.html     (119.3 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_020611.html     (119.3 KB, 2026-03-25)
│   ├── Technical_Log_20260325_014556.html          (118.6 KB, 2026-03-25)
│   ├── Technical_Log_20260325_014614.html          (118.6 KB, 2026-03-25)
│   ├── Technical_Log_20260325_014824.html          (118.6 KB, 2026-03-25)
│   ├── Technical_Log_20260325_014842.html          (118.6 KB, 2026-03-25)
│   ├── Technical_Log_20260325_015209.html          (118.8 KB, 2026-03-25)
│   ├── report_20260325_004710.html                 (120.1 KB, 2026-03-25)
│   ├── summary_20260325_004710.xlsx                (5.7 KB, 2026-03-25)
│   └── 硬件监控测试报告_20260325_003851.html               (123.1 KB, 2026-03-25)
├── run.py            # 项目运行入口 (4.9 KB, 2026-03-25)
└── tests/            (dir, 2026-03-25)
    └── test_hardware_to_web.py  # 测试脚本 (3.7 KB, 2026-03-25)
```

</details>
<!-- TREE_END -->












---

## 学习步骤
### 1. promt
* 准备一个自动化测试项目，目的是希望看到硬件测试设备通过接口传输到web的数据，如果报错的话则用ai分析报错原因并返回ai告知到结果，同时保证数据的安全性。
一共实现20个test case，case你来决定，test case可以放在单独的文件里方便维护。
全部用python语言。
必须调用61850接口，必须需要使用到playwright，必须能肉眼看到页面交互。
告诉我详细的建立文件的步骤，项目结构，代码里的注释尽可能详细，最好每一个行为都要有注释，比如用了fixture就注释说一下为什么用。从零开始细节教学，如果有专业术语必须要解释并且双语。文件夹根目录为playwright-test-projects

### 2. 激活虚拟环境
* python3 -m venv venv //这条命令会在文件夹里生成一个名为 venv 的文件夹，存放这个项目专用的 Python。
* source venv/bin/activate // 行完这个，你会发现终端提示符前面多了个 (venv) 字样，说明你已经进入了“样板间”。

### 3. 安装依赖
* python generate_tree.py --install
* 由于 iec61850-client 在 Windows/Python 环境下安装极易出错（涉及 C 编译），我们在教学中采用 Scapy 库来模拟 61850 报文，这是安全和测试领域最专业的工具。

```
# 安装 Scapy 用于处理 61850 报文
pip install scapy 

# 安装 Playwright 自动化框架
pip install playwright

#pyminimms 是一个常用的 Python 61850/MMS 库；openai 用于 AI 分析。
playwright install chromium

# 安装 OpenAI SDK 用于 AI 分析
pip install openai

# 安装 Flask 用于模拟 Web 后台接口
pip install flask

pip install scapy playwright pytest pytest-playwright python-dotenv openai

#生成报告
pip3 install pytest-html
pip install pandas openpyxl
pip install allure-pytest

#安装allure
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install allure
allure --version

#查看报告
allure serve allure-results

```

---

## 学习笔记梳理

### 1. playwright专业术语
* Browser Instance
* Browser Context
* Browser Page
* Playwright Locator
* Auto-waiting // 在你执行 click() 或 fill() 之前，Playwright 会自动检查元素是否：Visible (可见)、Attached (已挂载到 DOM)、Stable (动画已停止)、Enabled (非禁用状态)。如果不满足，它会持续重试直到超时。
* Test Fixtures // 它包含 Setup (执行前准备) 和 Teardown (执行后清理)。例如 page 就是一个内置 Fixture，它帮你自动处理了浏览器启动和关闭。
* Web-First Assertions // 它们是异步且会自动重试的。例如 await expect(locator).toBeVisible() 不会立即失败，它会反复检查元素是否出现，直到达到设定的超时时间（默认 5 秒）。
* Codegen // 打开一个浏览器，你在网页上的所有点击、输入都会在侧边窗口同步生成高质量的 Playwright 代码。
* Trace Viewer // 它记录了测试运行的每一个瞬间。你可以查看到每一步操作前后的 DOM 快照、Network (网络请求)、Console (控制台日志)。
* Storage State // 你可以先登录一次，将 Cookie 和 LocalStorage 保存为一个 JSON 文件。之后的几百个测试用例直接加载这个 JSON，跳过登录步骤。
* Parallelization //Playwright 默认根据 CPU 核心数启动多个 Worker Processes (工作进程) 同时运行测试。

### 2. IEC 61850标准
* 👉 IEC 61850 = 标准（Standard）它里面包含了协议、数据模型、通信规则等一整套规范。
* IED (Intelligent Electronic Device): 智能电子设备（如施耐德的保护继电器）。
* MMS (Manufacturing Message Specification): 制造报文规范（61850 传输数据的核心协议）。
* Dataset (数据集): IED 中打包传输的一组逻辑值（如电压、电流）。
* Logical Node (LN): 逻辑节点（设备功能的最小单位，如测量节点 MMXU）。
* Data Consistency Check: 数据一致性检查（验证协议层和 UI 层数据是否同步）。

---

### 2. 工业专业术语
* 由于 iec61850-client 在 Windows/Python 环境下安装极易出错（涉及 C 编译），我们在教学中采用 Scapy 库来模拟 61850 报文，这是安全和测试领域最专业的工具。

---

## 问题与解决方法
### 1. 在sync的时候有弹窗报错：
* 归因：vpn不稳定导致
* 解决步骤：
    1. 报错弹窗
    2. Show Command Output查看报错信息
    3. > git pull --tags origin main
fatal: unable to access 'https://github.com/jcc371620/playwright-test-projects.git/': Failed to connect to github.com port 443 after 21054 ms: Could not connect to server
    4. gemini分析

### 2. .git/hooks/pre-commit
* 归因： .git/hooks/ 是本地目录，不会被 Git 提交，不会跟着仓库同步
* 解决步骤：
    1. 第一步：进入 hooks 目录 // cd .git/hooks
    2. 创建 pre-commit：
        Linux / Mac / Git Bash: touch pre-commit
        Windows: New-Item pre-commit
    3. 写内容： 
        #!/bin/sh
        python generate_tree.py
        git add README.md
    4. 给执行权限：
        chmod +x pre-commit
    5. 验证是否生效：
        git commit -m "test"