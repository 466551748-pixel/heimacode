"""
 思考：如果函数没有使用return语句返回数据，那么函数有返回值吗？
    解答：有的，python中有一个特殊的字面量 None
         无返回值的函数，实际上就是返回了 None 这个字面量
 None表示：空的，无实际意义的意思
 函数返回的None，也就是表示：这个函数没有返回什么有意义的内容，也就是返回了空的意思
 在if判断中，None就是False
"""
# 无return语句的函数返回值
def say_hi():
    print("你好啊")
result = say_hi()
print(f"无返回值函数，返回的内容是:{result}")
print(f"无返回值函数，返回的类型是:{type(result)}")

#主动返回None的函数
def say_hi2():
    print("你好啊")
    return None
print(f"主动返回None函数，返回的内容是:{result}")
print(f"主动返回None函数，返回的类型是:{type(result)}")

# None用于if判断
def check_age(age):
    if age >= 18:
        return "SUCCESS"
    else:
        return None
result = check_age(12)
if not result:
    # 进入if保湿result是None，也就是False
    print("未成年，不准进入")

# None用于声明无初始内容的变量
name = None