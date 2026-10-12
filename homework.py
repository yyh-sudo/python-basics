print("Hello World!")

PI = 3.14
age = 18
print("常量 PI =", PI, "，2 * PI =", 2 * PI)
print("变量 age =", age)
age = age + 1
print("过了一年，age =", age)

import keyword

age = 18
score = 95.5
num = 100
print("num 的值 =", num, "，num 的类型 =", type(num))
print("age 的值 =", age, "，age 的类型 =", type(age))
print("score 的值 =", score, "，score 的类型 =", type(score))
print("我爱沈阳")
print("真：", True, "，假：", False, "，类型：", type(True))

last_name = "阴"
first_name = "雨航"
print("firstName =", first_name, "| lastName =", last_name)
print("我的全名是：", last_name + first_name)

print("Python 的保留关键字有：")
print(keyword.kwlist)
print("'if' 是关键字吗？", keyword.iskeyword("if"))
print("'age' 是关键字吗？", keyword.iskeyword("age"))

print("常量 PI =", PI)
print("变量 age =", age)
print("字符串：嵌入式开发，你好！")

print(f"我今年的年龄是 {age} 岁")
print("我今年的年龄是 {} 岁".format(age))
print("我今年的年龄是 %d 岁" % age)

card = """
============= 我的名片 =============
姓名: 阴雨航
Email: yinyuhang@example.com
手机号: 15182103459
QQ: 123456789
学校: 辽东学院 · 信息工程学院
地址: 辽宁省丹东市振安区
===================================
"""
print(card)

pwd = input("请输入密码：")
print("密码的值 =", pwd, "，密码的类型 =", type(pwd))
print(f"你输入的密码为: [{pwd}]")

info = input("请输入用户名和密码（中间用空格隔开）：")
parts = info.split()
username = parts[0]
password = parts[1]
print("你输入的用户名是：", username)
print("你输入的密码是：  ", password)
print("它们的类型都是：", type(username), type(password))
print(f"欢迎回来，{username}！你的密码长度为 {len(password)} 位。")
