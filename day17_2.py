import os,math, difflib, pathlib, string, re, json, functools, networkx as nx, numpy as np, heapq
from itertools import permutations, combinations, chain, cycle, repeat, product
from collections import defaultdict, Counter, deque, ChainMap
from copy import deepcopy

#There is no mathmatical proof of this solution, just check repeatition 
#based on the surface + new piece fallowing + next shifts(single shifts does not work)

cur_dir = pathlib.Path(__file__).resolve().parents[0] #.parents[0] #direcotry of the script being run
file_name ="/input17.txt"
parts = open(str(cur_dir)+file_name).read().split("\n\n")
jetPattern = parts[0]
shapes = parts[1:]
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

highest_rock = 0
left_offset = 2
leftWall = -1
rightWall = 7
ground = 0
M = None
N = None
round = 0
jetPatternIdx = 0
restRocks = set()
surface = dict((i,0) for i in range(7))
surfaces = dict()
round2Surface =  dict()

def calculate_res():
    T = 1000000000000
    height_increase = round2Surface[N-1][1] - round2Surface[M-1][1]
    times, mod = divmod(T-M, N-M)
    mod += M
    res = round2Surface[mod][1] + times*height_increase
    print(res)
    exit()

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
        if any(True for x,y in shapeCords if (x,y+1) in restRocks or y+1 == rightWall ):        
            return False
    elif direction == "<":
        if any(True for x,y in shapeCords if (x,y-1) in restRocks or y-1 == leftWall ):        
            return False
    else:
        if any(True for x,y in shapeCords if (x-1,y) in restRocks or x-1 == ground ):        
            return False
    return True

def surface_seen_before(surface, shapeCords, round, height, shift):
    global M
    global N
    global repeatTime
    min_x = min(surface.values())
    surface_ajudsted = str([ x-min_x for x in surface.values()]) + "---"+ str(shapeCords) + "---"+shift
    
    if surface_ajudsted in surfaces:
        M = surfaces[surface_ajudsted]
        N = round
        round2Surface[round] = (surface_ajudsted,height)   
        calculate_res()
    else:
        surfaces[surface_ajudsted] = round
        round2Surface[round] = (surface_ajudsted,height)    

for shapeCords in cycle(shapeCords_all):
    highest_rock = max(surface.values())
    surface_seen_before(surface,shapeCords, round, highest_rock, jetPattern[jetPatternIdx%len(jetPattern):])      
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
        restRocks.add((x,y))           
        surface[y] = max(surface[y], x)  
    round += 1

