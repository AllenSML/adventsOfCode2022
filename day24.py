import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input24.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")


m, n = len(lines), len(lines[0])

def neighbours(x,y):
    global m
    global n    
    neighbours = [  (x-1,y), 
                    (x+1,y),
                    (x,y+1),
                    (x,y-1),
                    (x,y),]
    return [(nx, ny) for nx,ny in neighbours if 0 <= nx < m and 0 <= ny < n]
    


def draw_grid(tiles,pos):
    # print((tiles))
    global m
    global n 
    grid = [[ "." if 1 <= c < n-1 and 1 <= r < m-1 else "#" for c in range(n)] for r in range(m)]
    for (xx, yy)in tiles:
        grid[xx][yy] = tiles[(xx,yy)][0] if len(tiles[(xx,yy)]) == 1 else len(tiles[(xx,yy)]) 
    grid[pos[0]][pos[1]] = "E"
    print("\n".join( "".join(map(str,line)) for line in grid ))
    print("\n\n")

tiles = dict()
b2d = dict(zip("^v<>", [(-1,0),(1,0),(0,-1),(0,1)]))
start, end = (0,1), (m-1, n-2)


for i, line in enumerate(lines):
    for j, cell in enumerate(line):
        if 1 <= j < n-1 and 1 <= i <m-1 and cell != ".":
            tiles[(i,j)] = tiles.get((i,j),[]) + [cell]


def change_whether(tiles):
    global t2t
    if str(tiles) in t2t:
        return t2t[str(tiles)]
    newTiles = dict()
    for (i,j), blizards in tiles.items():
        for b in blizards:
            ni, nj = i + b2d[b][0], j + b2d[b][1]
            if not (1 <= nj < n-1 and 1 <= ni < m-1):
                if b == "^": 
                    ni = m-2
                elif b == "<":
                    nj = n-2
                elif b == ">":
                    nj = 1
                elif b == "v":
                    ni = 1
            newTiles[(ni,nj)] = newTiles.get((ni,nj), []) + [b]
    t2t[str(tiles)] = newTiles
    return newTiles
round = 1
cache = dict()
t2t = dict()

def exec(heap, end, backwards):    
    global tiles
    while heap:    
        tiles = change_whether(tiles)
        round = 0
        for _ in range(len(heap)):
            cost, pos = heapq.heappop(heap)           
            key = (*pos, str(tiles.items()))
            if key in cache:
                continue
            cache[key] = cost
            # draw_grid(tiles, pos)
            print(cost+1, round, pos)
            # if (cost+1)%100 == 0:
            #     print(cost+1)
            for nb in neighbours(*pos):        
                if nb == end: 
                    print(cost+1,round,nb)
                    draw_grid(tiles, pos)
                    return cost+1
                # print("lines[nb[0]][nb[1]]", lines[nb[0]][nb[1]])
                if not (1 <= nb[1] < n-1 and 1 <= nb[0] < m-1) and lines[nb[0]][nb[1]] == "#" : continue
                if nb in tiles and len(tiles[nb]) > 0: continue        
                
                heapq.heappush(heap, (cost+1, nb))            
            round +=1
    return cost

cost = exec([(0, start)],end, False)

cost = exec([(0, end)],start, True)
print(cost)