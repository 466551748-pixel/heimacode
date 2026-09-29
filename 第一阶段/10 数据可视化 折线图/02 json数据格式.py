"""
 什么是json？
 1.json是一种轻量级的数据交互格式，可以按照json指定的格式去组织和封装数据
 2.json本质上是一个带有特定格式的字符串
 主要的功能：json就是一种在各个编程语言中流通的数据格式，负责不同编程语言中的数据传递和交互，类似于
 1.国际通用语言->英语
 2.中国不同地区通用语言->普通话

 json有什么用？  ：不同语言的中转站
 python中有字典dict这样的数据类型，而其他语言可能没有
 python格式数据-->json格式数据-->c语言格式数据
 ：c语言程序接收json格式数据并且转化为c格式数据继续使用
"""
# 演示json数据和python字典的相互转换
import json
# 准备列表，列表内的每个元素都是字典，将其转换为json
data = [{"name":"张大山","age":11},{"name":"王大锤","age":13},{"name":"赵小虎","age":16},]
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)
# 准备字典，将字典转化为json
d = {"name":"周杰伦","addr":"台北"}
json_str = json.dumps(d,ensure_ascii=False)
print(type(json_str))
print(json_str)

# 将json字符串转化为python数据类型 列表
s = '[{"name":"张大山","age":11},{"name":"王大锤","age":13},{"name":"赵小虎","age":16}]'
l = json.loads(s)
print(type(l))
print(l)

# 将json字符串转化为python数据类型 字典
s = '{"name":"周杰伦","addr":"台北"}'
l = json.loads(s)
print(type(l))
print(l)