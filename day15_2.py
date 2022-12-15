import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input15.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")
lines = [list(map(int,re.findall(r"\-?\d+", line))) for line in lines]

base = 4000000
stop = False
for row in range(base+1):
    all_dist = list()

    for line in lines:
        sx,sy, bx, by = line
        dist = abs(sx-bx) + abs(sy-by)
        dist_wo_y = abs(sy-row) 
        if dist < dist_wo_y:
            continue
        left_x = sx - (dist-dist_wo_y)
        right_x = sx + (dist-dist_wo_y)
        all_dist.append([left_x, right_x])


    all_dist = list(sorted(all_dist))

    new_all_dist = list()
    for left, right in all_dist:
        if not new_all_dist: 
            new_all_dist += [[left, right]]

        elif left > new_all_dist[-1][1]+1:
            new_all_dist += [[left,right]]
        else:
            new_all_dist[-1][1] = max(right, new_all_dist[-1][1])

    start = 0
    for left, right in new_all_dist:
        if start < left:
            stop = True
            print("res: ",start*base+row)
            break
        start = max(start, right+1)
        if start > base:
            break
    if stop:
        break
        

    


    



