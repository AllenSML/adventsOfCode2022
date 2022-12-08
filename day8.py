import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input8.txt"
input = open(str(cur_dir)+file_name).read().split("\n")
lines = [[int(c) for c in l] for l in input]
print(lines)

res = 0
m, n = len(lines), len(lines[0])
lines_transpose = np.array(lines).transpose()

for x in range(1, m-1):
    for y in range(1, n-1):
        left = lines[x][:y]
        right = lines[x][y+1:]
        top = lines_transpose[y][:x]
        bottom = lines_transpose[y][x+1:]
        res += len(set( (x,y) for line in [left, right, top, bottom] if lines[x][y] > max(line) ))
        
print("part1: ",res+ m+m+2*(n-2))

res = float("-inf")
for x in range(1, m-1):
    for y in range(1, n-1):
        left = lines[x][:y][::-1]
        right = lines[x][y+1:]
        top = lines_transpose[y][:x][::-1]        
        bottom = lines_transpose[y][x+1:]
        score = 1
        for line in [left, right, top, bottom]:
            if max(line) < lines[x][y]:
                score *= len(line)
            else:
                for  i, v in enumerate(line):
                    if v >= lines[x][y]:
                        score *= (i+1)
                        break
        res = max(res, score)
             

print("part2: ", res)


