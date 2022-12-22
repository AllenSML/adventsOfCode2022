from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque
from copy import deepcopy
import os, os.path, math

file_path = "input1.txt"
inputs = open(file_path).read().split("\n\n")
lines = [list(map(int,ip.split("\n")))for ip in inputs]

stocks = [sum(l) for l in lines]
res = max(stocks)
print("part1:", res)
res = sum(sorted(stocks)[-3:])
print("part2: ", res)