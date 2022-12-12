#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 20:40:18 2022

@author: donal
"""
import os
import numpy as np
import pandas as pd

rootFolder = "/mnt/Data/Tresorit/Puzzles+Games/Advent of Code 2022"
inputFileName = "day_4_input.txt"

inputFile = open(os.path.join(rootFolder, inputFileName),'r')
inputData = pd.read_csv(inputFile, header=None)
inputData.columns = ["Elf1", "Elf2"]

inputData[["E1S", "E1E"]] = inputData.Elf1.str.split("-", expand=True).astype(int)
inputData[["E2S", "E2E"]] = inputData.Elf2.str.split("-", expand=True).astype(int)

# Logical tests
# Elf 1 contains Elf 2: E1S < E2S & E1E > E2E
overlaps1 = inputData[(inputData.E1E <= inputData.E2E) & (inputData.E1S >= inputData.E2S)].index
# Elf 2 contains Elf 1: E1S > E2S & E1E < E2E
overlaps2 = inputData[(inputData.E1E >= inputData.E2E) & (inputData.E1S <= inputData.E2S)].index

totalOverlaps = np.union1d(overlaps1, overlaps2).shape[0]
print(totalOverlaps)

overlapIndex = []

for i in inputData.index:
    overlap1 = np.intersect1d(range(inputData.E1S[i], (inputData.E1E[i] + 1)),
                              range(inputData.E2S[i], (inputData.E2E[i] + 1)))
    if overlap1.size != 0:
        overlapIndex.append(i)

totalOverlaps2 = len(overlapIndex)
    
print(totalOverlaps2)