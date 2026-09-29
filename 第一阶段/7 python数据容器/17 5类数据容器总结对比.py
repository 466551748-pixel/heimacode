"""
 数据容器可以从以下视角进行简单分类
    1.是否支持下标索引
        支持：列表、元组、字符串 （序列类型）
        不支持：集合、字符串    （非序列类型）
    2.是否支持重复元素
        支持：列表、元组、字符串 （序列类型）
        不支持：集合、字符串    （非序列类型）
    3.是否可以修改
        支持：列表、集合、字典
        不支持：元组、字符串
 基于各类数据容器的特点，它们的应用场景如下：
    1.列表：一批数据，可修改，可重复的存储场景
    2.元组：一批数据，不可修改，可重复的存储场景
    3.字符串：一串字符串的存储场景
    4.集合：一批数据，去重存储场景
    5.字典：一批数据，可用key检索value的存储场景
"""

# 演示变量的类型注解

# 基础数据类型注解
var_1:int = 1
var_1:str = "zhuangyan"
var_1:bool = True
# 类对象类型注解
class Student:
    pass
stu_1:Student = Student()
# 基础容器类型注解
my_list:list = [1,2,3]
my_tuple:tuple = (1,2,3)
my_dict:dict = {"name":"庄严","age":18}
# 容器类型详细注解
my_list1:list[int] = [1,2,3]
my_tuple1:tuple[int,str,bool] = (1,"庄严",True)
my_dict1:dict[str,int] = {"name":"庄严","age":18}
print(my_dict1)
