# import json

# # 字典 → JSON 字符串
# data = {"name": "张志栋", "age": 48}
# text = json.dumps(data, ensure_ascii=False)
# print(text)
# # 输出：{"name": "张志栋", "age": 48}

# # JSON 字符串 → 字典
# text2 = '{"name": "张三", "age": 25}'
# data2 = json.loads(text2)
# print(data2["name"])
# # 输出：张三

import json

# # 写入 JSON 文件
# data = {"name": "张志栋", "age": 48, "skills": ["Python", "Git"]}

# with open("info.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=2)

# print("JSON 文件已保存！")

# # 读取 JSON 文件
# with open("info.json", "r", encoding="utf-8") as f:
#     loaded = json.load(f)

# print("读取到的数据：")
# print(loaded["name"])
# print(loaded["skills"])


import json

# 第1步：创建一个字典
student = {
    "name": "张志栋",
    "age": 48,
    "skills": ["Python", "Git", "Markdown"],
    "goal": "AI大模型开发"
}

# 第2步：保存到 JSON 文件
with open("student.json", "w", encoding="utf-8") as f:
    json.dump(student, f, ensure_ascii=False, indent=2)

print("学生信息已保存！")

# 第3步：读回来
with open("student.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print("读取到的姓名：" + loaded["name"])
print("读取到的目标：" + loaded["goal"])
print("读取到的技能：" + str(loaded["skills"]))
