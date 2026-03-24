# playwright-test-projects

本项目用于学习Pytest + Playwright 自动化测试

---

## Project Structure

<!-- TREE_START -->
<details>
<summary>📂 Project Structure（点击展开）</summary>

```text
├── README.md         # playwright-test-projects (2.9 KB, 2026-03-24)
├── generate_tree.py  # 根据vscode项目结构，生成readme里的递归生成树状项目结构。 (4.3 KB, 2026-03-24)
└── test3.py          # 测试递归树状结构 (0.0 KB, 2026-03-24)
```

</details>
<!-- TREE_END -->


---

## 学习笔记梳理

### 1. 专业术语
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

### 2. 

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