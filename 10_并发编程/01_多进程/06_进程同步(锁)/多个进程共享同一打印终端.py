#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 下午5:43
# @Author  : Ryu
# @Site    : 
# @File    : 多个进程共享同一打印终端.py
# @Software: PyCharm

# 并发运行,效率高,但竞争同一打印终端,带来了打印错乱
# from multiprocessing import Process
# import os, time
#
#
# def work():
#     print('%s is running' % os.getpid())
#     time.sleep(2)
#     print('%s is done' % os.getpid())
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         p = Process(target=work)
#         p.start()


# 由并发变成了串行,牺牲了运行效率,但避免了竞争
from multiprocessing import Process, Lock
import os, time


def work(lock):
    lock.acquire()
    try:
        print('%s is running' % os.getpid())
        time.sleep(2)
        print('%s is done' % os.getpid())
    finally:
        lock.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(3):
        p = Process(target=work, args=(lock,))
        p.start()
