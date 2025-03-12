import json

# 读取 Jupyter Notebook
with open("lab2_merged.ipynb", "r", encoding="utf-8") as f:
    notebook = json.load(f)

# 删除所有 cell 里的 "id" 字段
for cell in notebook["cells"]:
    cell.pop("id", None)

# 重新写回去
with open("lab2_merged_fixed.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Fixed notebook saved as lab2_merged_fixed.ipynb")