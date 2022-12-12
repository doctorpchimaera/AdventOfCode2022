#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 16:29:06 2022

@author: donal
"""
import os
import numpy as np
# import pandas as pd
# import re
# import anytree as at
import math

rootFolder = "/mnt/Data/Tresorit/Puzzles+Games/Advent of Code 2022"
inputFileName = "day_8_input.txt"

inputFile = open(os.path.join(rootFolder, inputFileName),'r')

inputData = []

for line in inputFile:
    inputData.append(line.replace('\n', ''))   
inputFile.close()

for i in range(0, len(inputData)):
    inputData[i] = list(inputData[i])

inputData = np.array(inputData)
inputData = inputData.astype(int)

numCols = inputData.shape[1]
numRows = inputData.shape[0]

# Set up results array: 1 means a tree is visible, default everything to 0 first
results = np.zeros(inputData.shape)
# Set outer perimeter trees to visible
results[:, 0] = 1
results[:, (numCols - 1)] = 1
results[0, :] = 1
results[(numRows - 1), :] = 1

for row in range(1, (numRows - 1)):
    # go through each row
    for col in range(1, (numCols - 1)):
        rCol = numCols - col - 1
        lMax = max(inputData[row, 0:col])
        rMax = max(inputData[row, (rCol + 1):])
        
        # go across from the left first
        if inputData[row, col] > lMax:
            # this tree is bigger than the ones left of it
            results[row, col] = 1
        
        # go across from the right
        if inputData[row, rCol] > rMax:
            # this tree is bigger than the ones right of it
            results[row, rCol] = 1
    
for col in range(1, (numCols - 1)):
    # go through each column
    for row in range(1, (numRows - 1)):
        bRow = numRows - row - 1
        tMax = max(inputData[0:row, col])
        bMax = max(inputData[(bRow + 1):, col])
        
        # go down from the top first
        if inputData[row, col] > tMax:
            # this tree is bigger than the ones above it
            results[row, col] = 1
            
        if inputData[bRow, col] > bMax:
            # this tree is bigger than the ones below it
            results[bRow, col] = 1
            
print("Visible Trees: {}".format(results.sum()))

### Part 2
scenicScore = np.zeros(inputData.shape)

for row in range(1, (numRows - 1)):
    # print(inputData[row, :])
    for col in range(1, (numCols - 1)):
        tree = inputData[row, col]

        leftTaller = np.where(inputData[row, 0:col] >= tree)[0] # should it be > instead of >=?
        rightTaller = np.where(inputData[row, (col + 1):] >= tree)[0] + (col + 1)
        
        # print("Row {} Col {}".format(row, col))
        # print("Tree {} leftTaller {}, rightTaller {}".format(tree, leftTaller, rightTaller))
        
        if leftTaller.size != 0:
            lScenic = col - max(leftTaller) 
        else:
            lScenic = col
            
        if rightTaller.size != 0:
            rScenic = min(rightTaller) - col
        else: 
            rScenic = numCols - col - 1
            
        # print("lScenic {}, rScenic {}\n".format(lScenic, rScenic))
        scenicScore[row, col] = rScenic * lScenic
        
for col in range(1, (numCols - 1)):
    for row in range(1, (numRows - 1)):
        tree = inputData[row, col]

        topTaller = np.where(inputData[0:row, col] >= tree)[0]
        bottomTaller = np.where(inputData[(row + 1):, col] >= tree)[0] + (row + 1)
        
        if topTaller.size != 0:
            tScenic = row - max(topTaller)
        else:
            tScenic = row
            
        if bottomTaller.size != 0:
            bScenic = min(bottomTaller) - row
        else:
            bScenic = numRows - row - 1
            
        scenicScore[row, col] = scenicScore[row, col] * tScenic * bScenic
        
print("Highest Scenic Score: {}".format(np.max(scenicScore)))