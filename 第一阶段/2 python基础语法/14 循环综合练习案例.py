"""
 某公司账户余额1万元，给20位员工发工资
 1.员工编号从1到20，从1开始，依次领工资，每个人可以领取1000元
 2.领工资时，财务判断员工的绩效（1-10随机生成），如果低于5，则不发工资，下一位
 3.如果工资发完了，结束发工资
"""
import random
all_money = 10000
for i in range(1,21):
    num = random.randint(1,10)
    if all_money > 0:  # 这里逻辑有点问题，工资发完了应该立即结束程序，而不是落到else再去结束
        if num >= 5:
            all_money -= 1000
            print(f"员工{i},发放工资1000元，账户余额还剩{all_money}")
        else:
            print(f"员工{i},绩效{num}，不发工资，下一位")
            continue
    else:
        print("工资发完了，下个月领取吧")
        break
"""
ai进化版本！！！！！

all_money = 10000

for i in range(1, 21):
    # 先检查余额，没钱直接结束
    if all_money <= 0:           # ⭐ 放最前面,养成好习惯，资源检放在最前面
        print("工资发完了，下个月领取吧")
        break
    
    num = random.randint(1, 10)
    
    if num < 5:
        print(f"员工{i},绩效{num}，不发工资，下一位")
        continue
    
    # 能到这里：有钱 + 绩效合格
    all_money -= 1000
    print(f"员工{i},发放工资1000元，账户余额还剩{all_money}")
"""