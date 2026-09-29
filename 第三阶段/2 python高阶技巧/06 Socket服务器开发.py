"""
 Socket:
 套接字，是进程之间通信的一个工具我，进程之间想要进行网络通信需要Socket
 类似于进程之间网络数据传输的搬运工

 你代码里有 bind() + listen() + accept() 这三件套，这就是服务端的"身份证"。客户端只有 connect()。
 证明我是服务端
"""
# 演示Socket服务端开发
import socket

# 创建Socket对象
socket_server = socket.socket()

# 指定ip地址和端口
socket_server.bind(("localhost",8888))
# 监听端口
socket_server.listen(1)
# listen方法内接受一个整数传参数，表示接受的链接数量
# 等待客户端链接
result = socket_server.accept() # 返回二元元组
conn = result[0]                # 客户端和服务端的链接对象 一条具体通话的电话线
address = result[1]             # 客户端的地址信息
# 或者 conn,address = socket_server.accept()
# 可以通过 变量1,变量2 = socket_server.accept() 的形式，直接接收二元元组内的俩个元素
# accept方法是阻塞的方法，等待客户端的链接，如果没有链接，就卡在这，不向下运行
print(f"接受到了客户端的链接，客户端的信息是:{address}")
while True:
    # 接受客户端的信息，要使用客户端和服务器的本次链接对象（conn），而非socket_server对象
    data = conn.recv(1024).decode("utf-8")
    # recv也是阻塞
    # recv接受的参数是缓冲区大小，一般1024，返回值是一个字节数组，也就是bytes对象，不是字符串，通过decode方法通过utf-8编码，转为字符串对象
    print(f"客户端发来的消息:{data}")
    # 发送回复消息
    msg = input("输入你给客户端回复的消息：\n")
    if msg == "exit":
        break
    conn.send(msg.encode("utf-8"))  # encode可以将utf-8编码为字节数组对象

# 关闭链接
conn.close()
socket_server.close()
