#根据vscode项目结构，生成readme里的递归生成树状项目结构。

# Promt: 根据vscode项目结构，生成readme里的递归生成树状项目结构。要求显示所有文件夹和文件的注释（比如我把注释写在每个文件的第一行）信息（大小 + 修改时间）。如果项目结构变了，树状图可以相应改变。 格式：文件名 #注释（文件大小，最后修改日期） 注意每一行要对齐

import os
import datetime
import re

ROOT_DIR = "."
OUTPUT_FILE = "README.md"

IGNORE = {".git", "__pycache__", "node_modules", ".idea", ".vscode"}

# 获取文件大小 + 修改时间
def get_file_info(path):
    size = os.path.getsize(path)
    mtime = datetime.datetime.fromtimestamp(os.path.getmtime(path))
    return f"{size/1024:.1f} KB", mtime.strftime("%Y-%m-%d")

# 获取文件第一行注释
def get_file_comment(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith(("#", "//", "/*", '"""', "'''")):
                    return line.lstrip("#/ ").strip()
                if line:  # 第一行不是注释就结束
                    break
    except:
        pass
    return ""

# 获取目录注释
def get_dir_comment(path):
    for name in [".dircomment", "README.md"]:
        file_path = os.path.join(path, name)
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            return line.lstrip("#/ ").strip()
            except:
                pass
    return ""

# 收集当前层（用于对齐）
def collect_items(root):
    items = []
    for name in sorted(os.listdir(root)):
        if name in IGNORE:
            continue

        path = os.path.join(root, name)

        if os.path.isdir(path):
            _, mtime = get_file_info(path)
            items.append({
                "name": name + "/",
                "comment": get_dir_comment(path),
                "info": f"(dir, {mtime})",
                "is_dir": True,
                "path": path
            })
        else:
            size, mtime = get_file_info(path)
            items.append({
                "name": name,
                "comment": get_file_comment(path),
                "info": f"({size}, {mtime})",
                "is_dir": False,
                "path": path
            })
    return items

# 构建树（核心：对齐）
def build_tree(root, prefix=""):
    tree = ""
    items = collect_items(root)

    if not items:
        return tree

    # 计算最大文件名长度（用于对齐）
    max_len = max(len(item["name"]) for item in items)

    for i, item in enumerate(items):
        connector = "└── " if i == len(items) - 1 else "├── "

        # 文件名填充空格（关键！）
        name_padded = item["name"].ljust(max_len)

        # 至少留2个空格再接 #
        base = f"{prefix}{connector}{name_padded}  "

        if item["comment"]:
            line = f"{base}# {item['comment']} {item['info']}"
        else:
            line = f"{base}{item['info']}"

        tree += line + "\n"

        # 递归子目录
        if item["is_dir"]:
            extension = "    " if i == len(items) - 1 else "│   "
            tree += build_tree(item["path"], prefix + extension)

    return tree

# 写入 README
def update_readme(tree_text):
    start = "<!-- TREE_START -->"
    end = "<!-- TREE_END -->"

    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = ""

    new_block = f"{start}\n```\n{tree_text}```\n{end}"

    if start in content and end in content:
        content = re.sub(f"{start}.*?{end}", new_block, content, flags=re.S)
    else:
        content += "\n## 📂 Project Structure\n\n" + new_block

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    tree = build_tree(ROOT_DIR)
    update_readme(tree)