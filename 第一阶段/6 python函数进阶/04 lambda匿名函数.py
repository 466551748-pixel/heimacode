"""
 目标：掌握lambda匿名函数的语法
 函数的定义中：
    1.def关键字，可以定义带有名称的函数
    2.lambada关键字，可以定义匿名函数（无名称）
    有名称的函数，可以基于名称重复使用
    无名称的匿名函数，只能临时使用一次

 匿名函数定义语法：
    lambda 传入参数:函数体(一行代码)
        1.lambda是关键字，表示定义匿名函数
        2.传入参数表示匿名函数的形式参数，如x,y表示接受2个形式参数
        3.函数体，就是函数的执行逻辑，要注意；函数体只能写一行，无法写多行代码
"""
def test_func(compute):
    result = compute(1,2) # 这里确定compute是一个函数
    print(f"compute参数的类型是：{type(compute)}")
    print(f"计算的结果是：{result}")

def compute(x,y):
    return x+y
# 以上代码也可以通过lambda关键字，传入一个一次性使用的lambda匿名函数
test_func(lambda x,y:x+y) # 更简单，不用写 def compute