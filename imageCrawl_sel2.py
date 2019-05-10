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


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


baseurl = 'https://unsplash.com/collections/1112424/portraits'


directory = os.getcwd()
driver = webdriver.Chrome('chromedriver',options=options)
driver.implicitly_wait(3)
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
        time.sleep(10)
        
print('scroll complete')

savePath = '../gdrive/My Drive/CycleGan/face/facePics_re/'
elements = driver.find_elements_by_xpath('//*[@id="app"]/div/div[6]/div[1]/div/div/div[*]/figure[*]/div/a')

errcnt = 0
succnt = 0
for i in range(len(elements)):
    try:
        link = elements[i].get_attribute('href')
        tmpWindow = webdriver.Chrome('chromedriver',options=options)
        time.sleep(0.2)
        tmpWindow.get(link)
        print('window'+str(i)+' open')
        pic = tmpWindow.find_elements_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/div[3]/div/div/button/div[2]/img')
        href = pic[0].get_attribute('src')
        urllib.request.urlretrieve(href,savePath+str(i)+'.jpg')
        tmpWindow.close()
        succnt += 1
    except:
        errcnt += 1
        

print('success : ' + str(succnt) +', ' + 'error : ' + str(errcnt))


