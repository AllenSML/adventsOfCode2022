import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input15.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")

s2dis = dict()
beacons = set()

max_x = float("-inf")
min_x = float("inf")
max_y = float("-inf")
min_y = float("inf")

for line in lines:
    sx,sy, bx, by = list(map(int,re.findall(r"\-?\d+", line)))
    max_x = max(max_x, sx, bx)
    min_x = min(min_x, sx, bx)
    min_y = min(min_y, sy, by)
    max_y = max(max_y, sy, by)
    beacons.add((bx,by))
    s2dis[(sx,sy)] = abs(sx-bx) + abs(sy-by)

count = 0 
row = 2000000
loggest_distance = max(s2dis.values())

for col in range(min_x-loggest_distance, max_x+loggest_distance+1):
    if (col,row)  in beacons: continue
    for (x,y), dis in s2dis.items():
        dis_ = abs(row-y) + abs(col-x)
        if dis_ <= dis:
            count += 1
            break
    
print("count:", count)

    



