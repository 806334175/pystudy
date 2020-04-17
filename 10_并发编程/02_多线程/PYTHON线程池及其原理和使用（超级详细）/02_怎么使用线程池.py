#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 上午11:44
# @Author  : Ryu
# @Site    : 
# @File    : 02_怎么使用线程池.py
# @Software: PyCharm


# 线程池的基类是 concurrent.futures 模块中的 Executor，Executor 提供了两个子类，即 ThreadPoolExecutor 和 ProcessPoolExecutor，
# 其中 ThreadPoolExecutor 用于创建线程池，而 ProcessPoolExecutor 用于创建进程池。
#
# 如果使用线程池/进程池来管理并发编程，那么只要将相应的 task 函数提交给线程池/进程池，剩下的事情就由线程池/进程池来搞定。
#
# Exectuor 提供了如下常用方法：
#
# submit(fn, *args, **kwargs)：将 fn 函数提交给线程池。*args 代表传给 fn 函数的参数，*kwargs 代表以关键字参数的形式为 fn 函数传入参数。
# map(func, *iterables, timeout=None, chunksize=1)：该函数类似于全局函数 map(func, *iterables)，只是该函数将会启动多个线程，
# 以异步方式立即对 iterables 执行 map 处理。
# shutdown(wait=True)：关闭线程池。
#
# 程序将 task 函数提交（submit）给线程池后，submit 方法会返回一个 Future 对象，Future 类主要用于获取线程任务函数的返回值。
# 由于线程任务会在新线程中以异步方式执行，因此，线程执行的函数相当于一个“将来完成”的任务，所以 Python 使用 Future 来代表。
#
# Future 提供了如下方法：
#
# cancel()：取消该 Future 代表的线程任务。如果该任务正在执行，不可取消，则该方法返回 False；否则，程序会取消该任务，并返回 True。
# cancelled()：返回 Future 代表的线程任务是否被成功取消。
# running()：如果该 Future 代表的线程任务正在执行、不可被取消，该方法返回 True。
# done()：如果该 Funture 代表的线程任务被成功取消或执行完成，则该方法返回 True。
# result(timeout=None)：获取该 Future 代表的线程任务最后返回的结果。如果 Future 代表的线程任务还未完成，该方法将会阻塞当前线程，
#                       其中 timeout 参数指定最多阻塞多少秒。
# exception(timeout=None)：获取该 Future 代表的线程任务所引发的异常。如果该任务成功完成，没有异常，则该方法返回 None。
# add_done_callback(fn)：为该 Future 代表的线程任务注册一个“回调函数”，当该任务成功完成时，程序会自动触发该 fn 函数。
#
# 在用完一个线程池后，应该调用该线程池的 shutdown() 方法，该方法将启动线程池的关闭序列。调用 shutdown() 方法后的线程池不再接收新任务，
# 但会将以前所有的已提交任务执行完成。当线程池中的所有任务都执行完成后，该线程池中的所有线程都会死亡。
#
# 使用线程池来执行线程任务的步骤如下：
#
#    1,调用 ThreadPoolExecutor 类的构造器创建一个线程池。
#    2.定义一个普通函数作为线程任务。
#    3,调用 ThreadPoolExecutor 对象的 submit() 方法来提交线程任务。
#    4,当不想提交任何任务时，调用 ThreadPoolExecutor 对象的 shutdown() 方法来关闭线程池。

from concurrent.futures import ThreadPoolExecutor
import threading, time


def test(value1, value2=None):
    print("%s threading is printed %s, %s" % (threading.current_thread().name, value1, value2))
    time.sleep(2)
    return 'finished'


def test_result(future):
    print(future.result())


if __name__ == "__main__":

    threadPool = ThreadPoolExecutor(max_workers=4, thread_name_prefix="test_")
    for i in range(0, 10):
        future = threadPool.submit(test, i, i + 1)

    threadPool.shutdown(wait=True)
