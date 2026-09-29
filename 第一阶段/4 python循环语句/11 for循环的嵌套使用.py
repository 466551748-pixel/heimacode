"""
 演示嵌套应用for循环
 for和while可以相互嵌套使用
"""
# 坚持表白100天，每天都送10朵花
for i in range(1,100):
    print(f"今天是向小美表白的第{i}天")
    for j in range(1,10):
        print(f"送的第{j}朵花",end=" ")