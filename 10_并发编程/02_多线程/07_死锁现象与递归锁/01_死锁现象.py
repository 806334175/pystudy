#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 上午10:38
# @Author  : Ryu
# @Site    : 
# @File    : 01_死锁现象.py
# @Software: PyCharm

# 所谓死锁： 是指两个或两个以上的进程或线程在执行过程中，
# 因争夺资源而造成的一种互相等待的现象，若无外力作用，
# 它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁，
# 这些永远在互相等待的进程称为死锁进程，如下就是死锁


from threading import Thread, Lock
import time

mutexA = Lock()
mutexB = Lock()


class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        mutexA.acquire()
        print('1%s 拿到A锁' % self.name)

        mutexB.acquire()
        print('2%s 拿到B锁' % self.name)
        mutexB.release()
        print('3%s 释放B锁' % self.name)

        mutexA.release()
        print('4%s 释放A锁' % self.name)

    def func2(self):
        mutexB.acquire()
        print('5%s 拿到B锁' % self.name)
        time.sleep(2)
        # 在这个地方的时候模拟耗时操作，这个时候其他线程抢到GIL锁，拿到执行权限，然后从新运行了一遍func1和func2
        # 比如当前线程是线程1，当前线程拿到B的锁后进入了耗时操作，这个时候，线程2抢到GIL锁，拿到执行权限，先运行func1
        # 先去那A的锁，拿到了，然后去那B的锁，发现B的锁是被线程1所拿到，所以线程2只有让出运行权限，这个时候可能线程1又
        # 重新获取到了运行权限，继续往下走，想去获取A的锁，发现A的锁被线程2所拿到，这样就造成了死锁

        mutexA.acquire()
        print('6%s 拿到A锁' % self.name)
        mutexA.release()
        print('7%s 释放A锁' % self.name)

        mutexB.release()
        print('8%s 释放B锁' % self.name)


if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()
        # time.sleep(3)

'''
1Thread-1 拿到A锁
2Thread-1 拿到B锁
3Thread-1 释放B锁
4Thread-1 释放A锁
5Thread-1 拿到B锁
1Thread-2 拿到A锁
'''
