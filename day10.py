import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input10.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")

X, round = 1, 0
r2x = dict()
for line in lines:
    parts = line.split()
    op, val = None, 0
    if len(parts) == 2:
        op, val =  parts
        val = int(val)
    elif len(parts) == 1:
        op = parts[0]
    if op == "noop":    
        round += 1
        r2x[round] = X
    elif op == "addx":
        r2x[round+1] = X
        r2x[round+2] = X
        round += 2
        X += val
res = 0 
for i in range(20,round+1,40):
        res += i*r2x[i]

print("part1:", res)

r2x[0] = 1
round = 1
for row in range(6):
    image = ""
    for id in range(40):        
        if r2x[round]-1 <= id <= r2x[round]+1:
            image += '#'
        else:
            image += ' '
        round += 1
        id += 1
    print(image)
