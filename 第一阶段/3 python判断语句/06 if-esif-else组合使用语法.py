"""
if
elif
elif
else
记得条件之间要互斥
"""
height = int(input("请输入你的身高（cm）："))
vip_level = int(input("请输入你的vip等级（1-5）"))
# 通过if判断，使用多条件判断语句
print("欢迎来到游乐园")
if height <= 120:
    print("免费游玩")
elif vip_level > 3:
    print("免费游玩")
else:
    print("需要付款10元")


# 通过if判断，使用多条件判断语句
print("欢迎来到游乐园")
if int(input("请输入你的身高（cm）：")) <= 120:
    print("免费游玩")
elif int(input("请输入你的vip等级（1-5）")) > 3:
    print("免费游玩")
else:
    print("需要付款10元")