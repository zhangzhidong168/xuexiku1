# 我的第一个 VS Code Python 文件
name = "张志栋"
print("你好，我叫" + name)

# 算一下年龄
year = 2026
birth = 1978
age = year - birth
print("我今年" + str(age) + "岁")


# 按键盘ctrl + · 1 字的左边
# 打开终端
# 输入python + 文件名  回车输出

# 在sh 窗口 输入
# cd ~/文件夹名 (如：git_practice)
# code .         打开VS Code 当前文件夹
# git add .      把改动放进“待提交区”
# git commit -m "说明：（如：Day18：第一个VS Code Python文件）"     正式保存一个版本
# git push       把本地版本传到GitHub上
# git log        查看全部文件
# 直接按 q 退出


# # 1. 创建一个练习文件夹
# mkdir git_practice
# cd git_practice

# # 2. 初始化 Git 仓库
# git init

# # 3. 创建一个文件
# echo "第一版代码" > hello.py

# # 4. 查看状态
# git status

# # 5. 添加到暂存区
# git add .

# # 6. 提交（保存版本）
# git commit -m "第一版：创建hello.py"

# # 7. 修改文件
# echo "第二版代码，加了新功能" > hello.py

# # 8. 再提交
# git add .
# git commit -m "第二版：更新hello.py"

# # 9. 查看历史
# git log