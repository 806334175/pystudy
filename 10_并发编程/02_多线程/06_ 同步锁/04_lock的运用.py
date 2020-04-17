#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 下午6:01
# @Author  : Ryu
# @Site    : 
# @File    : 04_lock的运用.py
# @Software: PyCharm

# 锁通常被用来实现对共享资源的同步访问。为每一个共享资源创建一个Lock对象，
# 当你需要访问该资源时，调用acquire方法来获取锁对象（如果其它线程已经获得了该锁，则当前线程需等待其被释放），
# 待资源访问完后，再调用release方法释放锁：


# import threading
#
# R = threading.Lock()
#
# R.acquire()
# '''
# 对公共数据的操作
# '''
# R.release()

from threading import Thread, Lock
import os, time


def work():
    global n
    lock.acquire()
    temp = n
    time.sleep(0.1)
    n = temp - 1
    lock.release()


if __name__ == '__main__':
    lock = Lock()
    n = 100
    l = []
    for i in range(100):
        p = Thread(target=work)
        l.append(p)
        p.start()
    for p in l:
        p.join()

    print(n)  # 结果肯定为0，由原来的并发执行变成串行，牺牲了执行效率保证了数据安全
