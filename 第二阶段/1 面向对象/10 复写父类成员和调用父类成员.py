"""
 学习目标：
 1.掌握复写父类成员的语法
 2.掌握如何在子类中调用父类成员

 复写：
 子类继承父类的成员属性和成员方法后，如果对其"不满意"，那么可以进行复写，即：在子类中重新定义同名的属性或方法即可

 子类调用父类同名成员：
 一旦复写父类成员，那么类对象调用成员的时候，就会调用复写后的新成员
 如果需要使用被复写的父类的成员，
 方法1：
 1.父类名.成员变量
 2.父类名.成员方法(self)   注意不要少了self
 方法2：
 1.super().成员变量
 2.super().成员方法()
"""
class Phone:
    IMEI = None
    producer = "ITCAST"
    def call_by_5g(self):
        print("使用5g网络进行通话")

# 定义子类，复写父类成员
class MyPhone(Phone):
    producer = "ITHEIMA"         # 复写父类的成员属性

    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")
        # print("使用5g网络进行通话")
        # 在子类中，调用父类成员

        # 方式1
        print("----------方式1------------")
        print(f"父类的厂商是：{Phone.producer}")
        Phone.call_by_5g(self)
        # 方式2
        print("----------方式2------------")
        print(f"父类的厂商是：{super().producer}")
        super().call_by_5g()
        print("关闭CPU单核模式，确保性能")



phone = MyPhone()
phone.call_by_5g()
print("=====================")
phone1 = Phone()
phone1.call_by_5g()


