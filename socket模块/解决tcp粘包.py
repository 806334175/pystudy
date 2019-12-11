#!/usr/bin/env python
# -*- coding: utf-8 -*-

###########解决方法################
# 为字节流加上自定义固定长度报头，报头中包含字节流长度，然后一次send到对端，对端在接收时，先从缓存中取出定长的报头，然后再取真实数据
#
# struct模块
#
# 该模块可以把一个类型，如数字，转成固定长度的bytes
#
# >>> struct.pack('i',1111111111111)
#
# 。。。。。。。。。
#
# struct.error: 'i' format requires -2147483648 <= number <= 2147483647 #这个是范围


#########服务端（自定义报头）#############

import socket, struct, json
import subprocess

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 就是它，在bind前加

phone.bind(('127.0.0.1', 8080))

phone.listen(5)

while True:
    conn, addr = phone.accept()
    while True:
        cmd = conn.recv(1024)
        if not cmd: break
        print('cmd: %s' % cmd)

        res = subprocess.Popen(cmd.decode('utf-8'),
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        err = res.stderr.read()
        print(err)
        if err:
            back_msg = err
        else:
            back_msg = res.stdout.read()

        conn.send(struct.pack('i', len(back_msg)))  # 先发back_msg的长度
        conn.sendall(back_msg)  # 在发真实的内容

    conn.close()

# 服务端（自定制报头）


#############客户端（自定义报头）############
# _*_coding:utf-8_*_
# __author__ = 'Linhaifeng'
# import socket,time,struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
res = s.connect_ex(('127.0.0.1', 8080))

while True:
    msg = input('>>: ').strip()
    if len(msg) == 0: continue
    if msg == 'quit': break

    s.send(msg.encode('utf-8'))

    l = s.recv(4)
    x = struct.unpack('i', l)[0]
    print(type(x), x)
    # print(struct.unpack('I',l))
    r_s = 0
    data = b''
    while r_s < x:
        r_d = s.recv(1024)
        data += r_d
        r_s += len(r_d)

    # print(data.decode('utf-8'))
    print(data.decode('gbk'))  # windows默认gbk编码

# 客户端（自定制报头）
