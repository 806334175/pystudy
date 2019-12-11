#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from bs4 import BeautifulSoup
import os
import requests
import xlwt
import xlrd
import threading
import time
from xlutils import copy
import re
import queue

file = "D:\\offer_list.xls"

HEADERS = {
    'User-Agent': '',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': ''
}


def read_cols_excel(sheet, cols):
    try:
        wb = xlrd.open_workbook(filename=file)
        sheet1 = wb.sheet_by_index(sheet)
        cols_res = sheet1.col_values(cols)
    except IndexError as e:
        print('except:', e)
        print("读取列为空")
        return 0
    except PermissionError as e:
        print('except:', e)
        print("excel文件没有关闭")
        return 0
    return cols_res


def write_excel(sheet, row, col, str):
    try:
        rb = xlrd.open_workbook(filename=file)
        wb = copy.copy(rb)
        sheet1 = wb.get_sheet(sheet)
        sheet1.write(row, col, str)
        os.remove(file)
        wb.save(file)
    except IndexError as e:
        return 1
    except FileNotFoundError as e:
        return 1
    except PermissionError as e:
        return 1
    return 0


def get_cookie():
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
    print(response)
    res = response.cookies.get_dict()['JSESSIONID']
    return "JSESSIONID=" + res


def check_offer(UserAgent, Cookie, offerid):
    HEADERS["User-Agent"] = UserAgent
    HEADERS["Cookie"] = Cookie
    url = "http://affbb.tbnetwork.im/aff/offer/detail?id=" + offerid
    session = requests.session()
    response = session.post(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'lxml')  # 创建 beautifulsoup 对象
    res = soup.find_all("script", {"type": "text/javascript"})
    try:
        country = re.findall('countries":\["(.*)"\],"currency', str(res[14]))[0]
    except IndexError as e:
        country = None

    res_number = soup.find_all(type="number", class_="col-xs-10 col-sm-9")
    for k in res_number:
        if k["name"] == "price":
            res_price = k["value"]

    res = soup.find_all(type="text", class_="col-xs-10 col-sm-9")
    print(res)
    for k in res:
        try:
            if k["name"] == "packageName":
                res_id = k["value"]
            if k["name"] == "trackUrl":
                res_trackUrl = k["value"]
            if k["name"] == "offerName":
                res_offerName = k["value"]
            if k["name"] == "prodName":
                res_prodName = k["value"]
            if k["name"] == "price":
                res_price = k["value"]
            if k["name"] == "previewLink":
                res_previewLink = k["value"]
        except KeyError as e:
            res_offer_id = k["value"]

    print("[" + offerid + "]packageName：" + res_id + "\n" + "[" + offerid + "]trackUrl：" + res_trackUrl + "\n" + "[" + offerid + "]offer_id:" + offerid)
    return res_offerName, res_prodName, res_id, res_price, country, res_previewLink, res_trackUrl


def check_begin(cookie, offer_id, num):
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
    res = check_offer(ua, cookie, offer_id)

    ww = 1
    for i in res:
        lock.acquire()
        try:
            write_excel(0, num, ww, i)
        finally:
            lock.release()
            # pass
        ww += 1


if __name__ == '__main__':
    cookie = get_cookie()
    lock = threading.Lock()
    list_offer_id = read_cols_excel(0, 0)
    num = 0
    for key in list_offer_id:
        print(str(list_offer_id[num])+"ok")
        threading.Thread(target=check_begin, args=(cookie, str(list_offer_id[num]), num,)).start()
        # time.sleep(2)
        num = num + 1
