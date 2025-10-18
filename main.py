
s = input("请输入一行字符：")

# 初始化各类字符计数器
letter_count = 0  # 英文字符计数器
digit_count = 0   # 数字计数器
space_count = 0   # 空格计数器
other_count = 0   # 其他字符计数器

# 遍历输入的每一个字符
for char in s:
    if char.isalpha():  # 判断是否为英文字符（字母）
        letter_count += 1
    elif char.isdigit():  # 判断是否为数字
        digit_count += 1
    elif char.isspace():  # 判断是否为空格
        space_count += 1
    else:  # 其他字符
        other_count += 1

# 按照要求格式输出结果
print("英文字符:", letter_count)
print("数字:", digit_count)
print("空格:", space_count)
print("其他字符:", other_count)
