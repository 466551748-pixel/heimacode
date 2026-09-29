"""
 目标：知道函数如何返回多个函数值

"""

# 问：如果一个函数有俩个return，函数如何执行呢？
# 答：只执行第一个return，原因是因为return可以退出当前函数，导致return下方的代码不执行
def return_num():
    return 1
    return 2
result = return_num()
print(result)
print()
# 一个函数多个返回值情况：按照返回值的顺序，写对应顺序的多个变量接收即可，用逗号隔开，支持不同类型的return
def test_return():
    return 1,2,"hello",True
x,y,z,u = test_return()
print(x)
print(y)
print(z)
print(u)