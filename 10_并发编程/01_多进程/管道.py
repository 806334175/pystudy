#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 上午11:26
# @Author  : Ryu
# @Site    : 
# @File    : 管道.py
# @Software: PyCharm


# 创建管道的类：
# Pipe([duplex]): 在进程之间创建一条管道，并返回元组（conn1, conn2）, 其中conn1，conn2表示管道两端的连接对象，强调一点：必须在产生Process对象之前产生管道
# # 参数介绍：
# dumplex: 默认管道是全双工的，如果将duplex射成False，conn1只能用于接收，conn2只能用于发送。
# # 主要方法：
# conn1.recv(): 接收conn2.send(obj)
# 发送的对象。如果没有消息可接收，recv方法会一直阻塞。如果连接的另外一端已经关闭，那么recv方法会抛出EOFError。
# conn1.send(obj): 通过连接发送对象。obj是与序列化兼容的任意对象
# # 其他方法：
# conn1.close(): 关闭连接。如果conn1被垃圾回收，将自动调用此方法
# conn1.fileno(): 返回连接使用的整数文件描述符
# conn1.poll([timeout]): 如果连接上的数据可用，返回True。timeout指定等待的最长时限。如果省略此参数，方法将立即返回结果。如果将timeout射成None，操作将无限期地等待数据到达。
#
# conn1.recv_bytes([maxlength]): 接收c.send_bytes()
# 方法发送的一条完整的字节消息。maxlength指定要接收的最大字节数。如果进入的消息，超过了这个最大值，将引发IOError异常，并且在连接上无法进行进一步读取。如果连接的另外一端已经关闭，再也不存在任何数据，将引发EOFError异常。
# conn.send_bytes(buffer[, offset[,
#                 size]])：通过连接发送字节数据缓冲区，buffer是支持缓冲区接口的任意对象，offset是缓冲区中的字节偏移量，而size是要发送字节数。结果数据以单条消息的形式发出，然后调用c.recv_bytes()
# 函数进行接收
#
# conn1.recv_bytes_into(buffer[,
#                       offset]):接收一条完整的字节消息，并把它保存在buffer对象中，该对象支持可写入的缓冲区接口（即bytearray对象或类似的对象）。offset指定缓冲区中放置消息处的字节位移。返回值是收到的字节数。如果消息长度大于可用的缓冲区空间，将引发BufferTooShort异常。


# from multiprocessing import Pipe, Process
#
#
# def put(right):
#     for i in range(10):
#         right.send(i)
#     right.close()
#
#
# def get(left):
#     while True:
#         try:
#             print(left.recv())
#             pass
#         except EOFError:
#             left.close()
#             break
#             pass
#
#
# if __name__ == "__main__":
#     left, right = Pipe()
#     p1 = Process(target=put, args=(right,))
#     p2 = Process(target=get, args=(left,))
#     p1.start()
#     p2.start()
#     p1.join()
#     left.close()
#     right.close()

# ----------------------------------------------------------------------------

# from multiprocessing import Process, Pipe
#
# import time, os
#
#
# def consumer(p, name):
#     left, right = p
#     left.close()
#     while True:
#         try:
#             baozi = right.recv()
#             print('%s 收到包子:%s' % (name, baozi))
#         except EOFError:
#             right.close()
#             break
#
#
# def producer(seq, p):
#     left, right = p
#     right.close()
#     for i in seq:
#         left.send(i)
#         # time.sleep(1)
#     else:
#         left.close()
#
#
# if __name__ == '__main__':
#     left, right = Pipe()
#
#     c1 = Process(target=consumer, args=((left, right), 'c1'))
#     c1.start()
#
#     seq = (i for i in range(10))
#     producer(seq, (left, right))
#
#     right.close()
#     left.close()
#
#     c1.join()
#     print('主进程')

# 基于管道实现进程间通信（与队列的方式是类似的，队列就是管道加锁实现的）


# ----------------------------------------------------------------------------

from multiprocessing import Process, Pipe

import time, os


def adder(p, name):
    server, client = p
    client.close()
    while True:
        try:
            x, y = server.recv()
        except EOFError:
            server.close()
            break
        res = x + y
        server.send(res)
    print('server done')


if __name__ == '__main__':
    server, client = Pipe()

    c1 = Process(target=adder, args=((server, client), 'c1'))
    c1.start()

    server.close()

    client.send((10, 20))
    print(client.recv())
    client.close()

    c1.join()
    print('主进程')
# 注意：send()和recv()方法使用pickle模块对对象进行序列化。

# 管道可以用于双向通信，利用通常在客户端/服务器中使用的请求／响应模型或远程过程调用，就可以使用管道编写与进程交互的程序
