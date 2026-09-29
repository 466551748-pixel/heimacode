"""
 字符串格式化快速写法：
    语法：f"内容{变量}"
    总之前面加个f，变量记得用{}框起来
    ：不限制数据类型，但也不作精度控制
"""
name = "庄严"
age = 23
phone_number = 13430799698
print(f"{name}今年{age}岁，电话是 {phone_number}")