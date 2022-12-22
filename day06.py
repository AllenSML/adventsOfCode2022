import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input6.txt"
input = open(str(cur_dir)+file_name).read().split("\n")
print(input)

test_input = [
"bvwbjplbgvbhsrlpgdmjqwftvncz",
"nppdvjthqldpwncqszvftbrmjlhg",
"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" ]

test_input = [
"mjqjpqmgbljsphdztnvjfqwrcgsmlb",
"bvwbjplbgvbhsrlpgdmjqwftvncz",
"nppdvjthqldpwncqszvftbrmjlhg",
"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
]

def exec(max_len):
    for line in input:
        queue = deque(maxlen=max_len)
        for id, c in enumerate(line):
            queue.append(c)
            if len(queue) == max_len and len(set(queue)) == max_len:
                return id + 1


print("part1: ", exec(4))
print("part2: ", exec(14))