# 定义一个列表
my_list = [21,25,21,23,22,20]

# 追加一个数字31
my_list.append(31)
print(my_list)

# 追加一个新列表
my_list.extend([29,33,30])
print(my_list)

# 取出第一个元素
element = my_list.pop(0)
print(element)

# 取出最后一个元素
element1 = my_list.pop(8)
print(element1)

# 查找元素31，在列表中的下标位置
print(my_list)
index = my_list.index(31)
print(index)