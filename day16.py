import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input16.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")


G = nx.DiGraph()
startL = "AA"     
label2rate = dict()

for line in lines:
    parts = line.split()
    fromL, rate, toL = parts[1], int(parts[4][5:-1]), list(map(lambda x: x.strip(","),parts[9:]))
    label2rate[fromL] = rate
    for t in toL:
        G.add_edge(fromL, t, weight = 1)

valid_node = [ node for node in G.nodes() if label2rate[node] != 0]
 
res = float("-inf")
def dijkstra( start):
    global res
    round = 0
    heap = [(label2rate[start], 0 , set(), start)]
    while heap:
        pressure, dist, seen, label  = heapq.heappop(heap)
        round += 1
        if label in seen:
            continue       
        seen.add(label)        
        if dist > 30:
            continue 
        pressure = pressure + (label2rate[label] * (30-dist))
        res = max(res, pressure)
        
        for l in valid_node:            
            if l in seen: continue
            curDist = len(nx.shortest_path(G, source=label, target=l)) 
            heapq.heappush(heap, (pressure, dist+curDist, set(seen), l))

dijkstra(startL)
print("par1",res)