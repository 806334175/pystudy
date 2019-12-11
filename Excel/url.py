import random
import requests


def get_redirect_url(track_url,super_proxy_url):
    # 重定向前的链接
    url=track_url
    super_proxy_url=super_proxy_url

    headers = {
      'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1'
    }

    # 请求网页

    proxies = {"http":super_proxy_url,
               "https": super_proxy_url,

               }

    response = requests.get(url, proxies=proxies, headers=headers, allow_redirects=False)
    print(proxies["https"])
    print(response.text)  # 打印重定向后的网址
    print(response.status_code)
    # 打印响应的状态码

    # 返回重定向后的网址
    if response.status_code==302:
        return response.headers["Location"]
    else:
        return "失败"




def offer_test(track_url,area, appid):
    track_url = track_url
    area = area
    appid = appid
    username = 'lum-customer-hl_f5b348f3-zone-static-route_err-block'
    password = 'i1cmrkiwpbwu'
    port = 22225
    session_id = random.random()
    super_proxy_url = ('http://%s-country-%s-session-%s:%s@zproxy.lum-superproxy.io:%d' %
                       (username, area, session_id, password, port))

    get_redirect_url("http://lumtest.com/myip.json",super_proxy_url)
    while True:

        print(track_url)
        if track_url.find('ttp') > -1 and track_url.find('itunes') == -1:
            # print(bb.find('ttp'))
            track_url = get_redirect_url(track_url,super_proxy_url)
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



if __name__ == '__main__':
    track_url="http://clkbb.tbnetwork.im/click?id=2356672&aff=555&ost=1567150020"
    area="jp"
    appid="1155432341"
    offer_test(track_url,area,appid)






