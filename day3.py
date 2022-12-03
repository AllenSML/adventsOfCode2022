from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy
import os,math, difflib, pathlib, string

#pathlib.Path(__file__).resolve() #direcotry of the script being run

file_path = "input3.txt"
inputs = open(file_path).read().split("\n")

l2Num = dict(zip(string.ascii_letters,range(1,53)))

ans = 0
for line in inputs:
    mid = len(line)//2
    first, second = line[:mid], line[mid:]
    letter = set(first) & set(second)
    ans += l2Num[letter.pop()]

print("part1: ", ans)


ans = 0
for i in range(0,len(inputs),3):
    first, second, third = inputs[i], inputs[i+1], inputs[i+2]    
    letter = set(first) & set(second) & set(third)
    ans += l2Num[letter.pop()]

print("part2: ", ans)



