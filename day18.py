import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input18.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")
lines = [ tuple(map(int, line.split(","))) for line in lines]

def neighbours(x,y,z):
    nbs = [
        (1,0,0),
        (-1,0,0),
        (0,1,0),
        (0,-1,0),
        (0,0,1),
        (0,0,-1)
    ]
    return [ (x+cx,y+cy,z+cz) for cx,cy,cz in nbs]

cubes = set(lines)
res = 0
for x,y,z in lines:    
    for xx, yy, zz in neighbours(x,y,z):
        if (xx,yy,zz) not in cubes:
            res += 1
print("part1: ",res)


min_xyz = [min(cord) for cord in zip(*lines)]
max_xyz = [max(cord) for cord in zip(*lines)]

start = tuple(v-1 for v in min_xyz)
queue = deque() 
queue.append(start)
seen = set()

res = 0
while queue:
    current = queue.pop()
    if current in seen:
        continue
    seen.add(current)

    for x,y,z in neighbours(*current):
        if (x,y,z) in cubes: 
            res += 1
        if (x,y,z) not in cubes and  all(l-1<=m <= r+1 for l,m, r in zip(min_xyz,(x,y,z),max_xyz)):
            queue.appendleft((x,y,z))
        
print("part2: ", res)