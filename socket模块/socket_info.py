#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

#########服务端##############

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket对象，面向连接的
server.bind(("127.0.0.1", 9999))  # 绑定主机名和端口号
server.listen(10)  # 设置最大连接数，超过后排队
clientsock, addr = server.accept()  # 建立与客户端的连接，返回(socket object, address info)元组对象
print("addr=%s %s" % (addr, type(addr)))
print("客户端ip地址为：%s  端口号为：%s" % addr)
clientsock.send("欢迎来到服务端".encode('utf-8'))  # python3要求发送byte型的数据，所以我们将它以utf-8的形式转换为bytes类型的
msg = clientsock.recv(1024)  # 接收客户端发来的消息,msg2为bytes类型的数据
print(msg.decode('utf-8'))  # 我们将bytes类型数据转换成str字符型的数据，以utf-8的形式
clientsock.close()


#########客户端##############

# import socket
#
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(("127.0.0.1", 9999))  # connect函数接收元组型数据
# msg = client.recv(1024)  # 接收从服务器发来的消息，为bytes类型的数据，大小为1024字节的缓冲区
# print(msg.decode('utf-8'))  # 我们转化为str字符串类型的数据，以utf-8的形式
# client.send("客户端到此一游".encode('utf-8'))  # python3要求发送bytes类型的数据，所以我们得将它转换
# client.close()


##########socket中的一些常用方法#####################

# import socket
# a=socket.gethostname()     #获得本机的主机名，返回str型数据
# print(a,type(a))
# b=socket.gethostbyname(a)  #根据主机名获取ip地址，返回str型数据，也可以是网络上的域名
# print(b,type(b))
# c=socket.gethostbyaddr(b)  #通过ip获得该主机的一些信息，返回tuple元组型数据
# print(c,type(c))
# #############################################
# Win-10 <class 'str'>
# 192.168.56.1 <class 'str'>
# ('bogon', [], ['192.168.56.1']) <class 'tuple'>
