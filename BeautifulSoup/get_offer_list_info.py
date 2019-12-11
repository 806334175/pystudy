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
import json

from requests_toolbelt import MultipartEncoder

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


def getpage(token, size):
    page_session = requests.session()
    page_res = page_session.get("http://apibb.tbnetwork.im/v2/offer/pull?token=" + token + "&size=" + size)
    page_j = json.loads(page_res.text)
    page = int(page_j["total_pages"])
    return page


def getinfolistbypage(token, page, size):
    session = requests.session()
    res = session.get("http://apibb.tbnetwork.im/v2/offer/pull?token=" + token + "&size=" + size + "&page=" + str(page))
    j = json.loads(res.text)
    data = j["data"]
    for i in data:
        list_app_name.append(i["app_name"])
        list_app_pack_name.append(i["app_pack_name"])
        list_cap_daily.append(i["cap_daily"])
        list_click_url.append(i["click_url"])
        list_countries.append(i["countries"])
        list_id.append(i["id"])
        list_os.append(i["os"])
        list_payout.append(i["payout"])
        list_preview_url.append(i["preview_url"])


if __name__ == '__main__':

    token = "c09086a9d4004648a96097e282598d75"
    size = "1000"

    list_app_name = []
    list_app_pack_name = []
    list_cap_daily = []
    list_click_url = []
    list_countries = []
    list_id = []
    list_os = []
    list_payout = []
    list_preview_url = []

    for i in range(getpage(token, size)):
        getinfolistbypage(token, i + 1, size)

    num = 1
    rb = xlrd.open_workbook(filename=file)
    wb = copy.copy(rb)
    sheet1 = wb.get_sheet(0)

    for i in list_id:
        sheet1.write(num, 0, list_id[num - 1])
        sheet1.write(num, 1, list_app_name[num - 1])
        sheet1.write(num, 2, list_app_pack_name[num - 1])
        sheet1.write(num, 3, list_payout[num - 1])
        sheet1.write(num, 4, list_cap_daily[num - 1])
        sheet1.write(num, 5, list_countries[num - 1])
        sheet1.write(num, 6, list_os[num - 1])
        sheet1.write(num, 7, list_preview_url[num - 1])
        sheet1.write(num, 8, list_click_url[num - 1])
        num += 1

os.remove(file)
wb.save(file)
