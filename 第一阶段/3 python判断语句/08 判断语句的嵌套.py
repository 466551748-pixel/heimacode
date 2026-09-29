"""
 if 条件1:
    if 条件2:
"""
'''
print("欢迎来到游乐园")
if int(input("请输入你的身高：")) > 120:
    print("你的身高大于120cm,不可以免费")
    print("不过如果你的VIP等级高于3，还是可以免费游玩")
    if int(input("请输入你的VIP等级：")) >3:
        print("恭喜你，你的VIP等级大于3，可以免费游玩")
    else:
        print("sorry,你需要补票10元")
else:
    print("欢迎你小朋友，身高低于120cm，可以免费游玩")
'''
age = int(input("请输入你的年龄："))
hire_year = int(input("请输入你的入已职年份："))
VIP = int(input("请输入你的VIP等级："))
if age >= 18 and age < 30:
    if hire_year >= 2:
        print("可以领取")
    elif VIP >= 3:
        print("可以领取")
else:
    print("领取失败")

