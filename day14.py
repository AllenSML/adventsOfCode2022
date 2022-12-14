import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input14.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")

max_x, max_y = float("-inf"), float("-inf")
grid = None

for line in lines:
    cordinates = [list(map(int,pair.split(",")[::-1])) for pair in line.split(" -> ")]
    for x, y in cordinates:
        max_x = max(max_x,x)
        max_y = max(max_y,y)

max_pair = ( max_x, max_y)
print("max_y", max_y)
print("max_y", max_x)

def prepare_grid():
    global lines
    global grid

    for line in lines:
        cordinates = [list(map(int,pair.split(",")[::-1])) for pair in line.split(" -> ")]
        for i  in range(len(cordinates)-1):
            print(cordinates[i], cordinates[i+1])
            x,y = cordinates[i]
            x_, y_ = cordinates[i+1]
            cy = abs(y-y_)
            cx = abs(x-x_)
            for i in range(min(x,x_), min(x,x_)+cx+1):
                for j in range(min(y,y_), min(y,y_)+cy+1):
                    grid[i][j] = 1

def prepare_data_part2():
    global max_x
    global max_y
    global grid
    max_x, max_y = max_pair
    floor_x = max_x+ 2
    max_x +=3
    max_y *=2
    grid = np.zeros((max_x, max_y))
    grid[0][500] = 9
    prepare_grid()
    grid[floor_x,:] = [1 for _ in range(max_y)]

def prepare_data_part1():
    global max_x
    global max_y
    global grid
    max_x, max_y = max_pair
    max_x += 1
    max_y += 1
    grid =  np.zeros((max_x, max_y))
    grid[0][500] = 9
    prepare_grid()



def get_neighbours(i,j):
    neighbours = [         
        (i+1,j),
        (i+1,j-1),
        (i+1,j+1),
        ]
    return [(r, c) for r,c in neighbours]# if 0 <= c < n and 0 <= r <m]




def dfs(position):
    x,y = position
    # print("x,y", x,y)
    rest = True
    falling_forever = False
    for cx,cy in get_neighbours(*position):
        if not( 0 <= cy < max_y and 0 <= cx <max_x):
            return True
        if grid[cx][cy]== 1 or grid[cx][cy]== 2: continue
        falling_forever = dfs((cx,cy))
        rest = False
        
        break    
    if rest:
        grid[x][y] = 2
    return falling_forever
    



def part1(): 
    prepare_data_part1()
    falling_forever = False
    sand = (0,500)
    round = 0
    while not falling_forever:
        if grid[0][500] != 9:
            break
        falling_forever = dfs(sand)
        round += 1

    print("part1: ", "falling_forever",falling_forever, "round: ", round-1)

def part2(): 
    prepare_data_part2()
    falling_forever = False
    sand = (0,500)
    round = 0
    while not falling_forever:
        if grid[0][500] != 9:
            break
        falling_forever = dfs(sand)
        round += 1

    print("part2: ", "falling_forever",falling_forever, "round: ", round)

part1()
part2()







        
    
    








# def dfs(pos):



