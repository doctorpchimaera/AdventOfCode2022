#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 22:25:35 2022

@author: donal
"""
import os
import numpy as np

rootFolder = "/mnt/Data/Tresorit/Puzzles+Games/Advent of Code 2022"

inputData = []

inputFile = open(os.path.join(rootFolder, "day_2_input.txt"),'r')
for line in inputFile:
    inputData.append(line.replace('\n', '').replace(' ', ''))    
inputFile.close()

opponent = ['A', 'B', 'C']
me = ['X', 'Y', 'Z']
itemScoresOpponent = {'A':1, 'B':2, 'C':3}
itemScoresMe = {'X':1, 'Y':2, 'Z':3}

gameScores = {'Win':6, 'Draw':3, 'Loss':0}

outcomes = {}

# matchValue ranges are computed externally for win/draw/lose and those results used to classify the pairings as they're processed here
for opMove in opponent:
    opItemScore = itemScoresOpponent[opMove]
    for meMove in me:
        meItemScore = itemScoresMe[meMove]
        match = opMove + meMove
        matchValue = (opItemScore ** 2) * meItemScore
        if matchValue in [1, 8, 27]:
            gameScore = gameScores['Draw']
        elif matchValue in [3, 4, 18]:
            gameScore = gameScores['Loss']
        elif matchValue in [2, 9, 12]:
            gameScore = gameScores['Win']
        
        roundScore = meItemScore + gameScore
            
        outcomes[match] = roundScore

gameList = np.array(inputData)

totalScore = 0
for game in gameList:
        totalScore = totalScore + outcomes[game]

print(totalScore)