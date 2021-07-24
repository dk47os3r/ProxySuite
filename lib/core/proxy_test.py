#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 14:07
# @Author  : ox400
# @Email   : ox01024@163.com
# @File    : proxy_test.py
import json
import requests
from multiprocessing.dummy import Pool
from lib.core.create_proxies import create_proxies
ipInfo_api=r'http://whois.pconline.com.cn/ipJson.jsp?json=true&ip='
r_List=[]

def proxy_test(proxy):
    proxies=create_proxies(proxy)
    try:
        r=requests.get(ipInfo_api,timeout=2,proxies=proxies)
        ipinfo=json.loads(r.text)
        print(proxy,ipinfo['addr'])
        r_List.append(proxy+''+ipinfo['addr'])

    except Exception as e:
         print(proxy,'error')


def proxy_survivalDetection(proxylist):
    print('[+] 开始探测代理存活')
    pool=Pool(4)
    pool.map(proxy_test,proxylist)
    print(f'[+] 测试完成存活ip共{len(r_List)}个' )
    for porxy in r_List:
        print(porxy)

