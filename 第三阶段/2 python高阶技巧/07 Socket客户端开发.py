"""
 演示socket客户端开发

 connect就是客户端，需要链接服务端
"""
import socket

# 创建socket对象
socket_client = socket.socket()

# 连接到服务端
socket_client.connect(("localhost",8888))

while True:
    msg = input("请输入你要给服务器发的消息：\n")
    if msg == "exit":
        break
    # 发送消息
    socket_client.send(msg.encode("utf8"))
    # 接受返回消息
    recv_data = socket_client.recv(1024)   # 1024缓冲区大小 recv阻塞方式
    print(f"服务端回复的消息是：{recv_data.decode("utf8")}")
# 关闭链接
socket_client.close()