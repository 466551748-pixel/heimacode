"""
 字符串"万过薪月，员序程马黑来，nohtyp学"
 使用学过的方式，取出“黑马程序员”
"""
my_str = "万过薪月，员序程马黑来，nohtyp学"
my_str1 = my_str.strip("万过薪月，")
my_str2 = my_str1.strip("来，nohtyp学")
my_str3 = my_str2[::-1]
print(f"结果是:{my_str3}")