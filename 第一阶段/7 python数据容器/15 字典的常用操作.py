"""
 字典的常用操作
    1.新增元素：
        语法：字典[key] = value
        结果：字典被修改，新增元素
    2.更新元素：
        语法：字典[key] = value
        结果：字典被修改，元素被更新
        注意：语法和新增元素一样，字典的key不可以重复，所以区别在对已存在的key执行，就是更新元素
    3.删除元素
        语法：字典.pop(key)
        结果：获得字典key的value，同时字典被修改，
    4.获取全部的key
        语法；字典.keys()
        结果：得到字典中的全部key
 总结：
    1.每一份数据都是键值对
    2.可以通过key获取到value，key不可重复
    3.可以容纳多个数据
    4.可以容纳不同类型的数据
    5.不支持下标索引
    6.支持修改（增加或删除更新元素等）
    7.支持for循环，不支持while循环

"""
my_dict = {"王力宏":99,"周杰伦":88,"林俊杰":77}
# 新增元素
my_dict["张信哲"] = 66
print(f"字典经过新增元素后，结果是：{my_dict}")

# 更新元素
my_dict["周杰伦"] = 33
print(f"字典经过更新元素后，结果是：{my_dict}")

# 删除元素
score = my_dict.pop("周杰伦")
print(f"字典中被移除了一个元素，结果是：{my_dict}，周杰伦的考试分数是：{score}")
# 清空元素

my_dict.clear()
print(f"字典被清空了，内容是{my_dict}")
# 获取全部的key

my_dict = {"王力宏":99,"周杰伦":88,"林俊杰":77}
keys = my_dict.keys()
print(f"字典的全部keys是：{keys}")

# 遍历字典，字典不支持下标索引，不支持while循环
# 方式1:通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是{my_dict[key]}")
# 方式2:直接对字典进行for循环，每一次循环都是直接得到key
for key in my_dict:
    print(f"2字典的key是：{key}")
    print(f"2字典的value是：{my_dict[key]}")

# 统计字典内的元素数量，len()函数
num = len(my_dict)
print(f"字典的元素数量是：{num}")

