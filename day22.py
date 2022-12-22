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
rowBoundary = defaultdict(lambda : [float("inf"), float("-inf")])
colBoundary = defaultdict(lambda : [float("inf"), float("-inf")])

directions = deque("ESWN")
di2Score = dict(zip(directions,[0,1,2,3]))
di2move = dict(zip(directions, ((0,1),(1,0),(0,-1),(-1,0))))

for r, line in enumerate(lines):    
    for c, tile in enumerate(line):
        if tile != " ":
            tiles[(r,c)] = True if tile == "." else False
            rowBoundary[r][0] = min(rowBoundary[r][0], c)
            rowBoundary[r][1] = max(rowBoundary[r][1], c)
            colBoundary[c][0] = min(colBoundary[c][0], r)
            colBoundary[c][1] = max(colBoundary[c][1], r)

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

pos = (0, rowBoundary[0][0])
step = ""

for i, c in enumerate(path):
    if c.isdigit():        
        step += c
    else:        
        pos = move(pos, int(step),directions[0])
        step = ""        
        directions.rotate([1,-1][c == "R"])
else: 
    if c.isdigit():
        pos = move(pos, int(step),directions[0])

res = 1000*(pos[0]+1) + 4*(pos[1]+1) +di2Score[directions[0]]
print(res)



