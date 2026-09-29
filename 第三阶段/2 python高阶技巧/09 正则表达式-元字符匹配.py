"""
 单字符匹配
 .    匹配任意一个字符（除了\n）,注意：\.匹配的是.本身
 []   匹配[]中列举的字符,[]内可以写[a-zA-Z0-9]三种范围组合（[a-c],[A-J],[3-6]都行）或者指定单个字符[aBcDFC123]
 \d   匹配数字，即0-9
 \D   匹配非数字
 \s   匹配空白，即空格、tab键
 \S   匹配非空白
 \w   匹配单词字符，即a-z、A-Z、0-9
 \W   匹配非单词字符

 数量匹配
 *     匹配前一个规则的字符出现0至无数次
 +     匹配前一个规则的字符出现1至无数次
 ?     匹配前一个规则的字符出现0次或1次
 {m}   匹配前一个规则的字符出现m次
 {m,}  匹配前一个规则的字符出现最少m次
 {m,n} 匹配前一个规则的字符出现m到n次

 边界匹配
 ^     匹配字符串开头
 $     匹配字符串结尾
 \b    匹配一个单词的边界
 \B    匹配非单词边界

 分组匹配
 |     匹配左右任意一个表达式
 ()    将括号中的字符作为一个分组
"""
# 演示正则表达式使用元字符匹配
import re

s = "zhuangyan @@11189 zhuangyue12"
# 匹配所以数字
result = re.findall("\d",s)
print(result)
print()
# 匹配特殊字符
result = re.findall("\W",s)
print(result)
print()
# 匹配所以英文字母,注意：不能用\w，会把数字也匹配上，用[]
result = re.findall("[a-zA-Z]",s)
print(result)
print()
# 匹配账号，只能由字母和数字组成，长度限制在6-10位
rule = "^[a-zA-Z0-9]{6,10}$"
str = "123saddd"
result = re.findall(rule,str)
print(result)
print()
# 匹配qq号，要求纯数字，长度5-11，第一位不为0
rule = "^[1-9]{1}\d{4,10}$"
str = "2133232"
result = re.findall(rule,str)
print(result)
# 匹配邮箱地址，只允许qq、163、gmail这三种邮箱地址
# rule = "^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$"
rule = r"(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)"     # 字符串前面加r，表示字符串内的转义字符\无效，当作普通字符
str = "a.v.c.s.s@qq.com.s.d"
result = re.findall(rule,str)       # findall方法若匹配规则里有()，会把每个()里面匹配的返回给你，所以要在外面再加一个()
print(result)
# 或者使用match，防止括号
result1 = re.match(rule,str)
print(result1.group())