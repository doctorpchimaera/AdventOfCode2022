#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 21:08:36 2022

@author: donal
"""
import os
import numpy as np
# import pandas as pd
# import re

rootFolder = "/mnt/Data/Tresorit/Puzzles+Games/Advent of Code 2022"
inputFileName = "day_6_input.txt"

inputFile = open(os.path.join(rootFolder, inputFileName),'r')
inputData = inputFile.read()
inputFile.close()

inputData = list(inputData[0:-1])

# inputData = list("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")

sopIndex = len(inputData) - 4

for i in range(0, sopIndex):
    testString = inputData[i:(i + 4)]
    if len(testString) == np.unique(testString).shape[0]:
        startOfPacket = i + 4
        break    
        
print("Start of Packet: {}".format(startOfPacket))

somIndex = len(inputData) - 14

for i in range(0, somIndex):
    testString = inputData[i:(i + 14)]
    if len(testString) == np.unique(testString).shape[0]:
        startOfMessage = i + 14
        break
    
print("Start of Message: {}".format(startOfMessage))