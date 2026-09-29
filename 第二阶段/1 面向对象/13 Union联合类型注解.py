"""
 为什么使用Union类型？
 答：混合过多的类型，普通办法写不完

 Union联合类型：里面有可能有这个有可能有那个
"""

# 演示Union联合类型注解
from typing import Union

my_list:list[Union[int,str]] = [1,2,"庄严","庄粤"]

def func(data:Union[int,str]) -> Union[str,int]:
    pass
func()