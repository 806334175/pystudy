#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/29 上午10:07
# @Author  : Ryu
# @Site    : 
# @File    : 02_生产者消费者模型.py
# @Software: PyCharm

'''
生产者消费者模型

在并发编程中使用生产者和消费者模式能够解决绝大多数并发问题。该模式通过平衡生产线程和消费线程的工作能力来提高程序的整体处理数据的速度。

    为什么要使用生产者和消费者模式

在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。在多线程开发当中，如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个问题于是引入了生产者和消费者模式。

    什么是生产者消费者模式

生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。

基于队列实现生产者消费者模型
'''

from multiprocessing import Process, Queue
import time, random, os


def consumer(q):
    while True:
        res = q.get()
        time.sleep(random.randint(1, 3))
        print('\033[45m%s 吃 %s\033[0m' % (os.getpid(), res))


def producer(q):
    for i in range(10):
        time.sleep(random.randint(1, 3))
        res = '包子%s' % i
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m' % (os.getpid(), res))


if __name__ == '__main__':
    q = Queue()
    # 生产者们:即厨师们
    p1 = Process(target=producer, args=(q,))

    # 消费者们:即吃货们
    c1 = Process(target=consumer, args=(q,))

    # 开始
    p1.start()
    c1.start()
    print('主')

# # 生产者消费者模型总结
#
#     # 程序中有两类角色
#     一类负责生产数据（生产者）
#     一类负责处理数据（消费者）
#
#     # 引入生产者消费者模型为了解决的问题是：
#     平衡生产者与消费者之间的工作能力，从而提高程序整体处理数据的速度
#
#     # 如何实现：
#     生产者 < -->队列 <—— > 消费者
# # 生产者消费者模型实现类程序的解耦和