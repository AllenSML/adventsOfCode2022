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
pos2side = dict()

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
print("part1:", res)

# this solution is inspired by https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day22p2.py
r = 0
c = 0
moveR = 0
directions = deque("ESWN")
direction = directions[0]
moveR, moveC = di2move[directions[0]]

for x, y in re.findall(r"(\d+)([RL]?)", path):
    x = int(x)
    for _ in range(x):
        direction_ = direction
        moveR, moveC = di2move[direction]
        nextRow = r + moveR
        nextCol = c + moveC
        if (nextRow,nextCol) not in tiles:
            if nextRow < 0 and 50 <= nextCol < 100 and direction == "N":
                direction = "E"
                nextRow, nextCol = nextCol + 100, 0
            elif nextCol < 0 and 150 <= nextRow < 200 and direction == "W":
                direction = "S"
                nextRow, nextCol = 0, nextRow - 100
            elif nextRow < 0 and 100 <= nextCol < 150 and direction == "N":
                nextRow, nextCol = 199, nextCol - 100
            elif nextRow >= 200 and 0 <= nextCol < 50 and direction == "S":    
                nextRow, nextCol = 0, nextCol + 100
            elif nextCol >= 150 and 0 <= nextRow < 50 and direction == "E":
                direction = "W"
                nextRow, nextCol = 149 - nextRow, 99
            elif nextCol == 100 and 100 <= nextRow < 150 and direction == "E":
                direction = "W"
                nextRow, nextCol = 149 - nextRow, 149
            elif nextRow == 50 and 100 <= nextCol < 150 and direction == "S":
                direction = "W"
                nextRow, nextCol = nextCol - 50, 99
            elif nextCol == 100 and 50 <= nextRow < 100 and direction == "E":
                direction = "N"
                nextRow, nextCol = 49, nextRow + 50
            elif nextRow == 150 and 50 <= nextCol < 100 and direction == "S":
                direction = "W"
                nextRow, nextCol = nextCol + 100, 49
            elif nextCol == 50 and 150 <= nextRow < 200 and direction == "E":
                direction = "N"
                nextRow, nextCol = 149, nextRow - 100
            elif nextRow == 99 and 0 <= nextCol < 50 and direction == "N":
                direction = "E"
                nextRow, nextCol = nextCol + 50, 50
            elif nextCol == 49 and 50 <= nextRow < 100 and direction == "W":
                direction = "S"
                nextRow, nextCol = 100, nextRow - 50
            elif nextCol == 49 and 0 <= nextRow < 50 and direction == "W":
                direction = "E"
                nextRow, nextCol = 149 - nextRow, 0
            elif nextCol < 0 and 100 <= nextRow < 150 and direction == "W":
                direction = "E"
                nextRow, nextCol = 149 - nextRow, 50

        if (nextRow, nextCol) in tiles:
            if lines[nextRow][nextCol] == "#":
                direction = direction_
                break
        r = nextRow
        c = nextCol
    
    while directions[0] != direction:
        directions.rotate()
    
    directions.rotate(-1 if y == "R" else 1 if y== "L" else 0)
    direction = directions[0]    

print("part2:",1000 * (r + 1) + 4 * (c + 1) + di2Score[direction] )