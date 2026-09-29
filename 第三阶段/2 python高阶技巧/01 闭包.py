"""
 学习目标：
 1.掌握闭包的用途和技巧
 2.掌握nonlocal关键字的作用

 闭包：
 例：通过全局变量account_amount来记录余额，尽管功能实现是ok的，但是仍有问题的
 1.代码在命名空间上（变量定义）不够干净、整洁
 2.全局变量有被修改的风险：被别的代码import得到全局变量
 出现闭包方法：
 在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数，我们把这个使用外部函数变量的内部函数称为闭包


 如何在内部函数中修改外部函数的变量：
 在内部函数里，使用nonlocal关键字修饰外部函数的变量，才可以在内部函数中修改

"""

# 简单闭包：先传入外层函数，传入后，被赋值的就变成了内层函数 这样logo就变成了对于outer是内部临时变量，没人能修改，对于inner又是外部全局变量
# import修改不了，只能重新调用outer改
def outer(logo):
    def inner(msg):
        print(f"{logo}{msg}{logo}")

    return inner
fn1 = outer("庄严")  # 只要outer传入了，这样fn1就变成了inner函数（因为最后的return返回的是inner）
fn1("庄粤")
fn2 = outer("庄严")("许晴")


# 原本函数
account_amount = 0
def atm(num,deposit=True):
    global account_amount
    if deposit:
        account_amount += num
        print(f"存款+{num}，账户余额：{account_amount}")
    else:
        account_amount -= num
        print(f"存款-{num}，账户余额：{account_amount}")
atm(300)
atm(300)
atm(100,deposit=False)

# 改成闭包
def outer_atm(outer_account_amount:int = 0):
    def inner(num,deposit=True):
        nonlocal outer_account_amount      # 才可以在内部函数修改
        if deposit:
            outer_account_amount += num
            print(f"存款+{num}，账户余额：{outer_account_amount}")
        else:
            outer_account_amount -= num
            print(f"存款-{num}，账户余额：{outer_account_amount}")
    return inner
fn3 = outer_atm(0)
fn3(300)
fn3(300)
fn3(100,deposit=False)

