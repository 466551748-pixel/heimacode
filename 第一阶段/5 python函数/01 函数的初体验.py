"""
 函数：是组织好的，可重复使用的，用来实现特定功能的代码段
 为什么要学习、使用函数呢？
    解答：为了得到一个针对特定需求，可供重复利用的代码段
         提高程序的复用性，减少重复性代码，提高开发效率
"""
from operator import length_hint

# 需求：统计字符串的长度，不使用内置函数len()
str1 = "intelligent"
str2 = "python"
length1 = 0 # 定义计数的变量
for i in str1:
    length1 += 1
print(length1)
length2 = 0 #定义计数的变量
for i in str2:
    length2 += 1
print(length2)

# 可以使用函数，来优化这个过程
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")
my_len(str1)