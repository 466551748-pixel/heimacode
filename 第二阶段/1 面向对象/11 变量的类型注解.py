"""
 为什么需要类型注解？
 在pycharm中编写代码，会有自动提示可用代码，例如 list.app.. 会出现提示 list.append(self,__object) 按tab自动补全
 思考：为什么pycharm工具能做到这一点，它是如何知道对象有append方法？
 答：因为pycharm确定这个对象是list类型，从而能推断是里面的append方法

 为什么内置模块的方法可以提示类型，自己定义的就不行
 答:因为pycharm无法通过代码确定应该传入什么类型，我们需要使用类型注解

 类型注解：
 python在3.5版本的时候引入了类型注解，以方便（静态类型检查工具、IDE）等第三方工具
 静态类型检查工具一读就知道：123 是整数，不是字符串，于是提前报个错提醒你。不用等你运行程序才发现问题
 作用：在代码中涉及数据交互的地方，提供数据类型的注解（显示的说明）
 主要功能：
 1.帮助第三方IDE工具（如pycharm）对代码进行类型推断，协助做代码提示
 2.帮助开发者自身对变量进行类型注释
 总结：其实简单来说，就是对数据的类型进行标注一下，不仅让pycharm工具能够得知类型，对我们自己也相当于打了个注释
 支持：
 1.变量的类型注解
 2.函数（方法）的形参列表和返回值的类型注解

 语法：
 1.变量:类型
 2.# type:类型
 除了第一种，也可以在注释中进行类型注解

 类型注解的限制：
 类型注解并不会真正的对类型做验证和判断，也就是，类型注解仅仅是提示性的，不是决定性的，仅仅是备注
 var:int = "庄严"    不会报错
"""
import json
import random

# 演示类型注解

# 基础数据类型注解
var_1:int = 1
var_2:str = "庄严"
var_3:bool = True

# 类对象类型注解
class Student:
    pass
stu:Student = Student()

# 基础容器类型注解
my_list:list = [1,2,3,4,5]
my_tuple:tuple = (1,2,3,4,5)
my_dict:dict = {"庄严":666}

# 容器类型详细注解
my_list_1:list[int] = [1,2,3,4,5]
my_tuple_1:tuple[int,str,bool] = (1,"庄严",True)
my_dict_1:dict[str,int] = {"庄严":666}

# 在注释中进行类型注解
a = random.randint(1,10)    # type:int
b = json.loads('{"<UNK>":666}')    # type:dict[str,int]
def func():
    return 10
var_4 = func()  # type:int

# 类型注解的限制
var_5:int = "庄严"   # 不会报错