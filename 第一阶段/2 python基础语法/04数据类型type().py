"""
 type()语句：用来的到数据的类型
 用法：type(被查看类型的数据)
"""
#第一种写法：查看字面量
print(type(111))
print(type("庄严"))
print(type(13.14))

#第二种写法：查看字面量
string_type = type("庄严")
int_type = type(11)
float_type = type(13.14)

print(string_type)
print(int_type)
print(float_type)

#第三种写法：查看变量中存储的数据类型
#注意：python中变量是没有类型的，变量中存储的是有类型的
#如字符串变量：表示变量中存储的是字符串类型
name = "庄严"
name_type = type(name)
print(name_type)