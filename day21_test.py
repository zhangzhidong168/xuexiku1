# 定义一个字典
info = {
    "name": "张志栋",
    "week": "第三周",
    "learned": ["Git", "Markdown", "VS Code", "文件读写", "JSON"]
}

# 用 json 保存到文件
import json
with open("week3_summary.json", "w", encoding="utf-8") as f:
    json.dump(info, f, ensure_ascii=False, indent=2)

print("第三周学习总结已保存！")

# 读回来验证
with open("week3_summary.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print("姓名：" + loaded["name"])
print("学了" + str(len(loaded["learned"])) + "个技能")