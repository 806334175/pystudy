#!/usr/bin/env python
# -*- coding: utf-8 -*-


import configparser

# ----读取---------------------------------
config = configparser.ConfigParser()
config.read('a.cfg')

# 查看所有的标题
res = config.sections()  # ['section1', 'section2']
print(res)

# 查看标题section1下所有key=value的key
options = config.options('section1')
print(options)  # ['k1', 'k2', 'user', 'age', 'is_admin', 'salary']

# 查看标题section1下所有key=value的(key,value)格式
item_list = config.items('section1')
print(
    item_list)  # [('k1', 'v1'), ('k2', 'v2'), ('user', 'egon'), ('age', '18'), ('is_admin', 'true'), ('salary', '31')]

# 查看标题section1下user的值=>字符串格式
val = config.get('section1', 'user')
print(val)  # egon

# 查看标题section1下age的值=>整数格式
val1 = config.getint('section1', 'age')
print(val1)  # 18

# 查看标题section1下is_admin的值=>布尔值格式
val2 = config.getboolean('section1', 'is_admin')
print(val2)  # True

# 查看标题section1下salary的值=>浮点型格式
val3 = config.getfloat('section1', 'salary')
print(val3)  # 31.0

# ----改写---------------------------------

config = configparser.ConfigParser()
config.read('a.cfg', encoding='utf-8')

# 删除整个标题section2
config.remove_section('section2')

# 删除标题section1下的某个k1和k2
config.remove_option('section1', 'k1')
config.remove_option('section1', 'k2')

# 判断是否存在某个标题
print(config.has_section('section1'))

# 判断标题section1下是否有user
print(config.has_option('section1', 'user'))

# 添加一个标题
config.add_section('egon')

# 在标题egon下添加name=egon,age=18的配置
config.set('egon', 'name', 'egon')
config.set('egon', 'age', "18")  # 报错,必须是字符串

# 最后将修改的内容写入文件,完成最终的修改
config.write(open('b.cfg', 'w'))

# ----添加ini文档-------------------------

config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'

with open('example.ini', 'w') as configfile:
    config.write(configfile)


