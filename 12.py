#!/usr/bin/python3

from copy import deepcopy
import math

def find_cheapest():
    minkey = (999,999)
    minval = math.inf
    for key in unvisited.keys():
        if unvisited[key] < minval:
            minval = unvisited[key]
            minkey = key
    return minkey

def djikstra2():
    while True:
        
        # expand cheapest un-visited node
        s = find_cheapest()

        # visiting node, no longer unvisited
        visited[s] = unvisited[s]
        del unvisited[s]

        # bail when we've visited an 'a' node
        if data[s[0]][s[1]] == 'a':
            return s

        # potential moves
        moves = [(s[0], s[1]-1), (s[0], s[1]+1), (s[0]-1, s[1]), (s[0]+1, s[1])]
        
        #iterate, updating values in unvisited nodes
        for move in moves:
            if move[0] >= 0 and \
               move[0] < len(data) and \
               move[1] >= 0 and \
               move[1] < len(data[s[0]]) and \
               ord(data[move[0]][move[1]]) >= ord(data[s[0]][s[1]]) - 1 and \
               move in unvisited:
                cost = visited[s] + 1
                if unvisited[move] > cost:
                    unvisited[move] = cost

def djikstra():
    while end not in visited:
        # expand cheapest un-visited node
        s = find_cheapest()

        # visiting node, no longer unvisited
        visited[s] = unvisited[s]
        del unvisited[s]

        # potential moves
        moves = [(s[0], s[1]-1), (s[0], s[1]+1), (s[0]-1, s[1]), (s[0]+1, s[1])]
        
        #iterate, updating values in unvisited nodes
        for move in moves:
            if move[0] >= 0 and \
               move[0] < len(data) and \
               move[1] >= 0 and \
               move[1] < len(data[s[0]]) and \
               ord(data[move[0]][move[1]]) <= ord(data[s[0]][s[1]]) + 1 and \
               move in unvisited:
                cost = visited[s] + 1
                if unvisited[move] > cost:
                    unvisited[move] = cost
        

ans1 = 0
ans2 = 0

with open('12.txt') as f:
    data = f.read().rstrip('\n').split('\n')

start = 0
end = 0
unvisited = {}
visited = {}
for row in range(len(data)):
    for col in range(len(data[row])):
        coord = (row, col)
        if data[row][col] == 'S':
            start = coord
            unvisited[coord] = 0
        else:
            unvisited[coord] = math.inf
            if data[row][col] == 'E':
                end = coord
    data[row] = data[row].replace("S", "a")
    data[row] = data[row].replace("E", "z")
backup = deepcopy(unvisited)

djikstra()
ans1 = visited[end]
print(f"Part 1: {ans1}")

visited = {}
unvisited = backup
unvisited[start] = math.inf
unvisited[end] = 0
s = djikstra2()

ans2 = visited[s]
print(f"Part 2: {ans2}")

