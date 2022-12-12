#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 22:00:02 2022

@author: donal
"""
import os

rootFolder = "/mnt/Data/Tresorit/Puzzles+Games/Advent of Code 2022"

inputFile = open(os.path.join(rootFolder, "puzzle_1_input.txt"),'r')
inputData = inputFile.read()
inputFile.close()

elvesLoad = str.split(inputData, '\n\n')
elfTotalLoad = []

for load in elvesLoad:
    elfLoad = str.split(load, '\n')
    totalCalories = 0
    for calories in elfLoad:
        if calories != '':
            totalCalories = totalCalories + int(calories)
    if totalCalories > 0:
        elfTotalLoad.append(totalCalories)
        
result = max(elfTotalLoad)
print(result)

## puzzle 2 work
elfTotalLoad.sort(reverse=True)
result2 = sum(elfTotalLoad[0:3])
print(result2)