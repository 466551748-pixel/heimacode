"""
 正则表达式：规则的定义
 又称规则表达式（regular expression），是使用单个字符串来描述、匹配某个句法规则的字符串，常被用来检索、替换那些符合某个模式（规则）的文本
 简单来说，正则表达式就是使用：字符串定义规则，并通过规则去验证字符串是否匹配
 比如，验证一个字符串是否符合条件的电子邮箱地址，只需要配置好正则规则，即可匹配任意邮箱。
 如果不使用正则，使用if else就非常困难麻烦

 语法：match，search，findall
 1.re.match(匹配规则,被匹配字符串)
 从被匹配字符串的开头进行匹配（开头不匹配，后面都不管，一开始就要符合），匹配成功返回匹配对象（包含匹配的信息），匹配不成功返回None

 2.re.search(匹配规则,被匹配字符串)
 搜索整个字符串，找出匹配的。从前向后，找到第一个后，就停止，不会继续向后

 3.re.findall(匹配规则,匹配字符串)
 匹配整个字符串，找出全部匹配项，找不到返回空list -> []
"""
import re

s = "python itheima"
# match 从头匹配
result = re.search("python",s)
print(result)
print(result.span())   # 匹配成功的下标范围
print(result.group())  # 匹配成功的值是什么

print()
# search
s = "1python itheima python"
result = re.search("python",s)
print(result)
print(result.span())   # 匹配成功的下标范围
print(result.group())  # 匹配成功的值是什么

print()


# findall
result = re.findall("python",s)
print(result)