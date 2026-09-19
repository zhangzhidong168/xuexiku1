# 第1步：写一个文件
with open("my_note.txt", "w", encoding="utf-8") as f:
    f.write("今天学了文件读写\n")
    f.write("读用 r，写用 w\n")
    f.write("with 写法最方便\n")

print("文件已写入！")

# 第2步：读回来看
with open("my_note.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("文件内容是：")
print(content)