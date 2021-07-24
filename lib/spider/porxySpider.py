#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 22:17
# @Author  : ox400
# @Email   : ox01024@163.com
# @File    : porxySpider.py
import re

import requests
# from multiprocessing.dummy import Pool
from lxml import html

def get_html(url):
    '''
    获取页面源码解析并返回html
    :param url: url
    :return:lxml.html.HtmlElement
    '''
    r=requests.get(url).text
    r_html=_html=html.fromstring(r)
    return r_html

def ip66():
    # num=300 #提取数量 最大300
    url=f'http://www.66ip.cn/nmtq.php?getnum=300&isp=0&anonymoustype=4&start=&ports=&export=&ipaddress=&area=1&proxytype=2&api=66ip'
    print('[+] 正在从66ip获取代理地址')
    try:
        r=requests.get(url).text
        print(r)
        list=re.findall('		(.*)<br />',r)
        print(f'[+] 获取到代理ip{len(list)}个')
        return list
    except:
        print('[-] 66ip代理获取出错')

def ip89():
    num=500
    url=f'https://www.89ip.cn/tqdl.html?num={num}&address=&kill_address=&port=&kill_port=&isp='
    print('[+] 正在从89ip获取代理地址')
    try:
        r = requests.get(url).text
        # print(r)
        list=re.findall(r'            (.*)<br>更好用的代理ip',r)
        list=list[0].split('<br>')
        print(f'[+] 获取到代理ip{len(list)}个')
        return list
    except Exception as e:
        print('[-] 89ip代理获取出错',e)









def seofangfa():
    proxy_list=[]
    url='https://seofangfa.com/proxy/'
    html=get_html(url)
    # 初始解析 抓大
    html_xparh=html.xpath(r'//table[@class="table"]/tbody/tr')
    for data in html_xparh:
        all=data.xpath(r'td/text()')
        ip=all[0]
        port=all[1]
        # print(f'{ip}:{port}')
        proxy_list.append(f'{ip}:{port}')
    return proxy_list







if __name__ == '__main__':
    ip66()
