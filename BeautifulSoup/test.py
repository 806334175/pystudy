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

file = "D:\\offer_check.xls"

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


def get_redirect_url(track_url, super_proxy_url):
    time.sleep(0.1)

    # print("get_redirect_url")
    # 重定向前的链接
    res = ""
    rs = ""
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
    }

    # 请求网页

    proxies = {"http": super_proxy_url,
               "https": super_proxy_url,

               }
    try:
        res = requests.get(track_url, proxies=proxies, headers=headers, allow_redirects=False, timeout=20)
    except requests.exceptions.ProxyError as requestsE:
        print(requestsE)
        pass

    if type(res) is str:

        return res
        pass
    else:
        if res.status_code == 302:
            res.close()
            return res.headers["Location"]

        elif res.status_code == 200:

            return res.text


def offer_test(track_url, area, appid):
    username = 'lum-customer-hl_f5b348f3-zone-static-route_err-block'
    password = 'i1cmrkiwpbwu'
    port = 22225
    session_id = random.random()
    super_proxy_url = ('http://%s-country-%s-session-%s:%s@zproxy.lum-superproxy.io:%d' %
                       (username, area, session_id, password, port))
    track_url2 = track_url

    while True:
        try:

            if track_url.find('www.google.com') > -1:
                print("country:%s--track_link:%s--app_id:%s--失败" % (area, track_url2, appid))
                return "失败"
            if track_url.find('ttp') > -1 and track_url.find('apple.com') == -1 and track_url.find(
                    'app.appsflyer.com/id') == -1:
                track_url = get_redirect_url(track_url, super_proxy_url)
            else:
                if track_url.find(appid) > -1:

                    print("country:%s--track_link:%s--app_id:%s--成功" % (area, track_url2, appid))
                    return "成功"
                else:
                    print("country:%s--track_link:%s--app_id:%s--失败" % (area, track_url2, appid))
                    return "失败"
                break

        except AttributeError as  e:
            return "失败"
            pass
        except requests.exceptions.InvalidSchema as  e:
            return "失败"
            pass


def test_url(track, country, appid, q):
    res = offer_test(track, country, appid)
    q.put(res)
    return res


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

    res = soup.find_all(type="text", class_="col-xs-10 col-sm-9")
    for k in res:
        try:
            if k["name"] == "packageName":
                res_id = k["value"]
            if k["name"] == "trackUrl":
                res_trackUrl = k["value"]
        except KeyError as e:
            res_offer_id = k["value"]
    print("[" + offerid + "]packageName：" + res_id + "\n" + "[" + offerid + "]trackUrl：" + res_trackUrl + "\n" + "[" + offerid + "]offer_id:" + res_offer_id)

    if country != None:

        q_1 = queue.Queue()
        q_2 = queue.Queue()
        q_3 = queue.Queue()
        q_4 = queue.Queue()
        q_5 = queue.Queue()
        track_res = []
        thread_list = []
        thread_1 = threading.Thread(name="thread_1", target=test_url, args=(res_trackUrl, country, res_id, q_1,))
        thread_list.append(thread_1)
        thread_2 = threading.Thread(name="thread_1", target=test_url, args=(res_trackUrl, country, res_id, q_2,))
        thread_list.append(thread_2)
        thread_3 = threading.Thread(name="thread_1", target=test_url, args=(res_trackUrl, country, res_id, q_3,))
        thread_list.append(thread_3)
        thread_4 = threading.Thread(name="thread_1", target=test_url, args=(res_trackUrl, country, res_id, q_4,))
        thread_list.append(thread_4)
        thread_5 = threading.Thread(name="thread_1", target=test_url, args=(res_trackUrl, country, res_id, q_5,))
        thread_list.append(thread_5)

        thread_1.start()
        thread_2.start()
        thread_3.start()
        thread_4.start()
        thread_5.start()

        for t in thread_list:
            t.join()

        track_res.append(q_1.get())
        track_res.append(q_2.get())
        track_res.append(q_3.get())
        track_res.append(q_4.get())
        track_res.append(q_5.get())

        return res_id, res_offer_id, track_res[0], track_res[1], track_res[2], track_res[3], track_res[4],
    return res_id, res_offer_id, "", "", "", "", ""


def check_begin(cookie, offer_id, num):
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
    res = check_offer(ua, cookie, offer_id)
    x = 10
    while x > 0:
        if write_excel(0, num, 2, res[1]) == 0:
            break
        else:
            time.sleep(2)

    x = 10
    while x > 0:
        if write_excel(0, num, 3, res[2]) == 0:
            break
        else:
            time.sleep(2)

    x = 10
    while x > 0:
        if write_excel(0, num, 4, res[3]) == 0:
            break
        else:
            time.sleep(2)

    x = 10
    while x > 0:
        if write_excel(0, num, 5, res[4]) == 0:
            break
        else:
            time.sleep(2)

    x = 10
    while x > 0:
        if write_excel(0, num, 6, res[5]) == 0:
            break
        else:
            time.sleep(2)

    x = 10
    while x > 0:
        if write_excel(0, num, 7, res[6]) == 0:
            break
        else:
            time.sleep(2)


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
    res = response.cookies.get_dict()['JSESSIONID']
    return "JSESSIONID=" + res


if __name__ == '__main__':
    cookie = get_cookie()
    list_offer_id = read_cols_excel(0, 1)
    num = 0
    for key in list_offer_id:
        threading.Thread(target=check_begin, args=(cookie, list_offer_id[num], num,)).start()
        time.sleep(2)
        num = num + 1
