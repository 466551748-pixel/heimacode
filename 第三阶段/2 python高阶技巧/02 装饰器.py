"""
 装饰器：
 装饰器其实也是一种包，其功能就是在不破坏目标函数原有代码和功能的前提下，为目标函数增加新功能
 装饰器就是使用创建一个闭包函数，在闭包函数内调用目标函数，可以达到在不改动目标函数的同时，增加额外功能

 注意：
 inner：代表这个函数本身
 inner():执行这个函数
"""
# 装饰器的一般写法(闭包)
# def outer(func):
#     def inner():
#         print("我睡觉了")
#         func()
#         print("我起床了")
#     return inner
# def sleep():
#     import random
#     import time
#     print("睡眠中.....")
#     time.sleep(random.randint(1,5))
#
# fn = outer(sleep)
# fn()

# 装饰器的快捷写法（语法糖）
def outer(func):
    def inner():
        print("我睡觉了")
        func()
        print("我起床了")
    return inner

@outer # 装饰器，本质上就是把sleep传入outer，返回了inner
def sleep():
    import random
    import time
    print("睡眠中.....")
    time.sleep(random.randint(1,5))

sleep()


