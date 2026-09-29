"""
 print(*objects, sep=' ', end='\n')
    *objects：打印对象
    sep=' '：控制多个对象之间用什么隔开
    end='\n'：控制打印结束加什么，默认换行符，所以会自动换行
 print语句会自动换行
 让print语句不自动换行的方法：默认的end='\n'换行符改成空格，就不会换行了
    print("hello",end=" ")
    print("world",end=" ")
    只需要在后面加  ,end" "
"""
print("hello",end=" ")
print("world",end=" ")

print("hello world")
print("itheima best")
# \t：（制表符）用于对齐文本，让输出更整洁
print("hello\tworld")
print("itheima\tbest")
i = 1
while i < 10:
    j = 1
    while j <= i:
        print(f"{j}*{i}={j*i}\t",end=" ")
        j += 1
    i += 1
    print() # print()空内容，就是输出一个换行
    # 因为没有对象，但是end="\n"是默认执行的，所以print()会有换行的作用

