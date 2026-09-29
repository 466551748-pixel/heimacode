# 有几个偶数
num = 100
odd_number = 0
for i in range(1,num):
    if i % 2 == 0:
        odd_number += 1
print(odd_number)