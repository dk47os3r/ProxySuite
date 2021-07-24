#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 12:27
# @Author  : ox400
# @Email   : ox01024@163.com
# @File    : spider_main.py
from lib.spider.porxySpider import  ip66,ip89

def porxy_list():
    list=[]
    list+=ip66()
    list+=ip89()
    print(f'[+] 共获取代理ip{len(list)}个' )
    return list