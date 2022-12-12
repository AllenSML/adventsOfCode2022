import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input12.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")

start = None
end = None

for line in lines:
    print(line)
height_map = list()
for x, line in enumerate(lines):
    new_line = list()
    for y, c in enumerate(line):
        if c == "S":
            start = (x,y)
            new_line.append(ord("a")- ord("a")+1)
        elif c == "E":
            end = (x,y)
            new_line.append(ord("z")- ord("a")+1)
        else:
            new_line.append(ord(c)- ord("a")+1)
    height_map.append(new_line)


        
m = len(height_map)
n = len(height_map[0])

def get_neighbours(x,y):
    neighbours = [  (x-1,y ), 
                    (x+1,y ),
                    (x,y+1 ),
                    (x,y-1 )]
    return [(r, c) for r,c in neighbours if 0 <= c < n and 0 <= r <m]


def dijkstra( start, end):
    visited = set()
    heap = [(0, start, visited)]
    while heap:
        cost, u, visited = heapq.heappop(heap)
        x,y = u
        if u in visited:
            continue
        visited.add(u)
        # print("lines[x][y]", lines[x][y], cost, u)
        if lines[x][y] == "E":
            return cost

        for cx,cy in get_neighbours(x,y):
            if (cx,cy) in visited:
                continue            
            # print(height_map)
            # print(m,n, cx,cy, x,y, height_map[cx][cy])
            if height_map[cx][cy] - height_map[x][y] > 1:
                continue 
            next = cost + 1
            heapq.heappush(heap, (next, (cx,cy), visited))
    return float("inf")


steps = dijkstra(start,end)
print("part1: ", steps)

res = float("inf")

for x, line in enumerate(lines):
    for y, c in enumerate(line):
        if c == "a" or c == "S":
            ans = dijkstra((x,y), end)
            res = min(ans, res)

print("part2: ", res)

