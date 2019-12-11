#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 上午11:02
# @Author  : Ryu
# @Site    : 
# @File    : 异步调用apply_async.py
# @Software: PyCharm


from multiprocessing import Pool
import os, time


def work(n):
    print('%s run' % os.getpid())
    time.sleep(3)
    return n ** 2


if __name__ == '__main__':
    start_time = time.time()

    p = Pool(3)  # 进程池中从无到有创建三个进程,以后一直是这三个进程在执行任务
    res_l = []
    for i in range(10):
        res = p.apply_async(work, args=(i,))  # 同步运行,阻塞、直到本次任务执行完毕拿到res
        res_l.append(res)  # 先拿到AsyncResult类的实例，后面等收到结果后用get()调用

    # 异步apply_async用法：如果使用异步提交的任务，主进程需要使用jion，等待进程池内任务都处理完，然后可以用get收集结果，否则，主进程结束，进程池可能还没来得及执行，也就跟着一起结束了
    p.close()
    p.join()  # 确保每个AsyncResult类的实例都拿到结果了
    for res in res_l:
        print("-------------")
        print(res.get())  # 使用get来获取apply_aync的结果,如果是apply,则没有get方法,因为apply是同步执行,立刻获取结果,也根本无需get

    end_time = time.time()
    use_time = end_time - start_time
    print("用时为:%f" % use_time)
# 异步调用apply_async
