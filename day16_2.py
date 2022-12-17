import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input16.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")


G = nx.DiGraph()
label2rate = dict()

for line in lines:
    parts = line.split()
    fromL, rate, toL = parts[1], int(parts[4][5:-1]), list(map(lambda x: x.strip(","),parts[9:]))
    label2rate[fromL] = rate
    for t in toL:
        G.add_edge(fromL, t, weight = 1)

valid_node_orignal = [ node for node in G.nodes() if label2rate[node] != 0] 
valid_node = valid_node_orignal+[("AA")]
ftDist = dict()
for l in valid_node:
    for ll in valid_node:            
        if l !=  ll:
            ftDist[(l,ll)] = len(nx.shortest_path(G, source=l, target=ll)) 

startL = "AA"    
level = 0
round = 0
visited = dict()
def dijkstra(start, seen):
    global startL
    global level
    global round
    res = float("-inf")
    heap = [(label2rate[start], 0 , seen, start)]
    level += 1
    while heap:
        round += 1
        pressure, dist, seen, label = heapq.heappop(heap)
        seen.add(label)        
        pressure = pressure + (label2rate[label] * (26-dist))
        terminate = True
        if level < 2:
            ans = 0
            if str(seen) not in visited:
                ans = dijkstra(startL, set(seen))                
                visited[str(seen)] = ans
            res = max(res, pressure+visited[str(seen)])
        for l in valid_node:            
            if l in seen: continue
            curDist = ftDist[(label,l)]
            if dist+curDist <= 26:
                terminate = False                
                heapq.heappush(heap, (pressure, dist+curDist, set(seen), l))
        if terminate:            
            res = max(pressure, res)
        if level == 1 and  level % 10000000 == 5:
            print(round, res)
    level -= 1
    return res

res = dijkstra(startL, set())
print("par2",res)
