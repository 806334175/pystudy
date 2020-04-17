#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shutil

# 高级的
# 文件、文件夹、压缩包
# 处理模块

# # shutil.copyfileobj(fsrc, fdst[, length])
# # 将文件内容拷贝到另一个文件中--------------------
# shutil.copyfileobj(open('old.xml', 'r', encoding="UTF-8"), open('new.xml', 'w', encoding="UTF-8")) # 目标文件无需存在
#
# # shutil.copyfile(src, dst)
# # 拷贝文件------------------------
# shutil.copyfile('f1.log', 'f2.log')  # 目标文件无需存在
#
# # shutil.copymode(src, dst)
# # 仅拷贝权限。内容、组、用户均不变-------------
# shutil.copymode('f1.log', 'f2.log')  # 目标文件必须存在
#
# # shutil.copystat(src, dst)
# # 仅拷贝状态的信息，包括：mode
# # bits, atime, mtime, flags------------------
# shutil.copystat('f1.log', 'f2.log')  # 目标文件必须存在
#
# # shutil.copy(src, dst)
# # 拷贝文件和权限-------------
# shutil.copy('f1.log', 'f2.log')
#
# # shutil.copy2(src, dst)
# # 拷贝文件和状态信息---------------
# shutil.copy2('f1.log', 'f2.log')


