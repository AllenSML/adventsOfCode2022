import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input25.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")

sums = 0
for line in lines:    
    multi = 1
    for c in line[::-1]:
        num = 0
        if c == "-":
            num = -1
        elif c == "=":
            num = -2
        else:
            num = int(c)
        sums += num * multi
        multi *=5

input = sums
i = 1
res =  ""
while input > 0:    
    input, mod = divmod(input, 5)
    if mod < 3:
        cur = str(mod)
    elif mod == 3:
        cur  = str("=")
        input += 1
    elif mod == 4:
        cur  = str("-")
        input += 1    
    res = cur + res 
print("part1:", res)
