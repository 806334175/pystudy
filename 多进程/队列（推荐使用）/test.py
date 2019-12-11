#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/29 上午10:46
# @Author  : Ryu
# @Site    : 
# @File    : test.py
# @Software: PyCharm

import queue         #只能用于线程
from multiprocessing import Process,Queue            #线程，进程都能用
import time
import threading


def put(q):
    for i in range(100):
        myData = 'A'
        q.put(myData)
        myData = 'B'


def get(q):
    while True:
        res = q.get()
        print(res)


if __name__ == "__main__":
    q = queue.Queue()
    p1 = threading.Thread(target=put, args=(q,))
    p2 = threading.Thread(target=get, args=(q,))
    p1.start()
    p2.start()
    # p1.join()
    # p2.join()

