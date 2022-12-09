import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input9.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")
hx, hy, tx, ty = 0,0,0,0
di2Cord = dict(zip("RLUD", [(0,1),(0,-1), (1,0),(-1,0)]))

def neighbours(i,j):
    neighbours = [
        (i+1,j),
        (i-1,j),
        (i,j+1),
        (i,j-1),
        (i+1,j+1),
        (i+1,j-1),
        (i-1,j+1),
        (i-1,j-1),
        (i,j),
    ]
    return [n for n in neighbours]
seen = set()
seen.add((0,0))

def calculate_pos(tx,ty, hx,hy):
    if (tx,ty) in neighbours(hx,hy):
        pass
    elif hx== tx:
        ty +=  1 if hy > ty else -1
    elif hy == ty:
        tx +=  1 if hx > tx else -1
    elif abs(hx-tx) == 1:
        tx = hx
        ty +=  1 if hy > ty else -1
    elif abs(hy-ty) == 1:
        ty = hy
        tx +=  1 if hx > tx else -1
    return tx, ty 

for line in lines:

    di, steps = line.split()
    steps = int(steps)
    cx, cy = di2Cord[di]
 
    for _ in range(steps):
        hx += cx
        hy += cy
        tx, ty = calculate_pos(tx,ty, hx,hy)
      
        seen.add((tx, ty))
print(len(seen))