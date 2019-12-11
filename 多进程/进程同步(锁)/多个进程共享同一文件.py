#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 下午6:14
# @Author  : Ryu
# @Site    : 
# @File    : 多个进程共享同一文件.py
# @Software: PyCharm


# 并发运行，效率高，但竞争写同一文件，数据写入错乱
# 文件db的内容为：{"count":1}
# 注意一定要用双引号，不然json无法识别
from multiprocessing import Process, Lock
import time, json, random


def search():
    dic = json.load(open('db.txt'))
    print('\033[43m剩余票数%s\033[0m' % dic['count'])


def get():
    dic = json.load(open('db.txt'))
    time.sleep(0.1)  # 模拟读数据的网络延迟
    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(0.2)  # 模拟写数据的网络延迟
        json.dump(dic, open('db.txt', 'w'))
        print('\033[43m购票成功\033[0m')


def task(lock):
    search()
    # lock.acquire()
    get()
    # lock.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(100):  # 模拟并发100个客户端抢票
        p = Process(target=task, args=(lock,))
        p.start()
