f = open("/Users/zhuangyan/Desktop/未命名文件夹/111.txt","r",encoding="utf-8")
g = open("/Users/zhuangyan/Desktop/未命名文件夹/bill1.txt","w",encoding="utf-8")

for line in f:
    if line.count("测试") == 1:
        continue
    else:
        g.write(line)

g.close()
f.close()
