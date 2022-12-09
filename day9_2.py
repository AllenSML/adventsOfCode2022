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
    # else:
    elif abs(hy-ty) == 1:
        ty = hy
        tx +=  1 if hx > tx else -1
    else:
        ty +=  1 if hy > ty else -1
        tx +=  1 if hx > tx else -1
    return tx, ty


nodes = dict(enumerate([(0,0) for _ in range(10)]))
n2pos = defaultdict(set)
for k, v in nodes.items():
    n2pos[k].add(v)

rounds = 0
for line in lines:

    di, steps = line.split()
    steps = int(steps)
    cx, cy = di2Cord[di]
 
    for _ in range(steps):
        hx += cx
        hy += cy
        nodes[0] = (hx,hy)
        n2pos[0].add(nodes[k])
        rounds +=1

        for k, v in nodes.items():
            if k == 0: continue
            
            cur_x, cur_y  = v
            pre_x, pre_y = nodes[k-1]
            cur_x, cur_y = calculate_pos(cur_x, cur_y, pre_x, pre_y)
            nodes[k] = (cur_x, cur_y)
            n2pos[k].add(nodes[k])

print("Part2: ", len(n2pos[9]))
