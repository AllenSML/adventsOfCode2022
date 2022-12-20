import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input20.txt"
nums = open(str(cur_dir)+file_name).read().split("\n")
# nums = [811589153, 1623178306, -2434767459, 2434767459, -1623178306, 0, 3246356612]

def exec(nums,time, decryptionKey ):
    nums = list(map(int, nums))    
    nums = list(map(lambda x:x*decryptionKey, nums))
    id2val = dict(enumerate(nums))
    val2id = dict((v,k) for k,v in id2val.items())
    queue = deque(id2val.keys())
    for _ in range(time):
        for k,v in id2val.items():
            pos = queue.index(k)
            queue.rotate(-pos)
            queue.popleft() 
            queue.rotate(-v)
            queue.appendleft(k)
    res = 0
    pos_0 = queue.index(val2id[0])
    queue.rotate((-pos_0))
    queue.rotate(-1000)
    res += id2val[queue[0]]
    queue.rotate(-1000)
    res += id2val[queue[0]]
    queue.rotate(-1000)
    res += id2val[queue[0]]
    return res
    
res = exec(nums,1,1)
print("part1: ", res)
res = exec(nums,10,811589153)
print("part2: ", res)



