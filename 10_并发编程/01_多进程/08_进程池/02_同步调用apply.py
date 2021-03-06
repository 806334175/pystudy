#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 上午10:05
# @Author  : Ryu
# @Site    : 
# @File    : 02_同步调用apply.py
# @Software: PyCharm


from multiprocessing import Pool
import os, time


def work(n):
    print('%s run' % os.getpid())
    time.sleep(1)
    return n ** 2


if __name__ == '__main__':
    p = Pool(3)  # 进程池中从无到有创建三个进程,以后一直是这三个进程在执行任务
    res_l = []
    for i in range(10):
        # 同步调用，直到本次任务执行完毕拿到res，等待任务work执行的过程中可能有阻塞也可能没有阻塞，但不管该任务是否存在阻塞，同步调用都会在原地等着，只是等的过程中若是任务发生了阻塞就会被夺走cpu的执行权限
        res = p.apply(work, args=(i,))
        res_l.append(res)
    print(res_l)

# 同步调用apply
