#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 下午4:36
# @Author  : Ryu
# @Site    : 
# @File    : 守护进程.py
# @Software: PyCharm

# 主进程创建守护进程
#
# 　　其一：守护进程会在主进程代码执行结束后就终止
#
# 　　其二：守护进程内无法再开启子进程,否则抛出异常：AssertionError: daemonic processes are not allowed to have children
#
# 注意：进程之间是互相独立的，主进程代码运行结束，守护进程随即终止


# from multiprocessing import Process
# import time
# import random
#
#
# class Piao(Process):
#     def __init__(self, a):
#         self.name = a
#         super().__init__()
#
#     def run(self):
#         print('%s is piaoing' % self.name)
#         time.sleep(random.randrange(1, 3))
#         print('%s is piao end' % self.name)
#
#
# p = Piao('abc')
# p.daemon = True  # 一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
# p.start()
# print(p.name)
# time.sleep(1)
# print('主')


# 主进程代码运行完毕,守护进程就会结束
from multiprocessing import Process
from threading import Thread
import time


def foo():
    print(123)
    time.sleep(1)
    print("end123")


def bar():
    print(456)
    time.sleep(3)
    print("end456")


p1 = Process(target=foo)
p2 = Process(target=bar)

p1.daemon = True
p1.start()
p2.start()
print("main-------")  # 打印该行则主进程代码结束,则守护进程p1应该被终止,可能会有p1任务执行的打印信息123,因为主进程打印main----时,p1也执行了,但是随即被终止

# 迷惑人的例子
