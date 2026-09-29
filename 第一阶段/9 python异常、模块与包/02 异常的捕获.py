"""
 为什么要捕获异常？
 答：世界上没有完美的程序，运行的过程中都有可能出现bug，也就是异常，使程序无法运行
    我们要做的，不是力求程序完美运行，而是在力所能及的范围内，对可能出现的bug，进行提前准备，提前处理
    这种行为我们称之为：异常处理（捕获异常）

 当我们的程序遇到了bug，会有俩种情况
 1.整个程序因为一个bug停止运行
 2.对bug进行提醒，整个程序继续运行
 显然我们之前遇到的是第一种情况，但是在真实工作中不可能因为一个bug就让整个程序崩溃，所以我们希望达到的是第二种情况，这时我们需要捕获异常
 捕获异常的作用：提前假设某处会出现异常，提前做好准备，当真的出现了异常，可以有后续的手段

 一.捕获常规异常基本语法
 try:
    可能发生错误的代码
 except:
    如果出现异常执行的代码

 快速入门：尝试用r打开文件，如果文件不存在，则用w打开
 try:
    f = open("linux.txt","r")
 except:
    f = open("linux.txt","w")

 二.捕获指定异常
 try:
    print(name)
 except NameError as e:
    print("name变量未定义错误")
 注意：e是异常对象,记录了异常的具体信息

 三.捕获多个异常:把要捕获的异常类型名字，放到except后，并使用元组方式书写
 try:
    print(1/0)
 except(NameError,ZeroDivisionError):
    print("ZeroDivision错误...")

 四.异常else：else表示如果没有异常要执行的代码
 try:
    print(1)
 except Exception as e:
    print(e)
 else:
    print("我是else，是没有异常的时候执行的代码")

 五.异常finally：表示无论是否异常都要执行的代码，例如关闭文件
 try:
    f = open("linux.txt","r")                  可能发现异常的语句
 except Exception as e:
    f = open("linux.txt","w")                  出现异常的准备手段
 else:
    print("没有异常，真开心")                     未出现异常时应该做的事情
 finally:
    print("我是finally，有没有异常我都要执行")      不管有没有异常都要做的事
    f.close()
"""

# 演示捕获异常

# 基本捕获语法
try:
    f = open("/Users/zhuangyan/Desktop/未命名文件夹/捕获异常.txt","r",encoding="utf-8")
except:
    print("出现异常了，因为文件不存在，我将r模式改为w模式去打开")
    f = open("/Users/zhuangyan/Desktop/未命名文件夹/捕获异常.txt","w",encoding="utf-8")

# 捕获指定异常
try:
    print(name)
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)

# 捕获多个异常：未正确设置捕获异常类型，将无法捕获异常
try:
    1/0
except(NameError,ZeroDivisionError) as e:
    print("出现了变量未定义 或者 除0的异常错误")

# 捕获全部异常:一开始的基本语法就是捕获全部异常，这里是第二种写法，Exception是顶级的异常
try:
    1/0
except Exception as e:
    print("出现异常了")