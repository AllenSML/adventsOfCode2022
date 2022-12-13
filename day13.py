import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, operator
from itertools import permutations, combinations, chain, cycle, repeat, product,zip_longest
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input13.txt"
pairs = open(str(cur_dir)+file_name).read().split("\n\n")

#to improve: use -1,0,1 intead of 0,1,2
def compare(p1,p2):
    for v1, v2 in zip_longest(p1,p2,fillvalue=None):
        # print("v1,v2", v1,v2, type(v1), type(v2))
        if not isinstance(v1, list) and not isinstance(v2, list):
            if v1 == None:
                return 2
            elif v2 == None:
                return 0
            elif v1 < v2:
                return 2            
            elif v1 > v2:
                return 0            
            
        elif  isinstance(v1, list) and isinstance(v2, list):
            ans = compare(v1, v2)
            if ans != 1:
                return ans
        elif  isinstance(v1, list) and not isinstance(v2, list):            
            if v2 == None: 
                return 0
            ans = compare(v1, [v2])
            if ans != 1:
                return ans
        elif  not isinstance(v1, list) and isinstance(v2, list):
            if v2 == None: 
                return 0
            ans = compare([v1], v2)
            if ans != 1:
                return ans
    return 1

def compare_convert(p1,p2):
    index = compare(p1,p2)
    return [1,0,-1][index]

def part1():    
    sum_indicies = 0 
    for i, pair in enumerate(pairs):
        p1, p2 = list(map(json.loads, pair.split("\n")))        
        res = compare(p1,p2)
        assert res == 0 or res == 2
        if res: 
            sum_indicies += i+1
            
    return sum_indicies

print("part1: ", part1())

pairs = open(str(cur_dir)+file_name).read().split("\n")
pairs = [ p for p in pairs if p.strip() != ""]
pairs = list(map(json.loads, pairs))
divider1 = [[2]]
divider2= [[6]]
pairs.extend([divider1, divider2])

    
pairs_sorted = sorted(pairs, key=functools.cmp_to_key(compare_convert))

keys = list()
for i, p in enumerate(pairs_sorted):
    if str(p) == str(divider2):
        keys.append(i+1)
    elif str(p) == str(divider1):
        keys.append(i+1)

ans = functools.reduce(operator.mul, keys,1)
print("ans", ans)


    
