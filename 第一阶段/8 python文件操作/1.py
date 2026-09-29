f = open("/Users/zhuangyan/Desktop/未命名文件夹/x.txt",'r',encoding='utf-8')

b = 0

for line in f:
    print(type(line))
    b += line.count("itheima")
print(b)