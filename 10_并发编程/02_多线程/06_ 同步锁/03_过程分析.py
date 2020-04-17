#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 下午6:01
# @Author  : Ryu
# @Site    : 
# @File    : 03_过程分析.py
# @Software: PyCharm


# 所有线程抢的是GIL锁，或者说所有线程抢的是执行权限
#
# 　　线程1抢到GIL锁，拿到执行权限，开始执行，然后加了一把Lock，还没有执行完毕，即线程1还未释放Lock，有可能线程2抢到GIL锁，开始执行，执行过程中发现Lock还没有被线程1释放，于是线程2进入阻塞，被夺走执行权限，有可能线程1拿到GIL，然后正常执行到释放Lock。。。这就导致了串行运行的效果
#
# 　　既然是串行，那我们执行
#
# 　　t1.start()
#
# 　　t1.join
#
# 　　t2.start()
#
# 　　t2.join()
#
# 　　这也是串行执行啊，为何还要加Lock呢，需知join是等待t1所有的代码执行完，相当于锁住了t1的所有代码，而Lock只是锁住一部分操作共享数据的代码。


# 因为Python解释器帮你自动定期进行内存回收，
# 你可以理解为python解释器里有一个独立的线程，
# 每过一段时间它起wake up做一次全局轮询看看哪些内存数据是可以被清空的，
# 此时你自己的程序 里的线程和 py解释器自己的线程是并发运行的，假设你的线程删除了一个变量，
# py解释器的垃圾回收线程在清空这个变量的过程中的clearing时刻，
# 可能一个其它线程正好又重新给这个还没来及得清空的内存空间赋值了，
# 结果就有可能新赋值的数据被删除了，为了解决类似的问题，
# python解释器简单粗暴的加了锁，即当一个线程运行时，其它人都不能动，
# 这样就解决了上述的问题，  这可以说是Python早期版本的遗留问题。


from threading import Thread
import os, time


def work():
    global n
    temp = n
    time.sleep(0.1)
    n = temp - 1


if __name__ == '__main__':
    n = 100
    l = []
    for i in range(100):
        p = Thread(target=work)
        l.append(p)
        p.start()
    for p in l:
        p.join()

    print(n)  # 结果可能为99 因为100个线程同时对n进行操作，所有线程运行的都是100-1，所以是99
