import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input22.txt"
input = open(str(cur_dir)+file_name).read()
lines = input.splitlines()[:-2]
path = input.splitlines()[-1]

tiles = dict()
colRange = defaultdict(list)
rowRange = defaultdict(list)
colBoundary = dict()
rowBoundary = dict()

for r, line in enumerate(lines):    
    for c, tile in enumerate(line):
        if tile != " ":
            tiles[(r,c)] = True if tile == "." else False
            colRange[c].append(r)
            rowRange[r].append(c)
        
rowBoundary = dict( (id, (min(v), max(v))) for id, v in rowRange.items())
colBoundary = dict((id, (min(v), max(v)))  for id, v in colRange.items())


directions = deque("ESWN")
di2Score = dict(zip("ESWN",[0,1,2,3]))
di2move = dict(zip("ESWN", ((0,1),(1,0),(0,-1),(-1,0))))


def move(pos, steps, direction):
    for _ in range(steps):
        nextPos = tuple( x+y for x, y  in zip(di2move[direction],pos))
        if nextPos not in tiles:
            if direction == "E":
                nextPos = (pos[0], rowBoundary[pos[0]][0])
            elif direction == "S":
                nextPos = (colBoundary[pos[1]][0], pos[1])
            elif direction == "W":
                nextPos = (pos[0], rowBoundary[pos[0]][1])
            elif direction == "N":
                nextPos = (colBoundary[pos[1]][1], pos[1])                
        if not tiles[nextPos]:
            nextPos = pos
            return pos
        pos = nextPos
    return pos


direction = directions[0]
pos = (0, rowBoundary[0][0])
step = None

for i, c in enumerate(path):
    if c.isdigit():        
        step = step if step else ""
        step += c
    else:
        if step:
            print(pos, int(step), direction)
            pos = move(pos, int(step),direction)
            step = None        
        if c == "R":
            directions.rotate(-1)
            direction = directions[0]
        elif c == "L":
            directions.rotate(1)
            direction = directions[0]            
else: 
    if c.isdigit():
        print(pos, int(step), direction)
        pos = move(pos, int(step),direction)


r, c = pos
res = 1000*(r+1) + 4*(c+1) +di2Score[direction]
print(res)



