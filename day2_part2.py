#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 22:25:35 2022

@author: donal
"""
import os
import numpy as np
import pandas as pd

rootFolder = "/mnt/Data/Tresorit/Puzzles+Games/Advent of Code 2022"

# inputData = []

# inputData = pd.DataFrame(np.array([["A", "Y"], ["B", "X"], ["C", "Z"]]))

inputData = pd.read_csv(os.path.join(rootFolder, "day_2_input.txt"), delimiter=" ", header=None)
inputData.columns = ["Op", "Result"]
inputData.sort_values(["Op", "Result"], inplace=True)
inputData.reset_index(drop=True, inplace=True)


opponentPlays = ['A', 'B', 'C']
results = {'X':'Loss', 'Y':'Draw', 'Z':'Win'}

resultList = {"AX":"S", "AY":"R", "AZ":"P", "BX":"R", "BY":"P", "BZ":"S", "CX":"P", "CY":"S", "CZ":"R"}

itemScoresOpponent = {'A':1, 'B':2, 'C':3}
itemScoresMe = {'R':1, 'P':2, 'S':3}

gameScores = {'Win':6, 'Draw':3, 'Loss':0}

outcomes  = []
outcomeScores = []
mePlays = []
meScores = []

for i in range(0, inputData.shape[0]):
    resultTemp = results[inputData.Result[i]]
    outcomes.append(resultTemp)
    outcomeScores.append(gameScores[resultTemp])
    
inputData["Outcomes"] = outcomes
inputData["OutcomeScores"] = outcomeScores
inputData["Rounds"] = inputData.Op + inputData.Result

for game in inputData.Rounds:
    me = resultList[game]
    meScore = itemScoresMe[me]
    
    mePlays.append(me)
    meScores.append(meScore)
    
inputData["Me"] = mePlays
inputData["MeScores"] = meScores

inputData["TotalScore"] = inputData.MeScores + inputData.OutcomeScores

totalScore = inputData.TotalScore.sum()
print(totalScore)