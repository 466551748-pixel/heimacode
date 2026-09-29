import random
num = random.randint(1,100)
# 通过一个布尔类型的变量，做循环是否能继续的标记
print(num)
flag = True
i = 0 # 记录总共猜了多少次
while flag :
    guess = int(input("请输入你猜测的数字："))
    i += 1
    if guess != num:
        if guess < num:
            print("小了")
        if guess > num:
            print("大了")
    else:
        flag = False
        print("猜对了")
        print(f"总共猜了{i}次")
