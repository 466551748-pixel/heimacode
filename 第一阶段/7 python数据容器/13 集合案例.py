"""
 有一个列表
    1.定义一个空集合
    2.通过for循环遍历列表
    3.在for循环中将列表的元素添加到集合
    4.最终得到元素的集合对象，并打印输出
"""
my_list = ["黑马程序员","传智播客","黑马程序员","传智播客","itheima","itcast","itheima","itcast","best"]

# 定义一个空集合
my_set = set()

for num in my_list:
    print(f"遍历列表，其中的元素有：{num}")
    my_set.add(num)

print(f"集合：{my_set}")
for i in my_set:
    print(f"集合中的元素有：{i}")