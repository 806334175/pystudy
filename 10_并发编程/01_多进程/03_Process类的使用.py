#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 上午10:25
# @Author  : Ryu
# @Site    : 
# @File    : 03_Process类的使用.py
# @Software: PyCharm


# if __name__ == "__main__"
# since statements inside this if-statement will not get called upon import.
# 由于Windows没有fork，多处理模块启动一个新的Python进程并导入调用模块。
# 如果在导入时调用Process（），那么这将启动无限继承的新进程（或直到机器耗尽资源）。
# 这是隐藏对Process（）内部调用的原，使用if __name__ == “__main __”，这个if语句中的语句将不会在导入时被调用。


##创建并开启子进程的两种方式##

# 开进程的方法一:
import time
import random
import os
from multiprocessing import Process


def piao(name):
    print('%s piaoing' % name)
    print(os.name)
    time.sleep(random.randrange(1, 5))
    print('%s piao end' % name)


p1 = Process(target=piao, args=('egon',), name="a")  # 必须加,号
p2 = Process(target=piao, args=('alex',), name="b")
p3 = Process(target=piao, args=('wupeqi',), name="c")
p4 = Process(target=piao, args=('yuanhao',), name="d")

p1.start()
p2.start()
p3.start()
p4.start()
print('主线程')


# 开进程的方法二:
# import time
# import random
# from multiprocessing import Process


class Piao(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s piaoing' % self.name)

        time.sleep(random.randrange(1, 5))
        print('%s piao end' % self.name)


p1 = Piao('egon')
p2 = Piao('alex')
p3 = Piao('wupeiqi')
p4 = Piao('yuanhao')

p1.start()  # start会自动调用run
p2.start()
p3.start()
p4.start()
print('主线程')



##进程间内存的隔离
# from multiprocessing import Process

n = 100  # 在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了


def work():
    global n
    n = 0
    print('子进程内: ', n)


if __name__ == '__main__':
    p = Process(target=work)
    p.start()
    print('主进程内: ', n)
