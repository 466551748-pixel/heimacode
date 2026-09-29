"""
 import threading

 thread_obj = threading.Thread(group,target,name,args,kwargs)
 # group:暂时没用，未来功能的预留参数
 # target:执行的目标任务函数
 # args:以元组方式给执行任务传参数
 # kwargs:以字典方式给执行任务传参数
 # name:线程名，一般不需要设置

 # 启动线程，让线程开始工作
 thread_obj.start()
"""
import time
import threading

# 演示多线程的使用

def Sing(mag):
    while True:
        print(mag)
        time.sleep(1)

def Dance(mag):
    while True:
        print(mag)
        time.sleep(1)

sing = threading.Thread(target=Sing,args=("我在唱歌",))
dance = threading.Thread(target=Dance,args=("我在跳舞",))
sing.start()
dance.start()