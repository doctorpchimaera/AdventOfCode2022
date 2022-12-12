#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 22:05:58 2022

@author: donal
"""
import os
import numpy as np
import pandas as pd
import re

rootFolder = "/mnt/Data/Tresorit/Puzzles+Games/Advent of Code 2022"
inputFileName = "day_5_input.txt"

inputData = []

inputFile = open(os.path.join(rootFolder, inputFileName),'r')
inputData = inputFile.read()
inputFile.close()

[crateStart, moves] = inputData.split("\n\n")

crateStart = crateStart.split("\n")
moves = moves.split("\n")

moves = pd.DataFrame(moves)

moves = moves.iloc[:, 0].str.split(" ", expand=True).iloc[:, [1, 3, 5]].astype(int)
moves.columns = ["Qty", "From", "To"]

crateStackNum = int((len(crateStart[0]) + 1) / 4)
crateStacks = []

for i in range(0, (len(crateStart) - 1)):
    crateLine = crateStart[i]
    crateStack = []
    for j in range(0, crateStackNum):
        crateIndex = (4 * j) + 1
        crateStack.append(crateLine[crateIndex])
        
    crateStacks.append(crateStack)
    
crateStacks = np.flipud(np.array(crateStacks))

crateStackFinal = []

for i in range(0, crateStackNum):
    crateIndex = np.where(crateStacks[:, i] != ' ')[0]
    crateStackFinal.append(crateStacks[crateIndex, i].tolist())    
    
"""
Time to start moving crates around

Bottom of crate stack is first item of stack list, top is last

Moves are from top to top, and only one crate moved at a time - multiple crates moved will invert the stack
"""
for i in moves.index:
    numMoves = moves.Qty[i]
    fromStack = moves.From[i] - 1
    toStack = moves.To[i] - 1
    
    for n in range(0, numMoves):        
        crateStackFinal[toStack].append(crateStackFinal[fromStack].pop())

result = ""
        
for finalStack in crateStackFinal:
    result = result + finalStack[-1]

print(result)