#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MyLogging Test
"""

import time
import logging
import logging配置文件  # 导入自定义的logging配置

logger = logging.getLogger(__name__)  # 生成logger实例


def demo():
    logger.debug("start range... time:{}".format(time.time()))
    logger.info("中文测试开始。。。")
    for i in range(10):
        logger.debug("i:{}".format(i))
        time.sleep(0.2)
    else:
        logger.debug("over range... time:{}".format(time.time()))
    logger.info("中文测试结束。。。")


if __name__ == "__main__":
    logging配置文件.load_my_logging_cfg()  # 在你程序文件的入口加载自定义logging配置
    demo()

# 使用
