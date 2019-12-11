#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests

post_dict = {
    'username': 'Eason',
    'password': 'Y6u?8waWe^',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
}

# 2 将密码字典以post方式提交到抽屉的登录界面
response = requests.post(
    url='http://affbb.tbnetwork.im/login',
    data=post_dict
)

print(response.text)

print(response.cookies.get_dict()['JSESSIONID'])
