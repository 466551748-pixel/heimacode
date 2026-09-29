f = open("/Users/zhuangyan/Desktop/未命名文件夹/x.txt",'r',encoding='utf-8')

lines = f.readlines()
line1 = []
b = 0
for line in lines:
    a = line.split( )
    line1.extend(a) # 元素取出一个一个放进去
    #line1.append(a) 这会导致嵌套列表，因为是把每行数据当成一个列表整个放进去
print(line1)
print(f"itheima出现的次数为：{line1.count('itheima')}")

"""
 #最便捷的方法
lines = f.read()
print(f"itheima出现的次数为：{lines.count('itheima')}")
"""
