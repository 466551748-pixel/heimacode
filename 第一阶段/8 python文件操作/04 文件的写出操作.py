"""
 写操作快速过程
 一.打开文件
    f = open()
 二.文件写入
    f.write("")
 三.内容刷新
    f.flush()
 这一步是为了写会外存，因为f.write是写到了程序的缓冲区中，为了避免频繁的操作磁盘（磁盘操作速度慢）
 最后才用f.flush写回外存
"""
# 打开文件，不存在的文件,w模式会自动创建
f = open("/Users/zhuangyan/Desktop/未命名文件夹/111.txt","w",encoding="utf-8")
# write写入
f.write("hello world")
# f.flush()刷新，写回外存,f.close()也可以达到目标
f.flush()