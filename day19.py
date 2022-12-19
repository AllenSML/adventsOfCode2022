import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input19.txt"
lines = open(str(cur_dir)+file_name).read().split("\n")

robot2index = {"ore":0,"clay": 1, "obsidian": 2,"geode":3}
index2robot = dict((v,k) for k,v in robot2index.items())
mem = dict()
data = list()

for line in lines:
    robotlimit = [0,0,0]
    bluePrint = list()
    for part in map(lambda input: input.strip(),line.strip(".").split(": ")[1].split(".")):                
        formular = list()
        print(part)
        for x, y in re.findall(r'(\d+) (\w+)', part):            
            x = int(x)
            formular.append((x,robot2index[y]))            
            robotlimit[robot2index[y]] = max(robotlimit[robot2index[y]],x)
        bluePrint.append(formular)        
    stock = [0,0,0,0]        
    robots = [1,0,0,0]
    time = 32
    data.append((stock, robots, time, bluePrint, robotlimit))

def dfs(stock, robots, time , bluePrint, robotlimit):
    
    if time <= 0:
        return stock[3]
    key = (time, *stock, *robots)
    if key in mem:        
        return mem[key]        
    repeat = True
    tried = set()
    res =  stock[3]  + robots[3]*time 
    while repeat:
        if time <= 0 or len(tried): 
            break
        time -= 1
        for i in range(4):
            if i in tried: continue
            bp = bluePrint[i]
            if (i != 3 and robots[i] >= robotlimit[i]):
                tried.add(i)             
                continue
            for amount, resource in bp:
                if amount > stock[resource]:
                    break
            else:
                stock_new = deepcopy(stock)
                robots_new = deepcopy(robots)
                tried.add(i)
                for amount, resource in bp:
                    if robots[resource] == 0: 
                        break
                    stock_new[resource] = stock[resource]-amount
                else:
                    robots_new[i] += 1            
                    stock_new = [ s + r for s, r in  zip(stock_new, robots)]            
                    for j in range(3):
                        stock_new[j] =  min(stock_new[j], robotlimit[j] * time) 
                    res =max(res, dfs(stock_new, robots_new, time, bluePrint, robotlimit))        
        stock = [ s + r for s, r in zip(stock, robots)]
    mem[key] = res
    return res

res = 0
for i, d in enumerate(data):
    mem.clear()
    ans = dfs(*d)
    res += (i+1)*ans
print("part1: ",res)

res = 1
for i, d in enumerate(data[:3]):
    mem.clear()
    ans = dfs(*d)
    res *= ans
print("part2: ", res)


