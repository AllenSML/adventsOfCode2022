from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque
from copy import deepcopy
import os, os.path, math

file_path = "input2.txt"
inputs = open(file_path).read().split("\n")
lines = [ [ w for w in ip.split() ] for ip in inputs]


stra2Score = {"X":1, "Y": 2, "Z":3, "A": 1, "B":2, "C": 3}
score  = 0 

for line in lines:
    p1, p2 = line
    cur = 0
    if " ".join([p1,p2]) in ("A Y", "B Z", "C X"):
        cur += 6    
    if " ".join([p1,p2]) in ("A X", "B Y", "C Z") :
        cur +=3
    else:
        cur +=0
    cur += stra2Score[p2]
    score += cur

print("part1: ", score)

str2 = {"A": ("Y", "X", "Z"), "B": ("Z","Y", "X"), "C": ("X", "Z", "Y")}
score = 0
for line in lines:
    p1, p2 = line
    cur = 0
    if p2 == "X":
        cur += stra2Score[str2[p1][2]]
    elif p2 == "Y":
        cur +=3
        cur += stra2Score[str2[p1][1]]
    else:
        cur += stra2Score[str2[p1][0]]
        cur +=6
    score += cur

print("part2 ", score)

