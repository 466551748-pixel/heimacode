"""
 学习目标：
 1.理解多态的概念
 2.理解抽象类（接口）的编程思想

 多态：指的是：多种状态，即完成某个行为时，使用不同的对象会得到不同的状态
 同样的行为（函数），传入不同的对象，得到不同的状态

 多态常作用于继承关系上
 如：函数（方法）形参声明接收父类对象，实际传入父类的子类对象进行工作
 即：1.以父类做定义声明
    2.以子类做实际工作
    3.用以获得同一行为，不同状态

 抽象类：含有抽象方法的类称之为抽象类
 抽象方法：方法体是空实现的（pass） 称之为抽象方法

 为什么要使用抽象类？
 答：提出标准后，不同的厂家各自实现标准的要求，抽象类（父类）就好比定义一个标准，真正去实现这个标准的是子类
 如：制冷，每一家制冷的技术（自己的核心技术）不一样，但符合标准能制冷就行
 抽象就是个模板
 抽象类配合多态完成：
 1.抽象的父类设计（设计标准）
 2.具体的子类设计（实现标准）
"""
# 演示多态
class Animal:                 # 抽象类
    def speak(self):          # 抽象方法    定义函数但pass的意义：父类用来确定有那些方法，具体的方法实现由子类自行决定，这种写法叫抽象类，也可以叫接口
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal:Animal):
    # 制造点噪音，需要传入Animal对象
    animal.speak()

# 使用2个子类对象来调用函数
dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)

# 演示抽象类
class AC:
    def cool_wind(self):
        # 制冷
        pass

    def hot_wind(self):
        # 制热
        pass

    def swing_l_r(self):
        # 左右摆风
        pass

class midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")

    def hot_wind(self):
        print("美的空调制热")

    def swing_l_r(self):
        print("美的空调左右摆风")


class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def hot_wind(self):
        print("格力空调制热")

    def swing_l_r(self):
        print("格力空调左右摆风")

def make_cool(ac:AC):
    ac.cool_wind()

midea_ac = midea_AC()
gree_ac = GREE_AC()
make_cool(gree_ac)
make_cool(midea_ac)





