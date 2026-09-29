"""
 变量作用域：
    指的是变量的作用范围，变量在哪里可以用，在哪不能用
    主要分为2类：局部变量、全局变量 (按照函数体内外来区分)
    一.局部变量：定义在函数体内部的变量，只在函数体内部生效
    二.全局变量：指在函数体内、外都能生效的变量
"""
# 局部变量
def testA():
    num = 100
    print(f"1.{num}")
testA()
#print(num) 报错，num是局部变量，在函数外访问会报错

# 全局变量
num = 100
def test_a():
    print(f"2.{num}")
def test_b():
    print(f"3.{num}")
test_a()
test_b()
print(f"4.{num}")

"""
 思考：“testB”函数需要修改变量num的值为200，如何修改程序？
    解答：global关键字，在函数内声明变量为全局变量
"""
num = 300
def testC():
    print(f"5.{num}")

def testB():
    # global 关键字声明num是全局变量
    global num
    num = 500
    print(f"6.{num}")
testC()
testB()
print(f"7.{num}") # 经过global，num就是全局变量被修改为500