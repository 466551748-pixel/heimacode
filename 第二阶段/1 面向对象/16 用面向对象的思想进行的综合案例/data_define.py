"""
 数据定义的类
"""
class Record:

    def __init__(self,date,order_id,money,province):
        self.date = date             # 订单日期
        self.order_id = order_id     # 订单id
        self.money = money           # 订单金额
        self.province = province     # 销售省份

    def __str__(self):     # 给用户看的
        return f"{self.date},{self.order_id},{self.money},{self.province}"

    def __repr__(self):   # 列表，字典。。等等元素里显示数据需要用这个魔术方法
        return self.__str__()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"{self.name}今年{self.age}岁"  # 友好，给用户
#
#     def __repr__(self):
#         return f"Person(name='{self.name}', age={self.age})"  # 详细，给开发者
#
#
# p = Person("张三", 20)
#
# # 给用户看
# print(p)  # 张三今年20岁
#
# # 给开发者看
# p  # Person(name='张三', age=20)
# repr(p)  # Person(name='张三', age=20)
#
# # 列表里（调试用）
# print([p])  # [Person(name='张三', age=20)]