"""
 文件的操作步骤
  一.打开文件
  open(name,mode,buffering,encoding)
  name：要打开的目标文件名的字符串（或者文件所在的具体路径）注意：只给文件名的话代表找的是和python同一层的文件的名字
  mode：设置打开文件的模式（访问模式）
        1.只读r
        2.写入w：打开个文件进行写入，如果该文件已存在，则打开文件从头开始编辑，原有内容会被删除
                如果文件不存在，创建新文件
        3.追加a：如果该文件已存在，新的内容会被写入到已有内容之后
                如果该文件不存在，创建新文件
  encoding：编码格式（推荐utf-8）
  示例代码：
  f = open('python.txt','r',encoding='UTF-8')
  注意：1.f是返回的文件对象，python进行了包装，里面包含着操作系统学过的文件描述符，
       所以可以直接对其进行操作
       2.为什么encoding='UTF-8'直接用的是关键字参数而不是位置参数？
         答：因为还open函数第三位是buffering，是控制缓冲区大小和行为的，
            若不用关键字参数，第三位会被buffering接收导致错误

 二.读写文件
 1.read()
    文件对象.read(num)
 num:表示要从文件中读取数据的长度（单位是字节），如果没有传入num，代表读取文件所有的数据
 2.readlines()
 按照行的方式把整个文件中的内容一次性进行读取，并且返回的是一个列表，其中每一行元素的数据为一个元素
 3.readline()
 一次读取一行内容，用一次读一行，用一次读一行

 三.文件的关闭
    文件对象.close()
 为什么需要关闭？ 因为open了文件，文件会被python程序一直占用，需要close释放文件

"""
# 打开文件
f = open('/Users/zhuangyan/Desktop/未命名文件夹/x.txt','r',encoding='UTF-8')
print(type(f))

# 读取文件 read() 注意：连续俩个read方法，是会接着第一个没读完的继续读取的
print(f"read方法读取10字节的结果是：{f.read(3)}")
print(f"read方法读取全部的结果是：{f.read()}")

# 读取文件 readlines() 读取文件的全部行，封装到列表中
lines = f.readlines()
print(f"lines对象的类型：{type(lines)}")
print(f"lines对象的内容是{lines}")       # 注意：这里为什么为空？ 因为3435行代码导致读取文件指针已经到了最后，如果想要有结果，必须注释掉3435行代码

# 读取文件 readline()
line1 = f.readline()
line2 = f.readline()
print(f"第一行的数据是：{line1}")
print(f"第二行的数据是：{line2}") # 这里会空也是文件指针到最后的问题

# for循环读取文件行
for line in f:
    print(f"每一行的数据是：{line}")

# 文件的关闭
#f.close()

# with open 语法操作文件
with open('python.txt','w',encoding='UTF-8') as f:
    for line in f:
        print(f"每一行的数据是：{line}")
# 这种写法可以避免忘记close文件，它执行完with open内的代码会自动close文件
