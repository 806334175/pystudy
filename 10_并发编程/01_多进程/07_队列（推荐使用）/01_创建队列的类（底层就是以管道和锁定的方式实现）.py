#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/29 上午10:00
# @Author  : Ryu
# @Site    : 
# @File    : 01_创建队列的类（底层就是以管道和锁定的方式实现）.py
# @Software: PyCharm

# 加锁可以保证多个进程修改同一块数据时，同一时间只能有一个任务可以进行修改，即串行的修改，没错，速度是慢了，但牺牲了速度却保证了数据安全。
# 虽然可以用文件共享数据实现进程间通信，但问题是：
# 1.效率低（共享数据基于文件，而文件是硬盘上的数据）
# 2.需要自己加锁处理
#
#
#
# #因此我们最好找寻一种解决方案能够兼顾：1、效率高（多个进程共享一块内存的数据）2、帮我们处理好锁问题。这就是mutiprocessing模块为我们提供的基于消息的IPC通信机制：队列和管道。
# 队列和管道都是将数据存放于内存中
# 队列又是基于（管道+锁）实现的，可以让我们从复杂的锁问题中解脱出来，
# 我们应该尽量避免使用共享数据，尽可能使用消息传递和队列，避免处理复杂的同步和锁问题，而且在进程数目增多时，往往可以获得更好的可获展性。


# Queue([maxsize]):创建共享的进程队列，Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。
# maxsize是队列中允许最大项数，省略则无大小限制。


# q.put方法用以插入数据到队列中，put方法还有两个可选参数：blocked和timeout。如果blocked为True（默认值），并且timeout为正值，该方法会阻塞timeout指定的时间，直到该队列有剩余的空间。如果超时，会抛出Queue.Full异常。如果blocked为False，但该Queue已满，会立即抛出Queue.Full异常。
# q.get方法可以从队列读取并且删除一个元素。同样，get方法有两个可选参数：blocked和timeout。如果blocked为True（默认值），并且timeout为正值，那么在等待时间内没有取到任何元素，会抛出Queue.Empty异常。如果blocked为False，有两种情况存在，如果Queue有一个值可用，则立即返回该值，否则，如果队列为空，则立即抛出Queue.Empty异常.
#
# q.get_nowait(): 同q.get(False)
# q.put_nowait(): 同q.put(False)
#
# q.empty(): 调用此方法时q为空则返回True，该结果不可靠，比如在返回True的过程中，如果队列中又加入了项目。
# q.full()：调用此方法时q已满则返回True，该结果不可靠，比如在返回True的过程中，如果队列中的项目被取走。
# q.qsize(): 返回队列中目前项目的正确数量，结果也不可靠，理由同q.empty()和q.full()一样

# 其他方法(了解)：
# 1 q.cancel_join_thread():不会在进程退出时自动连接后台线程。可以防止join_thread()方法阻塞
# 2 q.close():关闭队列，防止队列中加入更多数据。调用此方法，后台线程将继续写入那些已经入队列但尚未写入的数据，但将在此方法完成时马上关闭。如果q被垃圾收集，将调用此方法。关闭队列不会在队列使用者中产生任何类型的数据结束信号或异常。例如，如果某个使用者正在被阻塞在get()操作上，关闭生产者中的队列不会导致get()方法返回错误。
# 3 q.join_thread()：连接队列的后台线程。此方法用于在调用q.close()方法之后，等待所有队列项被消耗。默认情况下，此方法由不是q的原始创建者的所有进程调用。调用q.cancel_join_thread方法可以禁止这种行为


'''
multiprocessing模块支持进程间通信的两种主要形式:管道和队列
都是基于消息传递实现的,但是队列接口
'''

from multiprocessing import Process, Queue
import time

q = Queue(3)

# put ,get ,put_nowait,get_nowait,full,empty
q.put(3)
q.put(3)
q.put(3)
# q.put(3)
print(q.full())  # 满了

print(q.get())
print(q.get())
print(q.get())
print(q.empty())  # 空了
