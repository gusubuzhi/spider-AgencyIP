import requests
from lxml import etree
import time
import random

headers = {
        'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWUzYzNkNDE5MjEwOGI3NTU3OWJlYWNlZjFhNjgyMDllBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXdITjUxNXE5MTNCWmMzQVlCaVVzdkExNmlFZytqNUpBWkQ5dW5qckk5b0E9BjsARg%3D%3D--1129f82ee016b2f8c490a18e4a9c0a798dd8be12; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1531106168,1531362172; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1531362189',
        'Host': 'www.xicidaili.com',
        'Referer': 'http://www.xicidaili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

}


def get_ip(offset):
    url = 'http://www.xicidaili.com/nn/%d' %offset
    print(url)
    re = requests.get(url,headers = headers)
    re.encoding = 'utf-8'
    html = re.text
    # print(html)
    ip_items = etree.HTML(html)
    print("---第%d页----" %offset)
    # ip = ip_items.xpath('//*[@id="ip_list"]/tbody/tr/td[2]')
    ip = ip_items.xpath('//table[@id="ip_list"]//tr[@class="odd" or @class=""]/td[2]/text()')
    # print(ip)
    port = ip_items.xpath('//table[@id="ip_list"]//tr[@class="odd" or @class=""]/td[3]/text()')
    # print(port)
    l = []
    for n in range(len(ip)):
        ip_port = ip[n]+':'+port[n]
        l.append(ip_port)
        # print(ip_port)
    return l

def check_ip(l):
    # time.sleep(1)
    headers = {
        'Cookie': 'cye=shenzhen; _lxsdk_cuid=1646d5d66d76-0325cb2d24f0d4-47e1039-1fa400-1646d5d66d9c8; _lxsdk=1646d5d66d76-0325cb2d24f0d4-47e1039-1fa400-1646d5d66d9c8; _hc.v=a8aa2d27-a028-f56e-191c-16e4988bc86b.1530843195; s_ViewType=10; _lx_utm=utm_source%3Dso.com%26utm_medium%3Dorganic; cy=7; _lxsdk_s=1647cc0b6c8-232-c94-410%7C%7C65',
        'Host': 'www.dianping.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Accept-Encoding': 'gzip',

    }
    for i in range(len(l)):
        r = random.choice(l)
        print("正在测试:%s" %r)
        url = "http://www.dianping.com/shenzhen/ch50/g157"
        # url = "http://www.dianping.com/shenzhen/ch50"
        # url = "https://www.baidu.com"
        proxies= {"http":"http://%s" %r}
        try:
            # res = requests.get(url,proxies = proxies,headers = headers)
            res = requests.get(url, proxies=proxies)
        except :
            print("%s--无法连接" %r)
            continue
        # res = requests.get(url, proxies=proxies,timeout = 10)
        if res.status_code == 200:
            print("-------%s :此IP可用-------" %r)
        else:
            print("%s :此IP不可用" % r)

        # L.append(ip)
        # return L
        # continue


if __name__ == "__main__":
    for i in range(5, 7):
        ip = get_ip(i)
        check_ip(ip)
