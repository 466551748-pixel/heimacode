import random
num = random.randint(1,10)
print(num)
guess_num1 = int(input("请输入第一次猜的数字："))
if guess_num1!= num:
    if guess_num1 > num:
        print("大了")
    elif guess_num1 < num:
        print("小了")
    guess_num2 = int(input("请输入第二次猜的数字："))
    if guess_num2 != num:
        if guess_num2 > num:
            print("大了")
        if guess_num2 < num:
            print("小了")
        guess_num3 = int(input("请输入第三次猜的数字："))
        if guess_num3 != num:
            if guess_num3 > num:
                print("大了")
            if guess_num3 < num:
                print("小了")
        else:
            print("恭喜你猜对了")
    else:
        print("恭喜你猜对了")
else:
    print("恭喜你猜对了")
