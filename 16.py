#!/usr/bin/python3

import re

# Naive part 1 recursive solution
def recurse(loc, elapsed, score):
    if elapsed >= 30:
        return score
    best = score
    # generate moves.  first is to turn on valve
    if state[loc] == False and rate[loc] > 0:
        state[loc] = True
        s = recurse(loc, elapsed + 1, score + rate[loc] * (30 - elapsed - 1))
        if s > best:
            best = s
        state[loc] = False
    else:
        # others are moving to an important valve that is currently off
        for k in important.keys():
            c = elapsed + cost[loc + k]
            if c <= 30 and k != loc and state[k] == False and rate[k] > 0:
                s = recurse(k, c, score)
                if s > best:
                    best = s
    return best

# Part 2 recursive solution
# does all the "you" moves, followed by all the elephant moves
# has a ghetto beta cutoff type thing to bail out of searches
# where even perfect results can't improve beyond what's already
# been found
def recurse2(loc1, loc2, elapsed1, elapsed2, score):
    global bestsofar
    best = score
    found = False

    # generate "you" moves.  first is to turn on valve
    if state[loc1] == False and rate[loc1] > 0 and elapsed1 < 26:
        found = True
        state[loc1] = True
        s = recurse2(loc1, loc2, elapsed1 + 1, elapsed2, score + rate[loc1] * (26 - elapsed1 - 1))
        if s > best:
            best = s
        state[loc1] = False
    else:
        # others are moving to an important valve that is currently off
        for k in important.keys():
            c = elapsed1 + cost[loc1 + k]
            if c <= 26 and k != loc1 and state[k] == False and rate[k] > 0:
                found = True
                s = recurse2(k, loc2, c, elapsed2,  score)
                if s > best:
                    best = s

    if not found:
        # calculate a theoretical top end.  If it's below our best so far, bail early
        # (fakey beta cutoff)
        max = 0
        left = []
        for k in important.keys():
            if state[k] == False:
                left.append(rate[k])
        left.sort(reverse=True)
        n = 1
        for val in left:
            s = val * (26 - elapsed2 - n)
            if s > 0:
                max += s
                n += 2
        if score + max < bestsofar:
            return best
        
        # generate "elephant" moves.  first is to turn on valve
        if state[loc2] == False and rate[loc2] > 0 and elapsed2 < 26:
            state[loc2] = True
            s = recurse2(loc1, loc2, elapsed1, elapsed2 + 1, score + rate[loc2] * (26 - elapsed2 - 1))
            if s > best:
                best = s
            state[loc2] = False
        else:
            # others are moving to an important valve that is currently off
            for k in important.keys():
                c = elapsed2 + cost[loc2 + k]
                if c <= 26 and k != loc2 and state[k] == False and rate[k] > 0:
                    s = recurse2(loc1, k, elapsed1, c,  score)
                    if s > best:
                        best = s
    if best > bestsofar:
        bestsofar = best
        print(f"{best}")
    return best

# find_cheapest for dijkstra algrorithm
def find_cheapest():
    min = ''
    minval = 999999
    for k in unvisited.keys():
        if unvisited[k] < minval:
            minval = unvisited[k]
            min = k
    return min

# boring dijkstra algorithm to find fastest paths
def dijkstra():
    while len(unvisited) > 0:
        s = find_cheapest()
        visited[s] = unvisited[s]
        del unvisited[s]
        cost = visited[s] + 1
        for path in paths[s]:
            if path not in visited:
                if path not in unvisited:
                    unvisited[path] = cost
                elif unvisited[path] > cost:
                    unvisited[path] = cost

ans1 = 0
ans2 = 0

with open('16.txt') as f:
    data = f.read().rstrip('\n').split('\n')

rate = {}
state = {}
paths = {}
best = 0
important = {}
unvisited = {}
visited = {}
cost = {}

for line in data:
    n = re.match(r'Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line)
    g = n.groups()
    v = g[0]
    rate[v] = int(g[1])
    if int(g[1]) > 0 or v == 'AA':
        important[v] = int(g[1])
    state[v] = False
    paths[v] = g[2].split(', ')

# build cost map for moving from any important node to any important node
# ie either the start or one with a valve with a flow rate > 0
# so we always to the fastest path from one to another, and 
# we only ever "stop" at nodes with a worthwhile valve
for f in important.keys():
    visited.clear()
    unvisited.clear()
    unvisited[f] = 0
    dijkstra()
    for t in important.keys():
        cost[f+t] = visited[t]

# simple recursive search using the above data
ans1 = recurse('AA', 0, 0)
print(f"Part 1: {ans1}")

# Recursive search that does all the "you" moves followed by all the "elephant" moves
# Added cheesy beta cutoff to reduce the time spent in known bad sections of the tree
bestsofar = 0
ans2 = recurse2('AA', 'AA', 0, 0, 0)
print(f"Part 2: {ans2}")

