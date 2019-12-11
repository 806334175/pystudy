import os
import random
import requests
import xlwt
import xlrd
import threading
import time
from xlutils import copy

# file = "C:\\Users\\Administrator.DESKTOP-5MLNI1E\\Desktop\\offer.xls"
file = "D:\\offer.xls"

# file = "test.xlsx"


def read_rows_excel(sheet, row):
    wb = xlrd.open_workbook(filename=file)
    sheet1 = wb.sheet_by_index(sheet)
    rows_res = sheet1.row_values(row)
    return rows_res


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
    # 重定向前的链接
    url = track_url
    super_proxy_url = super_proxy_url

    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
    }

    # 请求网页

    proxies = {"http": super_proxy_url,
               "https": super_proxy_url,

               }

    response = requests.get(url, proxies=proxies, headers=headers, allow_redirects=False)
    # print(proxies["https"])
    # print(response.text)  # 打印重定向后的网址
    # print(response.status_code)
    # 打印响应的状态码

    # 返回重定向后的网址
    if response.status_code == 302:
        return response.headers["Location"]
    else:
        return "失败"


def offer_test(track_url, area, appid):
    track_url = track_url
    area = area
    appid = appid
    username = 'lum-customer-hl_f5b348f3-zone-static-route_err-block'
    password = 'i1cmrkiwpbwu'
    port = 22225
    session_id = random.random()
    super_proxy_url = ('http://%s-country-%s-session-%s:%s@zproxy.lum-superproxy.io:%d' %
                       (username, area, session_id, password, port))

    get_redirect_url("http://lumtest.com/myip.json", super_proxy_url)

    while True:

        # print(track_url)
        if track_url.find('ttp') > -1 and track_url.find('apple.com') == -1:
            # print(bb.find('ttp'))
            track_url = get_redirect_url(track_url, super_proxy_url)
        # print("继续跳转")

        else:
            print("跳转完成")
            if track_url.find(appid) > -1:
                print("跳转成功,找到APP")
                return "成功"
            else:
                print("跳转失败,非指定APP")
                return "失败"
            break


def test_url(xxx):
    list_track = read_cols_excel(0, 0)
    list_county = read_cols_excel(0, 1)
    list_appid = read_cols_excel(0, 2)

    num = 0
    for key in list_track:
        res = offer_test(list_track[num], list_county[num], list_appid[num])

        x = 10
        while x > 0:
            if write_excel(0, num, xxx + 3, res) == 0:
                break
            else:
                time.sleep(2)

        num = num + 1
    pass


if __name__ == '__main__':

    threads = []

    t1 = threading.Thread(target=test_url, args=(0,))
    threads.append(t1)
    t2 = threading.Thread(target=test_url, args=(1,))
    threads.append(t2)
    t3 = threading.Thread(target=test_url, args=(2,))
    threads.append(t3)
    t4 = threading.Thread(target=test_url, args=(3,))
    threads.append(t4)
    t5 = threading.Thread(target=test_url, args=(4,))
    threads.append(t5)
    # t6 = threading.Thread(target=test_url, args=(5,))
    # t7 = threading.Thread(target=test_url, args=(6,))
    # t8 = threading.Thread(target=test_url, args=(7,))
    # t9 = threading.Thread(target=test_url, args=(8,))
    # t10 = threading.Thread(target=test_url, args=(9,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    # t6.start()
    # t7.start()
    # t8.start()
    # t9.start()
    # t10.start()

    for t in threads:
        t.join()

    print("完成")
