#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 上午11:29
# @Author  : Ryu
# @Site    : 
# @File    : client.py
# @Software: PyCharm

from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

while True:
    # msg = input('>>:').strip()
    msg = input()
    print(msg)
    if not msg: continue

    client.send(msg.encode('utf-8'))
    msg = client.recv(1024)
    print(msg.decode('utf-8'))

# 客户端
