#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:54:28 2019

@author: allesgut
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:59:35 2019

@author: allesgut
"""
import sys
import urllib.request
from selenium import webdriver
import os, time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


baseurl = 'https://www.pexels.com/search/face/'

directory = os.getcwd()
driver = webdriver.Chrome('chromedriver',options=options)
driver.implicitly_wait(3)
driver.get(baseurl)
height = driver.execute_script("return document.body.scrollHeight")
time.sleep(2)

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)
    newHeight = driver.execute_script("return document.body.scrollHeight")
    if height != newHeight:
        height = driver.execute_script("return document.body.scrollHeight")
    else:
        break
    
    
print('scrolling complete')

savePath = '../gdrive/My Drive/CycleGan/face/facePics/'
elements = driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div[*]/article/a[1]/img')

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

for i in range(len(elements)):
    href = elements[i].get_attribute('srcset').split(' ')[0]
    urllib.request.urlretrieve(href,savePath+str(i)+'.jpg')

