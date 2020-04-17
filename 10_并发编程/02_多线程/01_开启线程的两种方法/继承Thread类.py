#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 下午3:07
# @Author  : Ryu
# @Site    : 
# @File    : 继承Thread类.py
# @Software: PyCharm


# 方式二
from threading import Thread
import time


class Sayhi(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(2)
        print('%s say hello' % self.name)


if __name__ == '__main__':
    t = Sayhi('egon')
    t.start()
    print('主线程')


