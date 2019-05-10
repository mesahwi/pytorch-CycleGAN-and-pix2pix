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

import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, time

baseurl = 'https://unsplash.com/collections/1112424/portraits'


directory = os.getcwd()
driver = webdriver.Chrome(directory+'/chromedriver-2')
driver.get(baseurl)
time.sleep(3)

loadMore = driver.find_elements_by_xpath('//*[@id="app"]/div/div[6]/div[2]/button')
try:
    loadMore[0].click()
except:
    print('yeah.. scroll once more')
    driver.execute_script("window.scrollBy(0, 200);")
    loadMore[0].click() 


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

while True:
    try:
        logo = driver.find_element_by_xpath('//*[@id="app"]/div/div[6]/div[2]/p')
        break
    except:
        time.sleep(30)
        
print('scroll complete')
