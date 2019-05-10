#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:30:25 2019

@author: allesgut
"""

import os, os.path
import numpy as np
from shutil import copyfile

dir = '../gdrive/My Drive/CycleGan/face/'
trainADir = '../gdrive/My Drive/CycleGan/face2impression/trainA/'
valADir = '../gdrive/My Drive/CycleGan/face2impression/valA/'
testADir = '../gdrive/My Drive/CycleGan/face2impression/testA/'
trainBDir = '../gdrive/My Drive/CycleGan/face2impression/trainB/'
valBDir = '../gdrive/My Drive/CycleGan/face2impression/valB/'
testBDir = '../gdrive/My Drive/CycleGan/face2impression/testB/'
trainDir = [trainADir, trainBDir]
valDir = [valADir, valBDir]
testDir = [testADir, testBDir]

elementList = os.listdir(dir)
dirList = []
for element in elementList:
    if len(element.split('.')) == 1:
        dirList.append(element)
        
lenList = []
for folder in dirList:
    newDir = dir+folder+'/'
    listAll = os.listdir(newDir)
    if folder=='facePics_re':  #set B
        spec = 1
    else:
        spec = 0
    for pic in listAll:
        if not pic.endswith('.jpg'):
            continue
        
        idx = np.random.choice([0,1,2], p=[0.6,0.2,0.2])
        if idx == 0:
#            os.rename(newDir+pic, trainDir[spec]+pic)
            copyfile(newDir+pic, trainDir[spec]+pic)
        elif idx == 1:
#            os.rename(newDir+pic, valDir[spec]+pic)
            copyfile(newDir+pic, valDir[spec]+pic)
            
        else :
#            os.rename(newDir+pic, testDir[spec]+pic)
            copyfile(newDir+pic, testDir[spec]+pic)

print('files are arranged!')
