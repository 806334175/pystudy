#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 下午6:13
# @Author  : Ryu
# @Site    : 
# @File    : 08_用join替代加锁.py
# @Software: PyCharm


# 有的同学可能有疑问:既然加锁会让运行变成串行,那么我在start之后立即使用join,就不用加锁了啊,也是串行的效果啊
# 没错:在start之后立刻使用jion,肯定会将100个任务的执行变成串行,毫无疑问,最终n的结果也肯定是0,是安全的,但问题是
# start后立即join:任务内的所有代码都是串行执行的,而加锁,只是加锁的部分即修改共享数据的部分是串行的
# 单从保证数据安全方面,二者都可以实现,但很明显是加锁的效率更高.
from threading import current_thread, Thread, Lock
import os, time


def task():
    time.sleep(3)
    print('%s start to run' % current_thread().getName())
    global n
    temp = n
    time.sleep(0.5)
    n = temp - 1


if __name__ == '__main__':
    n = 100
    lock = Lock()
    start_time = time.time()
    for i in range(100):
        t = Thread(target=task)
        t.start()
        t.join()
    stop_time = time.time()
    print('主:%s n:%s' % (stop_time - start_time, n))

'''
Thread-1 start to run
Thread-2 start to run
......
Thread-100 start to run
主:350.6937336921692 n:0 #耗时是多么的恐怖
'''
