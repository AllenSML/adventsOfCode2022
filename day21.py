import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy
import operator

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input21.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")

numMonkeys = dict()
mathMonkeys = dict()
operators = [operator.mul, operator.sub, operator.truediv,operator.add]
operators = dict(zip('*-/+', operators))
operatorsReversed= dict(zip([operator.mul, operator.sub, operator.truediv,operator.add], [operator.truediv, operator.add, operator.mul,operator.sub]))

humn = "humn"
root = "root"

for line in lines:
    monkey, yell = line.split(": ")
    if len(yell.split()) == 1:
        numMonkeys[monkey] = int(yell)
    elif len(yell.split()) == 3:
        mon1, op, mon2 = yell.split()                
        mathMonkeys[monkey] = [mon1, mon2, operators[op]]  
        

def dfs(monkey):
    if monkey in numMonkeys:
        return numMonkeys[monkey]
    mon1, mon2, op = mathMonkeys[monkey]
    ans = op(dfs(mon1),dfs(mon2))
    return ans

res = dfs(root)
print("part1: ",res)

numMonkeys[humn] = None


def dfs_1(monkey):
    if monkey in humn:
        return None
    if monkey in numMonkeys:
        return numMonkeys[monkey]
    assert monkey in mathMonkeys
    mon1, mon2, op = mathMonkeys[monkey]
    res1 = dfs_1(mon1)
    res2 = dfs_1(mon2)
    if res1 and res2:
        numMonkeys[monkey] = op(res1, res2)
        return numMonkeys[monkey]
    else:
        return None

dfs_1(root)
mon1, mon2, op = mathMonkeys[root]
numMonkeys[root] = 2* numMonkeys[mon1] if mon1 in numMonkeys else 2*numMonkeys[mon2]

def dfs_2(monkey):    
    global res 
    if monkey == humn:        
        return 
    mon1, mon2, op = mathMonkeys[monkey]
    if mon1 in numMonkeys and numMonkeys[mon1]:
        if op in [ operator.sub, operator.truediv]:
            numMonkeys[mon2] = op(numMonkeys[mon1],numMonkeys[monkey])
        else:
            numMonkeys[mon2] = operatorsReversed[op](numMonkeys[monkey],numMonkeys[mon1] )
        dfs_2(mon2)
    else:
        numMonkeys[mon1] = operatorsReversed[op](numMonkeys[monkey], numMonkeys[mon2])
        dfs_2(mon1)

dfs_2(root)
print("part2: ", numMonkeys[humn])