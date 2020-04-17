#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 下午6:08
# @Author  : Ryu
# @Site    : 
# @File    : 06_不加锁:并发执行,速度快,数据不安全.py
# @Software: PyCharm


# 不加锁:并发执行,速度快,数据不安全
from threading import current_thread, Thread, Lock
import os, time


def task():
    global n
    print('%s is running' % current_thread().getName())
    temp = n
    time.sleep(0.5)
    n = temp - 1


if __name__ == '__main__':
    n = 100
    lock = Lock()
    threads = []
    start_time = time.time()
    for i in range(100):
        t = Thread(target=task)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    stop_time = time.time()
    print('主:%s n:%s' % (stop_time - start_time, n))

'''
Thread-1 is running
Thread-2 is running
......
Thread-100 is running
主:0.5216062068939209 n:99
'''
