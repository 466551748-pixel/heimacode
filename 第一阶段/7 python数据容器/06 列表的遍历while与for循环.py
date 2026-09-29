"""
 既然数据容器里面可以包含多个元素，那么，就会有需求从容器内依次取出元素进行操作
 将容器内的元素依次取出进行处理的行为，称之为：遍历，迭代

 如何遍历列表的元素呢？
    使用while循环或者for循环
 如何在循环中取出列表的元素呢？
    使用列表[下标]的方式取出
 循环的条件如何去控制呢？
    定义一个变量表示下标，从0开始
    循环条件为 下标值<列表的元素数量
    index = 0
    while index < len(my_list):
        元素 = my_list[index]
        对元素进行处理
        index += 1
"""



# 演示对list列表的循环，使用while和for循环俩种方式
# while
def list_while_func():
    my_list = ["庄严","很帅","超级帅"]
    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(f"列表的元素：{element}")
        index += 1
list_while_func()
print()
# for循环
def list_while_func2():
    my_list = [1,2,3,4,5]
    for i in my_list:
        print(f"列表的元素有：{i}")
list_while_func2()

"""
 总结：
    在循环控制上：
        1.while循环可以自定循环条件，并自行控制
        2.for循环不可以自定循环条件，只可以一个个从容器取出数据
    在无限循环上：
        1.while循环可以通过条件控制做到无限循环
        2.for循环理论上不可以，因为被遍历的容器容量不是无限的
    在使用场景上
        1.while循环适用于任何想要循环的场景
        2.for循环适用于，遍历数据容器的场景或简单的固定次数循环场景
"""
"""
 练习：定义一个列表，内容是[1,2,3,4,5,6,7,8,9,10]
    1.遍历列表，取出列表内的偶数，并存入一个新的列表对象中
    2.使用while循环和for循环各操作一次
"""
# while
mylist = [1,2,3,4,5,6,7,8,9,10]
def list_while_odd(data):
    my_list = []
    index = 0
    while index < len(data):
        element = data[index]
        if element % 2 == 0:
            my_list.append(element)
        index += 1
    print(f"新列表为：{my_list}")
list_while_odd(mylist)
# for
def list_for_odd(data):
    my_list = []
    index = 0
    for element in data:
        if element % 2 == 0:
            my_list.append(element)
    index += 1
    print(f"新列表为：{my_list}")
list_for_odd(mylist)

