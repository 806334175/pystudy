#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 下午6:10
# @Author  : Ryu
# @Site    : 
# @File    : 07_不加锁:未加锁部分并发执行,加锁部分串行执行,速度慢,数据安全.py
# @Software: PyCharm


# 不加锁:未加锁部分并发执行,加锁部分串行执行,速度慢,数据安全
from threading import current_thread, Thread, Lock
import os, time


def task():
    # 未加锁的代码并发运行
    time.sleep(3)
    print('%s start to run' % current_thread().getName())
    global n
    # 加锁的代码串行运行
    lock.acquire()
    temp = n
    time.sleep(0.5)
    n = temp - 1
    lock.release()


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
主:53.294203758239746 n:0
'''
