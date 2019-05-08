#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:59:35 2019

@author: allesgut
"""

#for colab
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
!pip install selenium

from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
import os, time
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


nameList = []
baseurl0 = 'https://www.wikiart.org/en/pierre-auguste-renoir/' 
baseurl = baseurl0 + 'all-works/#!#filterName:Genre_portrait,resultType:text'

prefix = 'https://uploads0.wikiart.org/images/pierre-auguste-renoir/'
suffix = '.jpg'

savePath = '../gdrive/My Drive/CycleGan/face/Renoir/'

directory = os.getcwd()
driver = webdriver.Chrome('chromedriver',options=options)
driver.implicitly_wait(3)
driver.get(baseurl)


loadMore = driver.find_elements_by_xpath('/html/body/div[2]/div[1]/section/main/div[2]/div[3]/div[3]/a')

time.sleep(2)
while True:
    if 'hide' not in loadMore[0].get_attribute('class'):
        time.sleep(2)
        loadMore[0].click()
        time.sleep(2)
    else:
        print('all loaded. proceeding...')
        break

hList = []
totalLen = len(driver.find_elements_by_class_name('painting-list-text-row'))
base0Len = len(baseurl0)
element = driver.find_elements_by_xpath('/html/body/div[2]/div[1]/section/main/div[2]/div[3]/div[2]/div/div/ul/li/a[1]')
for i in range(len(element)):
    title = element[i].get_attribute('href')
    title = title[base0Len:]
    href = prefix + title + suffix
    print(title)
    urllib.request.urlretrieve(href, savePath + title + '.jpg')

    #girl reading; i=218
    
