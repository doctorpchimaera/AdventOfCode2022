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
inputFileName = "bigboy5.txt"

inputData = []

inputFile = open(os.path.join(rootFolder, inputFileName),'r')
inputData = inputFile.read()
inputFile.close()

[crateStart, moves] = inputData.split("\n\n")

crateStart = crateStart.split("\n")
moves = moves.split("\n")

moves = pd.DataFrame(moves)

moves = moves.iloc[:, 0].str.split(" ", expand=True).iloc[:, [1, 3, 5]]
moves.columns = ["Qty", "From", "To"]
moves.drop(axis=0, index=(moves.shape[0] - 1), inplace=True)    

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

Moves are from top to top, and multiple crates can move at a time - crate order is preserved during moves
"""
for i in moves.index:
    numMoves = -int(moves.Qty[i])
    fromStack = int(moves.From[i]) - 1
    toStack = int(moves.To[i]) - 1
    
    crateStackFinal[toStack].extend(crateStackFinal[fromStack][numMoves:])
    del crateStackFinal[fromStack][numMoves:]

result = ""
        
for finalStack in crateStackFinal:
    result = result + finalStack[-1]

print(result)