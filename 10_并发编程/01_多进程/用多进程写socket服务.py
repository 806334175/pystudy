#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 上午11:35
# @Author  : Ryu
# @Site    : 
# @File    : 用多进程写socket服务.py
# @Software: PyCharm


import socket
from multiprocessing import Process

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 1111))
server.listen(10)


def talk(conn, client_addr):
    while True:
        res = conn.recv(1024)
        if not res: break
        print(res)


if __name__ == '__main__':
    while True:
        conn, client_addr = server.accept()
        p = Process(target=talk, args=(conn, client_addr,))
        p.start()




# from socket import *
#
# client=socket(AF_INET,SOCK_STREAM)
# client.connect(('127.0.0.1',8080))
#
#
# while True:
#     msg=input('>>: ').strip()
#     if not msg:continue
#
#     client.send(msg.encode('utf-8'))
#     msg=client.recv(1024)
#     print(msg.decode('utf-8'))
#
# 多个client端


# 每来一个客户端，都在服务端开启一个进程，如果并发来一个万个客户端，要开启一万个进程吗，你自己尝试着在你自己的机器上开启一万个，10
# 万个进程试一试。
# 解决方法：08_进程池
