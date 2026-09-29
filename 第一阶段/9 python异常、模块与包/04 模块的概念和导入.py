"""
 什么是模块？
 答：python模块，是一个python文件，以.py结尾，模块能定义函数，类和变量，模块里也可以包含可执行的代码

 模块的作用：可以直接导入过来使用模块内定义好的函数，类和变量（import），也就是工具包

 导入方式：
 from 模块名 import 模块，类，变量，函数，*（*代表导入模块的所有内容） as 别名

 基本语法：
 import 模块名
 import 模块名1,模块名2

 模块名.功能名()
"""

# 使用import导入time模块使用sleep功能函数
# import time  # 导入python内置的time模块（time.py这个文件）
# print("你好")
# time.sleep(5)
# print("我好")

# 运用from导入time的sleep功能函数（针对某一个功能去使用）
# from time import sleep
# print("你好")
# sleep(5)
# print("我好")

# 使用 * 导入time模块的全部功能
# from time import *
# print("你好")
# sleep(5)
# print("我好")

# 使用as给特定功能（名字可能很长,用起来不方便）改名字（别名）
import time as t
print("你好")
t.sleep(5)
print("我好")


