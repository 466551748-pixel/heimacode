"""
 学习目标：
 1.理解继承的概念
 2.掌握继承的使用方法
 3.掌握pass关键字的作用

 什么是继承？
 答：就是一个类，继承另一个类的成员变量和成员方法（不含私有）

 单继承语法： 将从父类那里继承（复制）来成员变量和成员方法（不含私有）
 class 类名(父类目):
    类内容体

 多继承语法  一个子类继承了多个父类
 class 类名(父类1,父类2,,,,父类n)
    类内容体
 注意：多个父类中，如果有同名的，那默认以继承顺序从左到右为优先级，即 先继承的保留，后继承的被覆盖

"""

# 演示单继承
class Phone:
    IMEI = None      # 序列奥
    producer = "同名左边先"  # 厂商

    def call_by_4g(self):
        print("4g通话")

class Phone2022(Phone):
    face_id = "10001" # 面部识别id
    def call_by_5g(self):
        print("2022年新功能：5g通话")
phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()

# 演示多继承
class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    rc_type = "红外遥控"
    def control(self):
        print("红外遥控开启了")

class MyPhone(Phone, RemoteControl, NFCReader):
    def sss(self):
        print(f"{self.rc_type}")
    pass           # 不想加功能了，用pass关键字，为了让我们的语法不报错

phone = MyPhone()
phone.call_by_4g()
phone.control()
phone.write_card()
phone.read_card()
phone.sss()
print(phone.producer)