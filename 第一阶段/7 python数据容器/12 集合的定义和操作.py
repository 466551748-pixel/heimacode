"""
 为什么使用集合
 通过特性来分析，有什么局限呢？：
    列表可修改、支持重复元素且有序
    元组、字符串不可修改、支持重复元素且有序
 答：局限就在于，它们都支持重复元素
    如果场景需要对内容做重处理，列表、元组、字符串就不方便了
    而集合做主要的特点就是：不支持元素的重复，自带去重功能，且内部无序（无序不重复）

 总结：
    1.不允许重复数据存在
    2.数据是无序存储的（不支持下标索引）
    3.可以容纳多个数据
    4.可以容纳不同数据类型
    5.可以修改
    6.支持for循环
"""
# 定义集合和空集合
my_set = {"传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima"}
my_ste_empty = set()
print(f"my_set的内容是：{my_set}，类型是：{type(my_set)}")
print(f"my_set_empty的内容是：{my_ste_empty}，类型是：{type(my_ste_empty)}")

# 添加元素
my_set.add("python")
my_set.add("传智教育")
print(f"my_set添加元素后的结果是：{my_set}")

# 移除元素
my_set.remove("黑马程序员")
print(f"my_set移除黑马程序员后，结果是：{my_set}")

# 随机中集合中取出元素，因为集合不支持下标，所以pop相比列表，变成了随机取出
element = my_set.pop()
print(f"从my_set随机取出的元素是：{element}")
print(f"取出元素后剩余的集合为:{my_set}")

# 清空集合
my_set.clear()
print(f"集合被清空啦，结果是:{my_set}")

# 取出2个集合的差集（取出集合1有的，集合2没有的），语法： 集合1.difference(集合2)
# 结果：得到一个新的集合，原本的集合12不变
set1 = {1,2,3}
set2 = {1,5,9}
set3 = set1.difference(set2)
print(f"集合1和2的差集(集合1有的，集合2没有的)为：{set3}")

# 消除2个集合的差集（在集合1内，删除和集合2相同的元素），语法： 集合1.difference_update(集合2)
# 结果：集合1被修改，集合2不变
set1 = {1,2,3}
set2 = {1,2,9}
set1.difference_update(set2)
print(f"消除集合1和2的差集(在集合1内，删除和集合2相同的元素)为：{set1}")

# 合并(将集合1和集合2组合成新的集合)， 语法：集合1.union(集合2)
set1 = {1,2,3}
set2 = {1,5,9}
set3 = set1.union(set2)
print(f"集合1和集合2合并的结果是：{set3}")

# 统计集合元素的数量len()
set1 = {1,2,3,1,2,3}
num = len(set1)
print(f"集合内元素的数量有(注意去重)：{num}")

# 集合的遍历
# 注意集合不支持下标索引，不能用while循环
# 可以用for循环
my_set = {1,2,3,4,5,1}
for num in my_set:
    print(f"集合的元素有：{num}")



