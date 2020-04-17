#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 下午3:38
# @Author  : Ryu
# @Site    : 
# @File    : 02_主线程等待子线程结束.py
# @Software: PyCharm


from threading import Thread
import time


def sayhi(name):
    time.sleep(2)
    print('%s say hello' % name)


if __name__ == '__main__':
    t = Thread(target=sayhi, args=('egon',))
    t.start()
    t.join()
    print('主线程')
    print(t.is_alive())
    '''
    egon say hello
    主线程
    False
    '''
