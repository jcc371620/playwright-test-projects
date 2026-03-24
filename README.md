# playwright-test-projects

本项目用于学习Pytest + Playwright 自动化测试, 目的是能看到模拟硬件测试设备通过61850接口传输到web的数据，如果报错的话则用ai分析报错原因并返回ai告知到结果，同时保证数据的安全性，并且可以维护测试用例。

---

## Project Structure

<!-- TREE_START -->
<details>
<summary>📂 Project Structure</summary>

```text
├── .gitignore        # Python项目通用忽视规则 (1.0 KB, 2026-03-25)
├── README.md         # playwright-test-projects (26.8 KB, 2026-03-25)
├── allure-results/   (dir, 2026-03-25)
│   ├── 01a3b884-e2ac-4e7f-b514-37fd36f49541-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 0322661d-1dd9-448e-ba80-bcabd78948fd-container.json     (0.2 KB, 2026-03-25)
│   ├── 0e6f4467-92c8-49d6-9fd1-fac57ac0c1ae-container.json     (0.2 KB, 2026-03-25)
│   ├── 154ff783-5945-4629-8769-2f69b3327615-container.json     (0.4 KB, 2026-03-25)
│   ├── 1958cb0d-1da8-4234-95f2-9760930467e7-container.json     (0.2 KB, 2026-03-25)
│   ├── 2814efec-b1d4-436a-8bfe-40f67304b731-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 2adebad7-3481-422b-8197-277bb72fc3a7-container.json     (0.2 KB, 2026-03-25)
│   ├── 2b1e0d34-1530-4b69-a282-aface58e0fc7-container.json     (0.2 KB, 2026-03-25)
│   ├── 2d4339eb-09f2-4d27-b0e6-53f0da3f5813-container.json     (0.2 KB, 2026-03-25)
│   ├── 2fe2604e-eb28-4803-bf90-a8987c9d2fe4-result.json        (2.1 KB, 2026-03-25)
│   ├── 30c19ad3-d5c9-48c4-8402-47087181a316-container.json     (0.2 KB, 2026-03-25)
│   ├── 32228478-ee2d-45a0-84b4-a857cf6e391c-container.json     (0.2 KB, 2026-03-25)
│   ├── 3ff15362-3f1f-41e9-ae62-acaeb3965b92-container.json     (0.4 KB, 2026-03-25)
│   ├── 4f9c090d-9792-4593-83d6-0d577214efbb-container.json     (0.4 KB, 2026-03-25)
│   ├── 588649b6-9ca6-4187-a559-8857571433d5-container.json     (0.2 KB, 2026-03-25)
│   ├── 58e71048-3f35-4270-a7f6-9ffab678bd6f-container.json     (0.4 KB, 2026-03-25)
│   ├── 5caea6d8-379e-47bb-a093-516d0c598744-container.json     (0.2 KB, 2026-03-25)
│   ├── 5f449f02-fdf4-42dc-b7f4-b575f5537f4f-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── 5f941e8b-42ef-46ed-b27b-2aa5f1527376-container.json     (0.2 KB, 2026-03-25)
│   ├── 67f2f270-93a6-4dcb-9a1c-7a2ddeaaf38c-container.json     (0.6 KB, 2026-03-25)
│   ├── 697f99cd-eed5-4350-849a-3766088a468d-container.json     (0.4 KB, 2026-03-25)
│   ├── 6ba170e4-160b-42f7-9a9a-762ebe9fb585-container.json     (0.4 KB, 2026-03-25)
│   ├── 6f62cea3-e7d8-4a53-849f-05fd157be0cb-container.json     (0.4 KB, 2026-03-25)
│   ├── 8220793c-f465-4931-b753-362d33c1618c-container.json     (0.4 KB, 2026-03-25)
│   ├── 8652e77f-5f76-46e3-b2f1-9e3f22a08c20-container.json     (0.4 KB, 2026-03-25)
│   ├── 869a2241-4f8f-4832-b54f-69865acf8876-container.json     (0.4 KB, 2026-03-25)
│   ├── 8721e647-d153-4740-b377-89c75f3be43f-container.json     (0.4 KB, 2026-03-25)
│   ├── 8c1231df-1229-4732-848a-02b8c62f0ca4-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 8e0d3c83-e52d-4304-817f-91db76ca2e09-result.json        (3.3 KB, 2026-03-25)
│   ├── 911b5693-ae97-4852-bc9c-eca1bd3417e4-container.json     (0.2 KB, 2026-03-25)
│   ├── 93bbee9d-6cb7-4ffd-a327-7d89f4a70f9e-container.json     (0.4 KB, 2026-03-25)
│   ├── 94bc7c0c-e8f5-4339-836f-68908493721a-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── 971caa25-eb75-4a75-9fa9-921155a00040-container.json     (0.5 KB, 2026-03-25)
│   ├── 9735ff7c-1f6f-4d7a-bada-c5a32e10ce60-container.json     (0.5 KB, 2026-03-25)
│   ├── 9eb47934-aa34-43e5-b826-173d3852029c-container.json     (0.4 KB, 2026-03-25)
│   ├── a32d0d02-fb03-4645-9c56-c3492186d909-result.json        (7.8 KB, 2026-03-25)
│   ├── a43571ff-5978-413a-af3f-960b04dc3b68-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── a9084651-cf21-476d-8e62-47a5e14f4522-container.json     (0.2 KB, 2026-03-25)
│   ├── a94162fc-199a-4c4b-a6f5-9ce0b5d50e34-container.json     (0.4 KB, 2026-03-25)
│   ├── b41b92f4-9279-4521-ac66-afc313b68386-container.json     (0.2 KB, 2026-03-25)
│   ├── b4f526c9-2f52-4cb3-8033-186be1a6d51e-container.json     (0.4 KB, 2026-03-25)
│   ├── b7b3f2a2-86ff-4624-a1ef-bbc45a756da9-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── b8da72af-bfcf-45f5-b683-625e1018cc57-container.json     (0.2 KB, 2026-03-25)
│   ├── bcc1b2d8-90c5-4466-9b2f-dbbb299cc574-container.json     (0.4 KB, 2026-03-25)
│   ├── c0f1443d-b68e-4e61-9256-7bfab3470ad1-container.json     (0.2 KB, 2026-03-25)
│   ├── c386cf58-ce1d-4f13-9a9b-b166169e3756-result.json        (7.8 KB, 2026-03-25)
│   ├── c63b5c08-e5e6-4836-b3de-f1cd651709c7-container.json     (0.5 KB, 2026-03-25)
│   ├── cab12a85-54c0-47df-8350-a688ab365b30-container.json     (0.2 KB, 2026-03-25)
│   ├── d1a28211-72d2-46fb-a3db-83e8b66ca974-container.json     (0.2 KB, 2026-03-25)
│   ├── d27297ce-8eb1-42e0-8eb4-dd9c4da0190f-result.json        (7.8 KB, 2026-03-25)
│   ├── d3b4aef9-f116-46d8-bb94-f75662cfb23c-container.json     (0.4 KB, 2026-03-25)
│   ├── d3f67800-8ee0-4939-833f-fb57dbb5af41-attachment.txt     (0.1 KB, 2026-03-25)
│   ├── d6a0d298-1b97-4a0b-b8ae-7947ae717414-container.json     (0.4 KB, 2026-03-25)
│   ├── ef9ed021-b4a4-40dc-bc4e-850444842df7-container.json     (0.2 KB, 2026-03-25)
│   ├── f4f1eba9-e259-4fe2-9edc-9c7dbd88a920-container.json     (0.2 KB, 2026-03-25)
│   ├── f5187576-7b22-4df1-a326-64f50b558950-attachment.attach  (0.0 KB, 2026-03-25)
│   ├── f5e21eef-f5ac-4a31-9c06-989290e27c1f-container.json     (0.2 KB, 2026-03-25)
│   ├── f61b11c7-d7cc-4c09-99dd-9d4ea084b57d-container.json     (0.4 KB, 2026-03-25)
│   ├── fcd26136-c71c-4a66-a208-996c58de782b-container.json     (0.4 KB, 2026-03-25)
│   └── feabdd2f-d409-4adb-a050-695e6d03f303-attachment.attach  (0.0 KB, 2026-03-25)
├── conftest.py       # Pytest 全局配置文件及 Fixtures (2.0 KB, 2026-03-25)
├── data/             (dir, 2026-03-25)
│   └── test_cases.py  # data/test_cases.py (8.1 KB, 2026-03-25)
├── generate_tree.py  # 每次 git commit 自动更新 README (6.0 KB, 2026-03-25)
├── lib/              (dir, 2026-03-25)
│   ├── ai_analyzer.py      # AI 分析器模块 (2.9 KB, 2026-03-25)
│   └── iec61850_client.py  # IEC 61850 客户端模块 (4.8 KB, 2026-03-25)
├── mock_site/        (dir, 2026-03-25)
│   └── index.html  (0.6 KB, 2026-03-25)
├── reports/          (dir, 2026-03-25)
│   ├── Execution_Summary_20260325_011944.html      (120.1 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_012715.xlsx  (7.1 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_012717.xlsx  (7.1 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_013012.xlsx  (7.1 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_015339.xlsx  (6.6 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_020159.xlsx  (7.4 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_020611.xlsx  (7.4 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_022508.xlsx  (7.4 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_022809.xlsx  (7.4 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_023112.xlsx  (7.4 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_023344.xlsx  (7.4 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_024102.xlsx  (7.4 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_025135.xlsx  (7.4 KB, 2026-03-25)
│   ├── QA_Integration_Report_20260325_025829.xlsx  (7.4 KB, 2026-03-25)
│   ├── Quality_Report_20260325_011944.xlsx         (5.9 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_012715.html     (31.0 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_012717.html     (120.1 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_013012.html     (119.7 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_015339.html     (119.3 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_020159.html     (119.3 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_020611.html     (119.3 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_022508.html     (119.3 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_022809.html     (119.3 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_023112.html     (119.3 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_023344.html     (980.6 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_024102.html     (980.6 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_025135.html     (980.6 KB, 2026-03-25)
│   ├── Technical_Evidence_20260325_025829.html     (127.3 KB, 2026-03-25)
│   ├── Technical_Log_20260325_014556.html          (118.6 KB, 2026-03-25)
│   ├── Technical_Log_20260325_014614.html          (118.6 KB, 2026-03-25)
│   ├── Technical_Log_20260325_014824.html          (118.6 KB, 2026-03-25)
│   ├── Technical_Log_20260325_014842.html          (118.6 KB, 2026-03-25)
│   ├── Technical_Log_20260325_015209.html          (118.8 KB, 2026-03-25)
│   ├── report_20260325_004710.html                 (120.1 KB, 2026-03-25)
│   ├── summary_20260325_004710.xlsx                (5.7 KB, 2026-03-25)
│   └── 硬件监控测试报告_20260325_003851.html               (123.1 KB, 2026-03-25)
├── run.py            # run.py (4.9 KB, 2026-03-25)
└── tests/            (dir, 2026-03-25)
    └── test_hardware_to_web.py  # test_hardware_to_web.py (3.8 KB, 2026-03-25)
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