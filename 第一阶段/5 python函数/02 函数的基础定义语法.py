"""
 1.函数的定义：
    def 函数名(传入参数):
        函数体
        return 返回值
 2.函数的调用：
    函数名(参数)
 3.注意事项
    1 参数不需要可以省略
    2 返回值不需要可以省略
    3 函数必须先定义后使用
"""
# 定义一个函数，输出相关信息
def say_hi():
    print("hi 我叫庄严")
say_hi() # 调用函数

def number():
    return 10
print(number()*number())
