"""
 工厂模式：
 当需要大量创建一个类的实例的时候，可以使用工厂模式
 即：从原生的使用类的构造去创建对象的形式，迁移到，基于工厂提供的方法去创建对象的形式

 优点：
 1.大批量创建对象的时候有统一的入口，易于代码维护
 2.当发生修改，仅修改工厂类的创建方式即可
 3.符合现实世界的模式，即由工厂来制作产品（对象）
"""
# 演示设计模式之工厂模式
class Person:
    pass

class Worker(Person):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class PersonFactory:
    def get_person(self,p_type):
        if p_type == 's':
            return Student
        elif p_type == 'w':
            return Worker
        else:
            return Teacher

pf = PersonFactory()
worker = pf.get_person('w')
teacher = pf.get_person('t')
student = pf.get_person('s')
