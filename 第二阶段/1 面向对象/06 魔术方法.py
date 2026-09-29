"""
 学习目标：
 掌握几种常用的类内置方法

 魔术方法：
 上文学到的 __init__ 构造方法，是python类内置方法之一
 这些内置的类方法，各有各特殊的功能，这些内置方法我们称之为：魔术方法
 如： __init__  __str__  __lt__  __le__  __eq__
"""

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # __str__ 魔术方法   若是没有这个直接str(stu)，显示的是内存地址
    def __str__(self):
        return f"Student类对象，name： {self.name}, age: {self.age}"
    # __lt__ 魔术方法    直接对2个对象进行比较是不可以的，但在类中实现这个，可以同时完成：小于符号和大于符号俩种比较
    def __lt__(self,other):
        return self.age < other.age
    # __le__ 魔术方法    大于等于 或 小于等于
    def __le__(self,other):
        return self.age <= other.age
    # __eq__ 魔术方法    若没有这个方法，==比较的是内存地址
    def __eq__(self,other):
        return self.age == other.age
# str
stu = Student('周杰伦',22)
print(stu)
print(str(stu))

# lt
stu_1 = Student('周杰伦',31)
stu_2 = Student('林俊杰',36)
print(stu_1 < stu_2)
print(stu_1 > stu_2)

# le
stu_1 = Student('周杰伦',31)
stu_2 = Student('林俊杰',36)
print(stu_1 <= stu_2)
print(stu_1 >= stu_2)

# eq
stu_1 = Student('周杰伦',31)
stu_2 = Student('林俊杰',36)
print(stu_1 == stu_2)
print(stu_1 == stu_2)
