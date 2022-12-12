#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 21:59:17 2022

@author: donal
"""
import os
import numpy as np
import pandas as pd
import re
import anytree as at

rootFolder = "/mnt/Data/Tresorit/Puzzles+Games/Advent of Code 2022"
inputFileName = "day_7_input.txt"

inputFile = open(os.path.join(rootFolder, inputFileName),'r')

inputData = []

for line in inputFile:
    inputData.append(line.replace('\n', ''))   
inputFile.close()

name = []
isDir = []
parent = []
size = []

commands = ["cd", "ls"]

nodes = []

nodes.append(at.Node("root", size = 0, nType = "dir"))
lastParent = nodes[0]

deleteDirs = []
deleteTotal = 0

for line in inputData:
    elements = line.split(" ")
    if elements[0] == "$":
        # command
        cmd = elements[1]
        if cmd == "cd":
            target = elements[2]
            # changing directory: up if target is "..", otherwise down
            if target == "..":
                lastParent = lastParent.parent
                continue
            elif target == "/":
                continue
            else: 
                nodes.append(at.Node(target, parent = lastParent, size = 0, nType = "dir"))
                lastParent = nodes[-1]
        elif cmd  == "ls":
            # nothing to do, skip to the next line
            continue
    elif elements[0] == "dir":
        # directory entry
        continue
    else: 
        # file entry
        nodes.append(at.Node(elements[1], parent = lastParent, size = int(elements[0]), nType = "file"))

for node in at.PostOrderIter(nodes[0]):
    if node.nType == "file":
        node.parent.size += node.size

for node in at.PostOrderIter(nodes[0]):
    if node.nType == "dir":
        if node.parent:
            node.parent.size += node.size
            
for node in nodes:
    if node.nType == "dir":
        if node.size <= 100000:
            deleteDirs.append(node)
            deleteTotal += node.size
        
print(at.RenderTree(nodes[0]))
print(deleteTotal)

### Part 2
diskSize = 70000000
diskNeeded = 30000000
diskUsed = nodes[0].size
diskAvailable = diskSize - diskUsed

spaceNeeded = diskNeeded - diskAvailable

nodesForDeletion = []

for node in at.PostOrderIter(nodes[0]):
    if node.nType == "dir":
        if node.size >= spaceNeeded:
            nodesForDeletion.append(node)
    
smallestNode = nodesForDeletion[0]

for node in nodesForDeletion:
    if node.size < smallestNode.size:
        smallestNode = node
        
print(smallestNode.size)