#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 下午5:32
# @Author  : Ryu
# @Site    : 
# @File    : 04_Process对象的其他方法或属性（了解）.py
# @Software: PyCharm

# 进程对象的其他方法一:terminate,is_alive
# from multiprocessing import Process
# import time
# import random
#
#
# class Piao(Process):
#     def __init__(self, name):
#         self.name = name
#         super().__init__()
#
#     def run(self):
#         print('%s is piaoing' % self.name)
#         time.sleep(random.randrange(1, 5))
#         print('%s is piao end' % self.name)
#
#
# p1 = Piao('egon1')
# p1.start()
#
# p1.terminate()  # 关闭进程,不会立即关闭,所以is_alive立刻查看的结果可能还是存活
# print(p1.is_alive())  # 结果为True
# print('开始')
# time.sleep(5)
# print(p1.is_alive())  # 结果为False


# 进程对象的其他方法二:pid,name
from multiprocessing import Process
import time
import random


class Piao(Process):
    def __init__(self, name):
        # self.name=name
        # super().__init__() #Process的__init__方法会执行self.name=Piao-1,
        #                    #所以加到这里,会覆盖我们的self.name=name

        # 为我们开启的进程设置名字的做法
        super().__init__()
        self.name = name

    def run(self):
        print('%s is piaoing' % self.name)
        time.sleep(random.randrange(1, 3))
        print('%s is piao end' % self.name)


p = Piao('egon')
p.start()
print('开始')
print(p.pid)  # 查看pid
