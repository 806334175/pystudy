#!/usr/bin/env python
# -*- coding: utf-8 -*-


######## 第一种创建进程的方法#############
# 这段代码是在windows下跑的，通过Process类可以创建一个进程对象，然后p.start()即可开启进程，test函数是你想进程实现的功能。
# from multiprocessing import Process
# import time
#
#
# def test():
#     while True:
#         print('---test---')
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     p = Process(target=test)
#     p.start()
#     while True:
#         print('---main---')
#         time.sleep(5)

######## 第二种创建进程的方法#############
# 这里是第二种创建进程的方式，通过子类继承Process类，子类中必须有run方法，里面实现进程功能，创建子类对象之后，调用对象的start方法。

from multiprocessing import Process
import time


class MyNewProcess(Process):
    def run(self):
        while True:
            print('---1---')
            time.sleep(1)


if __name__ == '__main__':

    p = MyNewProcess()
    # 调用p.start()方法，p会先去父类中寻找start()，然后在Process的start方法中调用run方法
    p.start()
    while True:
        print('---Main---')
        time.sleep(1)
