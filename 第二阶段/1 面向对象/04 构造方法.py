"""
 学习目标：
 掌握使用构造方法向成员变量赋值
 因为原本的赋值方法太过繁琐，所以需要一个更高效的方法，引出构造方法

 python类可以使用：__init__()方法，称之为构造方法
 可以实现：
 1.在创建类对象（构造类）的时候，会自动执行
 2.在创建类对象（构造类）的时候，将传入参数自动传递给__init__方法使用
"""

# 演示使用构造方法对成员变量进行赋值
class Student:
    name = None                  # 这三行代码可以省略，因为19 20 12行代码既有赋值的功能也有定义的功能


    age = None
    gender = None

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
stu_1 = Student("许晴","18","女")
print(stu_1.name)
print(stu_1.age)
print(stu_1.gender)