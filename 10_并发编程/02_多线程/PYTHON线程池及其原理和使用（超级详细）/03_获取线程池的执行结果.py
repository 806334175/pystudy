#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 上午11:50
# @Author  : Ryu
# @Site    : 
# @File    : 03_获取线程池的执行结果.py
# @Software: PyCharm

# 前面程序调用了 Future 的 result() 方法来获取线程任务的运回值，但该方法会阻塞当前主线程，
# 只有等到钱程任务完成后，result() 方法的阻塞才会被解除。
#
# 如果程序不希望直接调用 result() 方法阻塞线程，则可通过 Future 的 add_done_callback()
# 方法来添加回调函数，该回调函数形如 fn(future)。当线程任务完成后，程序会自动触发该回调函数，
# 并将对应的 Future 对象作为参数传给该回调函数。
# 直接调用result函数结果
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
        future.add_done_callback(test_result)
        # print(future.result())

    threadPool.shutdown(wait=True)
    print('main finished')
