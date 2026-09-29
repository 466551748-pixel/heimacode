"""
 数据容器的通用操作：数据容器尽管各自有各自的特点，但是它们也有一些通用的操作
    一.遍历
        1.5类容器都支持for循环遍历
        2.列表、元组、字符串支持while循环，而集合、字典不支持while循环（无法下标索引）
    二.统计容器的元素个数
        语法：len(容器)
    三.统计容器的最大元素
        语法：max(容器)
    四.统计容器的最小元素
        语法：min(容器)
 数据容器的通用转换功能
    一.将给定容器转换成列表
        语法：list(容器)
    二.将给定容器转换成元组
        语法：tuple(容器)
    三.将给定容器转换成字符串
        语法：str(容器)
    四.将给定的容器转换成集合
        语法：set(容器)
 容器通用排序功能
    语法：sorted(容器,reverse=False)
         reverse默认为False为正序（从小到大）
         reverse若是True表示逆序（从大到小）
    注意：排序完的结果会通通变成列表对象

"""

my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_str = "abcdefg"
my_set = {1,2,3,4,5}
my_dict = {"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}


# max()最大元素
print(f"列表\t\t最大元素是：{max(my_list)}")
print(f"元组\t\t最大元素是：{max(my_tuple)}")
print(f"字符串\t最大元素是：{max(my_str)}")
print(f"集合\t\t最大元素是：{max(my_set)}")
print(f"字典\t\t最大元素是：{max(my_dict)}")
print()
# min()最小元素
print(f"列表\t\t最小元素是：{min(my_list)}")
print(f"元组\t\t最小元素是：{min(my_tuple)}")
print(f"字符串\t最小元素是：{min(my_str)}")
print(f"集合\t\t最小元素是：{min(my_set)}")
print(f"字典\t\t最小元素是：{min(my_dict)}")
print()

# 类型转换：容器转列表
print(f"列表\t\t转列表的结果是：{list(my_list)}")
print(f"元组\t\t转列表的结果是：{list(my_tuple)}")
print(f"字符串\t转列表的结果是：{list(my_str)}")
print(f"集合\t\t转列表的结果是：{list(my_set)}")
print(f"字典\t\t转列表的结果是：{list(my_dict)}，value被舍弃掉")  # value被舍弃掉
print()
# 类型转换：容器转元组
print(f"列表\t\t转元组的结果是：{tuple(my_list)}")
print(f"元组\t\t转元组的结果是：{tuple(my_tuple)}")
print(f"字符串\t转元组的结果是：{tuple(my_str)}")
print(f"集合\t\t转元组的结果是：{tuple(my_set)}")
print(f"字典\t\t转元组的结果是：{tuple(my_dict)}，value被舍弃掉")
print()
# 类型转换：容器转字符串
print("注意：省略了双引号")
print(f"列表\t\t转字符串的结果是：{str(my_list)}")
print(f"元组\t\t转字符串的结果是：{str(my_tuple)}")
print(f"字符串\t转字符串的结果是：{str(my_str)}")
print(f"集合\t\t转字符串的结果是：{str(my_set)}")
print(f"字典\t\t转字符串的结果是：{str(my_dict)}")
print()
# 类型转换：容器转集合
print(f"列表\t\t转集合的结果是：{set(my_list)}")
print(f"元组\t\t转集合的结果是：{set(my_tuple)}")
print(f"字符串\t转集合的结果是：{set(my_str)}，集合无序，数字有序是因为底层哈希排序")
print(f"集合\t\t转集合的结果是：{set(my_set)}")
print(f"字典\t\t转集合的结果是：{set(my_dict)},舍去了value值")
print()
# 进行容器的排序
my_list = [3,1,2,5,4]
my_tuple = (3,1,2,5,4)
my_str = "bdcefga"
my_set = {3,1,2,5,4}
my_dict = {"key3":1,"key1":2,"key2":3,"key5":4,"key4":5}
print(f"列表\t\t排序的结果是：{sorted(my_list)}")
print(f"元组\t\t排序的结果是：{sorted(my_tuple)}")
print(f"字符串\t排序的结果是：{sorted(my_str)}")
print(f"集合\t\t排序的结果是：{sorted(my_set)}")
print(f"字典\t\t排序的结果是：{sorted(my_dict)}")

print(f"列表\t\t反向排序的结果是：{sorted(my_list,reverse = True)}")
print(f"元组\t\t反向排序的结果是：{sorted(my_tuple,reverse = True)}")
print(f"字符串\t反向排序的结果是：{sorted(my_str,reverse = True)}")
print(f"集合\t\t反向排序的结果是：{sorted(my_set,reverse = True)}")
print(f"字典\t\t反向排序的结果是：{sorted(my_dict,reverse = True)}")
