#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 注意注意注意：
#
#
# # 1、有了上述方式我们的好处是：所有与logging模块有关的配置都写到字典中就可以了，更加清晰，方便管理
#
#
# # 2、我们需要解决的问题是：
# 1、从字典加载配置：12_logging.config.dictConfig(settings.LOGGING_DIC)
#
# 2、拿到logger对象来产生日志
# logger对象都是配置到字典的loggers
# 键对应的子字典中的
# 按照我们对logging模块的理解，要想获取某个东西都是通过名字，也就是key来获取的
# 于是我们要获取不同的logger对象就是
# logger = 12_logging.getLogger('loggers子字典的key名')
#
# 但问题是：如果我们想要不同logger名的logger对象都共用一段配置，那么肯定不能在loggers子字典中定义n个key
# 'loggers': {
#     'l1': {
#         'handlers': ['default', 'console'],  #
#         'level': 'DEBUG',
#         'propagate': True,  # 向上（更高level的logger）传递
#     },
#     'l2: {
#     'handlers': ['default', 'console'],
#     'level': 'DEBUG',
#     'propagate': False,  # 向上（更高level的logger）传递
# },
# 'l3': {
#     'handlers': ['default', 'console'],  #
#     'level': 'DEBUG',
#     'propagate': True,  # 向上（更高level的logger）传递
# },
#
# }
#
#
# # 我们的解决方式是，定义一个空的key
# 'loggers': {
# '': {
#     'handlers': ['default', 'console'],
#     'level': 'DEBUG',
#     'propagate': True,
# },
#
# }
#
# 这样我们再取logger对象时
# 12_logging.getLogger(__name__)，不同的文件__name__不同，这保证了打印日志时标识信息不同，但是拿着该名字去loggers里找key名时却发现找不到，于是默认使用key = ''
# 的配置
#
# !!!关于如何拿到logger对象的详细解释！！！