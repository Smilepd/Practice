#coding:utf-8

from bs4 import BeautifulSoup

import requests
import time
import ssl
import os
import  random

#请求代理ip网站链接
def get_url(url):
    url_list = []
    for i in range(1, 2):
        url_new = url + str(i)
        url_list.append(url_new)
    return url_list

#获取网页内容
def get_content(url):
    print ('当前访问地址：' + url)
    user_agent = "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"
    headers = {'User-Agent': user_agent}
    # with open("data3.txt", 'r') as f1:
    #     f2 = f1.readlines()
    #     ip = str(random.choice(f2))
    #     print('当前使用ip：' + ip)
    # proxy = {'http':ip}
    try:
        res = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(res.text, "html5lib")
        return soup
    except Exception as e:
        print (e)
        time.sleep(10)
        get_content(url)


#提取网页中ip地址和端口号信息
def get_info(content):
    all_ips = list()
    ip_list = content.find("table", id="ip_list")
    for tr in ip_list.find_all("tr"):
        info = tr.find_all("td")
        if len(info):
            all_ips.append(info[1].get_text() + ":" + info[2].get_text() + ":" + info[5].get_text())
    return all_ips

#验证代理ip的有效性，有效的保存到data2.txt，无效的直接丢弃
def try_connect(ip) :
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'
    headers = {'User-Agent': user_agent}
    test_ip = ip.split(":")[0] + ":" + ip.split(":")[1]
    proxy = {'http': test_ip}
    print(proxy)
    test_url = "https://www.baidu.com/"

    try:
        res = requests.get(test_url, proxies=proxy, headers=headers, timeout = 10)
        time.sleep(2)
        content = res.status_code
        # print(content)
        if content == 200:
            with open("climb_ip.txt", "a") as fd:
                fd.write(ip)
                fd.write(u"\n")
            print ("true")
        else:
            print ("false")
    except request.URLError as e:
        print (e.reason)
        print("false")


def run():
    url = 'http://www.xicidaili.com/nt/'
    url_list = get_url(url)
    if os.path.exists("climb_ip.txt"):
        os.remove("climb_ip.txt")
    for con_url in url_list:
        content = get_content(con_url)
        all_ips = get_info(content)
        for ip in all_ips:
            try_connect(ip)

if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nt/'
    url_list = get_url(url)
    if os.path.exists("climb_ip.txt"):
        os.remove("climb_ip.txt")
    for con_url in url_list:
        content = get_content(con_url)
        all_ips = get_info(content)
        for ip in all_ips:
            try_connect(ip)

