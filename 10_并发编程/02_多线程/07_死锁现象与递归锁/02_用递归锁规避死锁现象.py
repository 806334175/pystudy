#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 上午11:00
# @Author  : Ryu
# @Site    : 
# @File    : 02_用递归锁规避死锁现象.py
# @Software: PyCharm


# 解决方法，递归锁，在Python中为了支持在同一线程中多次请求同一资源，python提供了可重入锁RLock。

# 这个RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，
# 从而使得资源可以被多次require。直到一个线程所有的acquire都被release，
# 其他的线程才能获得资源。上面的例子如果使用RLock代替Lock，则不会发生死锁：


# mutexA=mutexB=threading.RLock() #一个线程拿到锁，counter加1,该线程内又碰到加锁的情况，
# 则counter继续加1，这期间所有其他线程都只能等待，等待该线程释放所有锁，即counter递减到0为止


from threading import Thread, Lock,RLock
import time

obj = RLock()

mutexA = obj
mutexB = obj

class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        mutexA.acquire()
        print('\033[41m%s 拿到A锁\033[0m' % self.name)

        mutexB.acquire()
        print('\033[42m%s 拿到B锁\033[0m' % self.name)
        mutexB.release()

        mutexA.release()

    def func2(self):
        mutexB.acquire()
        print('\033[43m%s 拿到B锁\033[0m' % self.name)
        time.sleep(2)

        mutexA.acquire()
        print('\033[44m%s 拿到A锁\033[0m' % self.name)
        mutexA.release()

        mutexB.release()


if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()


