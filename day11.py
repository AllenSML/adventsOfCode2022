import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input11.txt"
inputs = open(str(cur_dir)+file_name).read().split("\n\n")


m2i = defaultdict(list)
m2o = defaultdict(str)
m2d = dict()
m2next = defaultdict(list)

for id, input  in enumerate(inputs):   
    lines = input.split("\n")
    for index, line in enumerate(lines[1:]):
        if index == 0:
            match = re.findall(r'[0-9]+', line)        
            m2i[id].extend([int(num) for num in re.findall(r'\d+', line)])
        elif index == 1:
            m2o[id] = line.split("=")[-1].strip()
            # print(m2o)
        elif index == 2:
            m2d[id] = int(line.split()[-1])
        else:
            m2next[id] = [int(line.split()[-1])] + m2next[id]

multi = 1
for v in m2d.values():
    multi *= v

m2res = defaultdict(int)

for _ in range(10000):
    for id in m2i.keys():
        for __ in range(len(m2i[id])):
            m2res[id] += 1
            item = m2i[id].pop()
            old = item
            new = eval(m2o[id]) #// 3
            new %= multi  #for part2 only      
            divisible = new % m2d[id] == 0
            id_next = m2next[id][divisible]  
            m2i[id_next].append(new)

res = 1
for times in list(sorted(m2res.values()))[-2:]:
    res *= times    

print(res)


