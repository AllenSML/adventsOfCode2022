import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input17.txt"
parts = open(str(cur_dir)+file_name).read().split("\n\n")
jetPattern = parts[0]
shapes = parts[1:]
highest_rock = 0
left_offset = 2
leftWall = -1
rightWall = 7
ground = 0

# jetPattern = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

shapeCords_all = list()
for shape in shapes:
    shape = [list(line) for line in  shape.split("\n")[::-1]]
    shapeCordSet = list()
    for x, row in enumerate(shape):
        for y, v in enumerate(row):
            if v == '#':
                shapeCordSet.append((x,y))
    shapeCords_all.append(shapeCordSet)

def draw_grid(rest_rocks):
    grid = [["." for __ in range(8)] for _ in range(20)]
    print(shapeCords)
    for x, y in rest_rocks:
        grid[x][y] = "#"
    for g in grid[::-1]:
        print("".join(g))

def move_shape(shapeCords, direction=""):
    if direction == ">":
        shapeCords = [[x, y+1]  for (x,y) in shapeCords]
    elif direction == "<":
        shapeCords = [[x, y-1]  for (x,y) in shapeCords]
    else:
        shapeCords = [[x-1, y]  for (x,y) in shapeCords]
    return shapeCords
    
def can_move(shapeCords, direction=""):
    if direction == ">":
        if any( True for x,y in shapeCords if (x,y+1) in rest_rocks or y+1 == rightWall ):        
            return False
    elif direction == "<":
        if any( True for x,y in shapeCords if (x,y-1) in rest_rocks or y-1 == leftWall ):        
            return False
    else:
        if any( True for x,y in shapeCords if (x-1,y) in rest_rocks or x-1 == ground ):        
            return False
    return True

round = 0
jetPatternIdx = 0
rest_rocks = set()
for shapeCords in cycle(shapeCords_all):
    if rest_rocks:         
        highest_rock = max( x for x,y in rest_rocks )
    print("rounds: ", round, "highest_rock", highest_rock )

    if round == 2022:        
        print(highest_rock)
        exit()
    shapeCords = [[x+highest_rock+4, y+left_offset]  for (x,y) in shapeCords]
    
    rest = False
    while not rest:                
        while True:
            shift = jetPattern[jetPatternIdx%len(jetPattern)]
            jetPatternIdx += 1            
            if can_move(shapeCords, shift):                
                shapeCords = move_shape(shapeCords, shift)
            if can_move(shapeCords):
                shapeCords = move_shape(shapeCords)
            else:
                rest = True
                break
                
    for x, y in shapeCords:
        rest_rocks.add((x,y))
    round += 1
    