my_str = "itheima itcast boxuegu"
# 统计有多少个it
count = my_str.count("it")
print(f"总共有{count}个it")
# 将字符串内的空格全部替换为字符|
my_str = my_str.replace(" ", "|")
print(f"替换后的字符串为：{my_str}")
# 按照“|”进行字符串的分割，得到列表
my_str_list = my_str.split("|")
print(f"分割后的列表为：{my_str_list}")
