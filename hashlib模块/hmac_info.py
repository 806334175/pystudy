#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 它内部对我们创建 key 和 内容 进行进一步的处理然后再加密:
import hmac

h = hmac.new('alvin'.encode('utf8'))
h.update('hello'.encode('utf8'))
print(h.hexdigest())  # 320df9832eab4c038b6c1d7ed73a5940


# 注意！注意！注意
#要想保证hmac最终结果一致，必须保证：
#1:hmac.new括号内指定的初始key一样
#2:无论update多少次，校验的内容累加到一起是一样的内容


h1=hmac.new(b'egon')
h1.update(b'hello')
h1.update(b'world')
print(h1.hexdigest())

h2=hmac.new(b'egon')
h2.update(b'helloworld')
print(h2.hexdigest())

h3=hmac.new(b'egonhelloworld')
print(h3.hexdigest())

'''
f1bf38d054691688f89dcd34ac3c27f2
f1bf38d054691688f89dcd34ac3c27f2
bcca84edd9eeb86f30539922b28f3981
'''

