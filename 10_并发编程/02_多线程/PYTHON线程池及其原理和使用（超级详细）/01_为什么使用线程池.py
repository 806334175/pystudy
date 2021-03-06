#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 上午11:43
# @Author  : Ryu
# @Site    : 
# @File    : 01_为什么使用线程池.py
# @Software: PyCharm

# 系统启动一个新线程的成本是比较高的，因为它涉及与操作系统的交互。在这种情形下，
# 使用线程池可以很好地提升性能，尤其是当程序中需要创建大量生存期很短暂的线程时，更应该考虑使用线程池。
#
# 线程池在系统启动时即创建大量空闲的线程，程序只要将一个函数提交给线程池，
# 线程池就会启动一个空闲的线程来执行它。当该函数执行结束后，该线程并不会死亡，而是再次返回到线程池中变成空闲状态，等待执行下一个函数。
#
# 此外，使用线程池可以有效地控制系统中并发线程的数量。当系统中包含有大量的并发线程时，
# 会导致系统性能急剧下降，甚至导致 Python 解释器崩溃，而线程池的最大线程数参数可以控制系统中并发线程的数量不超过此数。
