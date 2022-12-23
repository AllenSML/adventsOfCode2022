import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input23.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")

tiles = set()
for x, line in enumerate(lines):
    for  y, tile in enumerate(line):
        if tile == "#":
            tiles.add((x,y))

nNbs = [ (-1,0),(-1,-1),(-1,1)]
sNbs = [ (1,0),(1,-1),(1,1)]
wNbs = [ (0,-1),(-1,-1),(1,-1)]
eNbs = [ (0,1),(-1,1),(1,1)]

nbsQueue = deque([nNbs, sNbs,wNbs, eNbs])
allNbs = functools.reduce(lambda x,y : set(x) | set(y), nbsQueue)

def neighbours(xy, dxy):    
    return [(xy[0]+dx,xy[1]+dy) for dx, dy in dxy]

round = 1
while True:
    nTiles = defaultdict(list)
    for x,y in tiles:        
        if all( (dx,dy) not in tiles for dx, dy in neighbours((x,y), allNbs)):
            nTiles[(x,y)].append((x,y))
            continue        
        for nb in nbsQueue:
            if all ((dx,dy) not in tiles  for dx, dy in neighbours((x,y), nb)):
                nTiles[neighbours((x,y), nb)[0]].append((x,y))
                break                        
        else:
            nTiles[(x,y)].append((x,y))

    nTiles_ = set()
    for k, v in nTiles.items():        
        if len(v) > 1:
            nTiles_ =  nTiles_ | set(v)
        else:
            nTiles_.add(k)
    
    if nTiles_ == tiles:
        print("part2:", round)
        exit()

    tiles = nTiles_
    nbsQueue.rotate(-1)
    if round == 10:        
        maxxy= [ max([t[i] for t in tiles]) for i in range(2)]
        minxy= [ min([t[i] for t in tiles]) for i in range(2)]
        print("part1:", (maxxy[0] - minxy[0]+1) * (maxxy[1] - minxy[1]+1)-len(tiles))
    round +=1