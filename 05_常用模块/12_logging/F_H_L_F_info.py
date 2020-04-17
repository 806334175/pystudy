#!/usr/bin/env python
# -*- coding: utf-8 -*-

# logger：产生日志的对象

# Filter：过滤日志的对象

# Handler：接收日志然后控制打印到不同的地方，FileHandler用来打印到文件中，StreamHandler用来打印到终端

# Formatter对象：可以定制不同的日志格式对象，然后绑定给不同的Handler对象使用，以此来控制不同的Handler的日志格式

'''
critical=50
error =40
warning =30
info = 20
debug =10
'''

import logging

# 1、logger对象：负责产生日志，然后交给Filter过滤，然后交给不同的Handler输出
logger = logging.getLogger(__file__)

# 2、Filter对象：不常用，略

# 3、Handler对象：接收logger传来的日志，然后控制输出
h1 = logging.FileHandler('t1.log', encoding="utf-8")  # 打印到文件
h2 = logging.FileHandler('t2.log', encoding="utf-8")  # 打印到文件
h3 = logging.StreamHandler()  # 打印到终端

# 4、Formatter对象：日志格式
formmater1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                               datefmt='%Y-%m-%d %H:%M:%S %p', )

formmater2 = logging.Formatter('%(asctime)s :  %(message)s',
                               datefmt='%Y-%m-%d %H:%M:%S %p', )

formmater3 = logging.Formatter('%(name)s %(message)s', )

# 5、为Handler对象绑定格式
h1.setFormatter(formmater1)
h2.setFormatter(formmater2)
h3.setFormatter(formmater3)

# 6、将Handler添加给logger并设置日志级别
logger.addHandler(h1)
logger.addHandler(h2)
logger.addHandler(h3)
logger.setLevel(10)

# 7、测试
logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')
