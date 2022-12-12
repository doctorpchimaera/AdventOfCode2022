#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 19:52:29 2022

@author: donal
"""
import os
import numpy as np
import pandas as pd

rootFolder = "/mnt/Data/Tresorit/Puzzles+Games/Advent of Code 2022"
inputFileName = "day_3_input.txt"

inputData = []

inputFile = open(os.path.join(rootFolder, inputFileName),'r')
for line in inputFile:
    inputData.append(line.replace('\n', ''))    
inputFile.close()

priorityList = {}

for i in range(97, 123):
    priorityList[chr(i)] = i - 96
    
for i in range(65, 91):
    priorityList[chr(i)] = i - 64 + 26

overlaps = []
priorities = []
    
for line in inputData:
    allItems = list(line)
    ruckSackSize = int(len(allItems) / 2)
    contents1 = list(allItems[0:ruckSackSize])
    contents2 = list(allItems[ruckSackSize:])
    
    overlap = np.intersect1d(contents1, contents2)
    
    if overlap.shape[0] > 0:
        overlaps.append(overlap[0])
        priorities.append(priorityList[overlap[0]])
        
print(sum(priorities))

badges = []
badgePriorities = []

for i in range(0, int(len(inputData) / 3)):
    j = 3 * i
    badge = np.intersect1d(
        np.intersect1d(list(inputData[j]), 
                       list(inputData[j + 1])),
        list(inputData[j + 2]))
    if badge.shape[0] > 0:
        badges.append(badge[0])
        badgePriorities.append(priorityList[badge[0]])
    
print(sum(badgePriorities))