"""
 自定义工具包my_utils
"""

import my_utils.file_util as file
import my_utils.str_util as string


# 测试str_util内俩个函数功能
str = "123456"
string.str_reverse(str)
string.substr(str,1,5)

# 测试file_util内俩函数功能

file.print_file_info("/Users/zhuangyan/Desktop/未命名文件夹/1.txt")
file.append_file_info("/Users/zhuangyan/Desktop/未命名文件夹/111.txt","aaaaaaaaab")