#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 下午3:32
# @Author  : Ryu
# @Site    : 
# @File    : 02_客户端.py
# @Software: PyCharm


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8080))

while True:
    msg = input('>>: ').strip()
    if not msg: continue

    s.send(msg.encode('utf-8'))
    data = s.recv(1024)
    print(data)


