#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 12:19
# @Author  : ox400
# @Email   : ox01024@163.com
# @File    : create_proxies.py

def create_proxies(proxy):
    proxies={
        "http": "http://"+proxy,
        "https": "https://"+proxy
    }
    return proxies