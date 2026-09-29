"""
 什么是函数的嵌套？
    所谓函数嵌套调用指的是一个函数里面又调用了另一个函数
"""
def fun_b():
    print("2")

def fun_a():
    print("1")
    fun_b() # 调用了另一个函数
    print("3")

# 调用函数fun_a()
fun_a()
