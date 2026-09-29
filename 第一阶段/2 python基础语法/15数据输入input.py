# 获取键盘输入

print("请告诉我你是谁？")
name = input()
print(f"我知道了，你是{name}")

# 等价于
name1 = input("请告诉我你是谁\n") # 小技巧：提示语句直接放入input
print(f"我知道了，你是{name1}")

# 数字类型：注意：无论键盘输入的是什么类型的数据，获得到的全都是字符串类型
phone_number = input("你的电话号码是")
print(type(phone_number))
phone_number = int(phone_number) # 必须手动转数据类型
print(type(phone_number))