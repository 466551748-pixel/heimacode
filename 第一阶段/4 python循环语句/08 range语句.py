"""
 for语句中的待处理数据集，严格来说，称为： 序列类型
 序列类型：指其内容可以一个个依次取出的一种类型
        例如：字符串、列表、元组..等
 range的语法：
    1.range(num)：获取一个从0开始到num(不包括num)结束的数字序列
        range(5)得到01234
    2.range(num1,num2)：获取一个从num1到num2(不包括num2)结束的数字序列
    3.range(num1,num2,step)：
        获取一个从num1到num2(不包括num2)结束的数字序列，但可以通过step设置步长
    4.快速控制次数
"""
# 语法1
for i in range(10):
    print(i,end=' ')
print() # 换行
# 语法2
for i in range(5,10):
    print(i,end=' ')
print()
# 语法3
for i in range(5,10,2):
    print(i,end=' ')
print()
# 快速控制次数
for i in range(5):
    print("庄严大帅哥",end=' ')