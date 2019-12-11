#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 下午2:53
# @Author  : Ryu
# @Site    : 
# @File    : test.py
# @Software: PyCharm


from socket import *

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',1111))


while True:
    msg=input('>>: ').strip()
    if not msg:continue

    client.send(msg.encode('utf-8'))
    # msg=client.recv(1024)
    # print(msg.decode('utf-8'))

# 多个client端