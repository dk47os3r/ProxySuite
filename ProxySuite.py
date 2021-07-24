#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 22:11
# @Author  : ox400
# @Email   : ox01024@163.com
# @File    : ProxySuite.py
import requests
from lib.spider.spider_main import porxy_list
from lib.core.proxy_test import proxy_survivalDetection

def Test_Proxy(proxylist):
        proxy_survivalDetection(proxylist)


if __name__ == '__main__':
    Test_Proxy(porxy_list())

