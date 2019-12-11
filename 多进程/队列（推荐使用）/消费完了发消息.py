#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 上午11:20
# @Author  : Ryu
# @Site    : 
# @File    : 消费完了发消息.py
# @Software: PyCharm


#JoinableQueue([maxsize])：这就像是一个Queue对象，但队列允许项目的使用者通知生成者项目已经被成功处理。通知进程是使用共享的信号和条件变量来实现的。

   #参数介绍：
#     maxsize是队列中允许最大项数，省略则无大小限制。
# 　 #方法介绍：
#     JoinableQueue的实例p除了与Queue对象相同的方法之外还具有：
#     q.task_done()：使用者使用此方法发出信号，表示q.get()的返回项目已经被处理。如果调用此方法的次数大于从队列中删除项目的数量，将引发ValueError异常
#     q.join():生产者调用此方法进行阻塞，直到队列中所有的项目均被处理。阻塞将持续到队列中的每个项目均调用q.task_done（）方法为止

from multiprocessing import Process, JoinableQueue
import time, random, os


def consumer(q):
    while True:
        res = q.get()
        time.sleep(random.randint(1, 3))
        print('\033[45m%s 吃 %s\033[0m' % (os.getpid(), res))

        q.task_done()  # 向q.join()发送一次信号,证明一个数据已经被取走了


def producer(name, q):
    for i in range(10):
        time.sleep(random.randint(1, 3))
        res = '%s%s' % (name, i)
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m' % (os.getpid(), res))
    q.join()


if __name__ == '__main__':
    q = JoinableQueue()
    # 生产者们:即厨师们
    p1 = Process(target=producer, args=('包子', q))
    p2 = Process(target=producer, args=('骨头', q))
    p3 = Process(target=producer, args=('泔水', q))

    # 消费者们:即吃货们
    c1 = Process(target=consumer, args=(q,))
    c2 = Process(target=consumer, args=(q,))
    c1.daemon = True
    c2.daemon = True

    # 开始
    p_l = [p1, p2, p3, c1, c2]
    for p in p_l:
        p.start()

    p1.join()
    p2.join()
    p3.join()
    print('主')

    # 主进程等--->p1,p2,p3等---->c1,c2
    # p1,p2,p3结束了,证明c1,c2肯定全都收完了p1,p2,p3发到队列的数据
    # 因而c1,c2也没有存在的价值了,应该随着主进程的结束而结束,所以设置成守护进程