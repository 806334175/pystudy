#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 下午6:00
# @Author  : Ryu
# @Site    : 
# @File    : 02_GIL VS Lock.py
# @Software: PyCharm


# 机智的同学可能会问到这个问题，就是既然你之前说过了，Python已经有一个GIL来保证同一时间只能有一个线程来执行了，为什么这里还需要lock?
#
# 　首先我们需要达成共识：锁的目的是为了保护共享的数据，同一时间只能有一个线程来修改共享的数据
#
#     然后，我们可以得出结论：保护不同的数据就应该加不同的锁。
#
# 　最后，问题就很明朗了，GIL 与Lock是两把锁，保护的数据不一样，前者是解释器级别的（当然保护的就是解释器级别的数据，比如垃圾回收的数据），
#
# 后者是保护用户自己开发的应用程序的数据，很明显GIL不负责这件事，只能用户自定义加锁处理，即Lock
