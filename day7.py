import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input7.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")


dir2Content = dict()
cur_dir, pre_dir, cmd, val, isContent =[],  "",None, None, False
n2w = defaultdict(int)
p2t = defaultdict(list)

n2w["."] = 0
for l in lines:
    if "$" in l:
        parts = l[2:].split()
        if len(parts) == 1:
            cmd = parts[0]
            val = None
        else:
            cmd, val = parts 
        if cmd == "cd":
            if val == "/":
                cur_dir = ["."]
            elif val == "..":                
                cur_dir.pop()
            else:
                cur_dir.append(val)
    else:   
        p1, p2 = l.split()        
        cur_dir_str = " ".join(cur_dir)
        cur_file_path_str = " ".join(cur_dir+[p2])
        if p1 == "dir":            
            n2w[cur_file_path_str] = 0
        else:
            n2w[cur_file_path_str] = int(p1) 
        p2t[cur_dir_str] += [cur_file_path_str]

dirs = [ k for k,v  in n2w.items() if v == 0]
    

part1_res =  []
# too slow with recursion, maximum levels exceeded
# def postorderTraversal(root):
#     if not root: return []
#     res, weights =0, list()
#     for node in p2t[root]:
#         weight = postorderTraversal(node)
#         weights += [weight]
#     if weights:
#         res = sum(weights)
#     res += n2w[root]
#     if res <= 100000 and n2w[root] != 0:
#         part1_res.append(res)
#     return res 

p2t_copy = deepcopy(p2t)
def postorderTraversal1(root):
    if not root: return []
    stack = [root]
    while stack:
        current = stack[-1]
        if not p2t[current]:
            stack.pop()
            for node in p2t_copy[current]:
                n2w[current] +=  n2w[node]
        else:
            for node in p2t[current]:
                stack.append(node)
            p2t[current] = []

ans = postorderTraversal1(".")

res = 0
for k,v in n2w.items():
    if v <= 100000 and k in dirs:
        res += v

print("part1: ", res)

total_size = 70000000
space_needed = 30000000
space_to_free = space_needed - (total_size-n2w["."])


res2 = float("inf")
for k,v in n2w.items():
    if k in dirs and v >= space_to_free:
        res2 = min(res2, v)


print("part2: ", res2)
