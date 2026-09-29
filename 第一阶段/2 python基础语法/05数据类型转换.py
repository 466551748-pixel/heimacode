"""
 int(x)：将x转为整数
 float(x)：将x转为浮点数
 str(x)：将x转为字符串
 同type()一样，这三个语句是带有结果的，可以直接print输出
"""
# 为什么要数据类型转换？：如从文件中读取的数字，默认是字符串，需要转换为数字类型

# 将数字类型转为字符串
num_str = str(11)
print(type(num_str),num_str)# 不会破坏内容

num_float = str(13.14)
print(type(num_float),num_float)
# 将字符串转为数字
num = int("11")
print(type(num),num)
num2 = float("13.14")
print(type(num2),num2)

# num3 = int("庄严")# 错误事例
# 万物都可以转字符串，字符串不一定能转数字（双引号里要是数字）
# print(type(num3),num3)

#浮点数转整数会丢失精度（保留整数）
int_num = int(11.33)
print(type(int_num),int_num)