#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Logger is also the first to filter the message based on a level — if you set the logger to INFO, and all handlers to DEBUG, you still won't receive DEBUG messages on handlers — they'll be rejected by the logger itself. If you set logger to DEBUG, but all handlers to INFO, you won't receive any DEBUG messages either — because while the logger says "ok, process this", the handlers reject it (DEBUG < INFO).


# 验证
import logging

form = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                         datefmt='%Y-%m-%d %H:%M:%S %p', )

# ch = 12_logging.StreamHandler("test.log",encoding="utf-8")
ch = logging.FileHandler("test.log", encoding="utf-8")

ch.setFormatter(form)
# ch.setLevel(10)
ch.setLevel(20)

l1 = logging.getLogger('root')
# l1.setLevel(20)
l1.setLevel(10)
l1.addHandler(ch)

l1.debug('l1 debug')
l1.info('l1 info')

# 重要，重要，重要！！！
