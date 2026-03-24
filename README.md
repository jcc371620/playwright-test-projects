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
│   ├── 03daf911-05cf-4912-8196-6550faeec0e1-result.json     (5.5 KB, 2026-03-25)
│   ├── 04a457c6-7b1e-49fd-ae01-716c2a3f04e1-container.json  (1.0 KB, 2026-03-25)
│   ├── 05a86bad-2eeb-4772-8fc6-fc3932427316-container.json  (5.8 KB, 2026-03-25)
│   ├── 07149a64-f2a0-4e58-9d1a-5502196edc80-container.json  (1.1 KB, 2026-03-25)
│   ├── 17deec2c-8323-4a0a-bbd7-fdd48697e880-result.json     (5.5 KB, 2026-03-25)
│   ├── 183addaf-4fca-45b0-ae30-334a527e3c93-result.json     (5.5 KB, 2026-03-25)
│   ├── 2bb68097-d829-4751-9228-61a741958213-container.json  (0.2 KB, 2026-03-25)
│   ├── 2d1d1285-5c01-4958-b048-e47cea5955c1-container.json  (1.0 KB, 2026-03-25)
│   ├── 3184e7f5-f304-4b68-bc80-5ea6905f8593-result.json     (5.5 KB, 2026-03-25)
│   ├── 34cafb63-2630-474f-a126-1b278ca33c84-container.json  (1.0 KB, 2026-03-25)
│   ├── 47cd0b97-83e2-43ea-8b9b-36fef240f0ae-result.json     (5.5 KB, 2026-03-25)
│   ├── 4dc8cc20-f22a-407b-8566-0a66fcaa0997-result.json     (5.5 KB, 2026-03-25)
│   ├── 5360db20-2fee-40d8-abad-83795157521c-container.json  (1.0 KB, 2026-03-25)
│   ├── 60c750eb-4a27-44e5-a7fe-dd4140ff324b-result.json     (5.5 KB, 2026-03-25)
│   ├── 68c8ec80-8220-40f6-b0aa-11c10de56e63-result.json     (5.5 KB, 2026-03-25)
│   ├── 6f90a69f-ca96-4da9-adae-e33903742349-container.json  (1.0 KB, 2026-03-25)
│   ├── 7abfa122-b15b-433d-af26-c9c9d0110b7a-result.json     (5.5 KB, 2026-03-25)
│   ├── 7f277e76-dd3a-465d-ba51-12fb09e6ce34-result.json     (5.5 KB, 2026-03-25)
│   ├── 82b3655a-b8f5-484b-8de8-1736fe59bd5b-result.json     (5.5 KB, 2026-03-25)
│   ├── a922d188-4d82-4c21-adff-b9cad5a422b8-container.json  (1.0 KB, 2026-03-25)
│   ├── ad81c20c-c40c-4bb0-a81c-59cae3ec9dde-result.json     (5.5 KB, 2026-03-25)
│   ├── affb69b1-41c0-4920-8c6d-8c0e472b89ce-result.json     (5.5 KB, 2026-03-25)
│   ├── b1e9884f-c1f6-4402-9b1b-5e373e7aed60-container.json  (1.0 KB, 2026-03-25)
│   ├── b353a723-ba68-4106-b88a-1cd05ad602a6-result.json     (5.5 KB, 2026-03-25)
│   ├── ba75bcd2-0d81-4068-8bbb-28a34f9cae53-container.json  (1.0 KB, 2026-03-25)
│   ├── c5ef7069-2d71-49dd-8927-269f948761f3-result.json     (5.5 KB, 2026-03-25)
│   ├── d9a19b75-a3fa-41c0-ab24-39a42cd96c31-result.json     (5.5 KB, 2026-03-25)
│   ├── e2138aac-81d9-4b41-b34e-26b7352cf2f5-result.json     (5.5 KB, 2026-03-25)
│   ├── e990b27e-943d-44fd-887b-d78f9fa3660b-result.json     (5.5 KB, 2026-03-25)
│   ├── f31cd156-c579-44d7-9f51-e15c5d88e321-result.json     (5.5 KB, 2026-03-25)
│   └── f68b5e65-da06-4ec3-8b14-c38aa01c90d8-result.json     (5.5 KB, 2026-03-25)
├── conftest.py       # Pytest 全局配置文件及 Fixtures (2.0 KB, 2026-03-25)
├── data/             (dir, 2026-03-25)
│   └── test_cases.py  # data/test_cases.py (8.1 KB, 2026-03-25)
├── generate_tree.py  # 每次 git commit 自动更新 README (6.0 KB, 2026-03-25)
├── lib/              (dir, 2026-03-25)
│   ├── ai_analyzer.py      # AI 分析器模块 (2.9 KB, 2026-03-25)
│   └── iec61850_client.py  # IEC 61850 客户端模块 (4.8 KB, 2026-03-25)
├── reports/          (dir, 2026-03-25)
│   ├── Execution_Summary_20260325_011944.html      (120.1 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_012715.xlsx  (7.1 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_012717.xlsx  (7.1 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_013012.xlsx  (7.1 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_015339.xlsx  (6.6 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_020159.xlsx  (7.4 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_020611.xlsx  (7.4 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_022508.xlsx  (7.4 KB, 2026-03-25)
│   ├── Quality_Report_20260325_011944.xlsx         (5.9 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_012715.html     (31.0 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_012717.html     (120.1 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_013012.html     (119.7 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_015339.html     (119.3 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_020159.html     (119.3 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_020611.html     (119.3 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_022508.html     (119.3 KB, 2026-03-25)
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