# 给函数添加说明文档，利用多行注释，辅助他人理解函数的作用
# 语法如下：
"""
函数说明
:param a: 形式参数x的说明
:param b: 形式参数y的说明
:return: 返回值的说明
"""

def add(a,b):
    """
    add函数可以接收2个参数，进行俩数相加的功能
    :param a: 形参a表示相加的其中一个数字
    :param b: 形参y表示相加的另一个数字
    :return: 返回值是2数相加的结果
    """
    result = a+b
    print(f"2数相加的结果是：{result}")
    return result

add(1,2)

