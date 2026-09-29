"""
 目标：掌握函数作为参数传递
 我们学习的函数本身，也可以作为参数传入另一个函数内，这是一种计算逻辑的传递，而非数据的传递
 计算的数字是确定的，计算数据的逻辑是不确定的

"""
# 定义一个函数，接收另一个函数作为传入参数
def test_func(data):
    result = data(1,2) # 这里确定compute是一个函数
    print(f"compute参数的类型是：{type(data)}")
    print(f"计算的结果是：{result}")

# 定义一个函数，准备作为参数传入另一个函数
def compute(x,y):
    return x+y

# 调用
test_func(compute)