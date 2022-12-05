from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy
import os,math, difflib, pathlib, string, re, json, functools

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input5.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")

stacks = ['NZ', 'DCM', "P"]
stacks = ['FTNZMGHJ', 'JWV', "HTBJLVG", "LVDCNJPB", "GRPMSWF", "MVNBFCHG", "RMGHD", "DZVMNH", "HFNG"]

stacks = [stack[::-1] for stack in stacks]
stacks = list(map(list, stacks))
stacks_backup = deepcopy(stacks)
    
for line in lines:
    a,b,c = list(map(int, re.findall(r'\d+', line)))
    for i in range(a):
        stacks[c-1].append(stacks[b-1].pop())
res = "".join([ s[-1] for s in stacks])
print("part1: ", res)

stacks = stacks_backup
for line in lines:
    a,b,c = list(map(int, re.findall(r'\d+', line)))
    temp_stack = list()
    for i in range(a):
        temp_stack.append(stacks[b-1].pop())
    while temp_stack:
        stacks[c-1].append(temp_stack.pop())

# print(stacks)

res = "".join([ s[-1] for s in stacks])
print("part2: ", res)




