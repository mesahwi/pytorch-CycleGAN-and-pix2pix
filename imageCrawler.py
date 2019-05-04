#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 11:52:18 2019

@author: allesgut
"""

import urllib.request
import requests
from bs4 import BeautifulSoup


def base_spider(url):
    # page = 1
    urlLen = len(url)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    

    hrefList = []
    for link in soup.findAll('a'):
        href = link.get('href')
        if href.endswith('.jpg'):
            hrefList.append(url + href)
    return hrefList, urlLen


address = 'https://archive.org/download/Van.gogh.paintings/Nuenen%20%281883-85%29/'
[hList, urlLen] = base_spider(address)
#i=1
for url in hList:
    title = url[urlLen:]
    title = title.replace('%20','_')
    #title = title.replace('%2C', ',')
    print('title : '+title)
    urllib.request.urlretrieve(url, '/Users/allesgut/Desktop/Main/1.courses/2019-1/AI/CycleGan/vanGogh/crawl/'+title)
    #i+=1

print('Complete !')