from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy
import os,math, difflib, pathlib, string, re

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input4.txt"
inputs = open(str(cur_dir)+file_name).read().split("\n")

lines = [[ list(map(int,l.split("-")))for l in  line.split(",")]for line in inputs]

ans = 0 
for line in lines:
    first, second = line
    if second[1] >= first[1] >= first[0] >= second[0]:
        ans += 1
    elif first[1] >= second[1] >= second[0] >= first[0]:
        ans += 1

print("part1: ", ans)


ans = 0 
for line in lines:
    first, second = line
    overlap = len(set(range(first[0], first[1]+1)) & set(set(range(second[0], second[1]+1)))) > 0
    ans += overlap

print("part2: ", ans)


ans = 0 
for line in lines:
    first, second = line
    left = max(first[0], second[0])
    right = min(first[1], second[1])

    ans += 1 if left <= right else 0

print("part2 ", ans)