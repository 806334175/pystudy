#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 上午10:20
# @Author  : Ryu
# @Site    : 
# @File    : 01_multiprocessing模块介绍.py
# @Software: PyCharm


# python中的多线程无法利用多核优势，如果想要充分地使用多核CPU的资源（os.cpu_count()查看），在python中大部分情况需要使用多进程。Python提供了multiprocessing。
#     multiprocessing模块用来开启子进程，并在子进程中执行我们定制的任务（比如函数），该模块与多线程模块threading的编程接口类似。
#
# 　 multiprocessing模块的功能众多：支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件。
#
#     需要再次强调的一点是：与线程不同，进程没有任何共享状态，进程修改的数据，改动仅限于该进程内。
