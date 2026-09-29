


"""
 列表提供了一系列功能（方法）：内置了一些方法供使用
    插入、删除、清空、修改、统计等
 回忆：函数是一个封装的代码单元，可以提供特定功能
    在python中，如果将函数定义为class（类）的成员，那么函数会称之为：方法
    函数和方法功能是一样的，只是写的地方不一样，使用的格式不同
    函数的使用：num = add(1,2)

    class Student():
        def add(self,a,b):
            return a+b
    方法的使用：通过一个.使用类里的方法（函数）
    student = Student()
    num = student.add(1,2)
 列表总结：
    1.可以容纳多个元素，上线为2**63-1
    2.可以容纳不同类型的元素（混装）
    3.数据是有序存储的（有下标序号）
    4.允许重复数据存在
    5.可以修改
"""
"""
 一.列表的查询功能（方法）
    功能：查找指定元素在列表的下标，如果找不到，报错
    语法： 列表.index(元素)
"""
mylist = [1,2,3,4,5,6,7,8,9]
index = mylist.index(5)
print(f"5在列表的下标索引是{index}")
print(f"原本的列表：\t\t\t\t\t\t{mylist}")

"""
 二.列表的修改功能：
    1.修改指定下标语法：列表[下标] = 值
    使用语法直接对指定下标（正向反向都行）的值进行重新赋值（修改）
    2.插入语法：列表.insert(下标,元素)
    在指定下标位置，插入指定元素
    3.追加单个语法：列表.append(元素)
    将指定元素，追加到列表的尾部
    4.追加多个语法：列表.extend(其他的数据容器)
    将其他数据容器的内容取出，依次追加到列表尾部
    5.删除元素语法1: del 列表[下标]
    指定下标元素删除
    6.删除元素语法2: 列表.pop(下标)
    指定下标元素删除,还可以有指定删除元素的返回值，供得到
    7.删除匹配元素语法：列表.remove(元素)
    删除某元素在列表中的第一个匹配项
    8.清空列表语法：列表.clear()
    9.统计元素语法：列表.count(元素)
    统计某元素在列表内的数量
    10.统计列表内有多少元素语法：len(列表)
"""
# 1修改
mylist[0] = "庄严"
print(f"列表（下标0）被修改后，结果为：\t\t{mylist}")

# 2插入
mylist.insert(1,"大帅哥")
print(f"列表继续（下标1）被插入后，结果为：\t{mylist}")

# 3追加单个元素
mylist.append("超级帅")
print(f"列表继续尾部追加单个元素后，结果为：\t{mylist}")

# 4追加多个元素
mylist.extend([10,11,12])
print(f"列表继续尾部追加多个元素，结果为：\t{mylist}")
print("注意这里是取出extend内数据容器内容，再依次追加到原列表的尾部")

# 5删除1
del mylist[0]
print(f"列表删除（下标0）后，结果为：\t\t{mylist}")

# 6删除2
element = mylist.pop(0)
print(f"列表再次删除（下标0），结果为：\t\t{mylist}，取出元素是：{element}")

# 7删除第一个匹配元素
mylist.remove("超级帅")
print(f"删除列表的第一个匹配元素后，结果为：\t{mylist}")

# 8清空列表
mylist.clear()
print(f"列表被清空了，结果是：\t\t\t\t{mylist}")

# 9统计元素
mylist1 = [1,1,1,6,"zhuang"]
print(f"以下使用的新列表是mylist1：\t\t{mylist1}")
count = mylist1.count("zhuang")
print(f"列表中\"zhuang\"的数量是：\t\t\t\t\t{count}")


# 10统计列表中的元素个数
length = len(mylist1)
print(f"列表mylist1的总元素个数是：\t\t{length}")

