#!/usr/bin/python3

import re, functools

ans1 = 0
ans2 = 1

# recursive search function
@functools.lru_cache(maxsize=None)
def search(ore, clay, obsidian, geode, r_0, r_1, r_2, r_3, time_left):
    global global_best
    resources = [ore, clay, obsidian, geode]
    nr = [ore, clay, obsidian, geode]
    robots = [r_0, r_1, r_2, r_3]

    # bail when time runs out
    if time_left == 0:
        if resources[3] > global_best:
            global_best = resources[3]
            print(f"New Global Best: {global_best}")
        return resources[3]

    best = 0
    score = 0

    # calculate best-case scenario for early exit if we can't possibly catch up
    s = geode
    ss = r_3
    for t in range(time_left, -1, -1):
        s += ss
        ss += 1
    if s < global_best:
        return 0

    # add what we make this round
    for i in range(4):
        nr[i] += robots[i]

    # build robot?
    for idx, r in enumerate(robot_cost):
        # don't build more resource-gathering robots than we can use
        if robots[idx] >= max_cost[idx]:
            continue
        # verify resources are available using round-start numbers
        can_build = True
        for i in range(3):
            if resources[i] < r[i]:
                can_build = False
        if can_build: 
            # subtract cost of robot
            for i in range(3):
                nr[i] -= r[i]
            
            # add robot
            robots[idx] += 1
            
            # recurse
            score = search(nr[0], nr[1], nr[2], nr[3], robots[0], robots[1], robots[2], robots[3], time_left - 1)
            if score > best:
                best = score
            
            # subtract robot
            robots[idx] -= 1
            
            # add cost of robot subtracted
            for i in range(3):
                nr[i] += r[i]
    
    # also try not-building robot
    score = search(nr[0], nr[1], nr[2], nr[3], robots[0], robots[1], robots[2], robots[3], time_left - 1)
    if score > best:
        best = score

    return best

with open('19.txt') as f:
    data = f.read().rstrip('\n').split('\n')

blueprint_number = 0
robot_cost = []
max_cost = [0, 0, 0, 0]
global_best = 0

# iterate through inputs
for index, line in enumerate(data):
    robot_cost = []
    blueprint_number = 0
    global_best = 0
    res = re.findall(r'\d+', line)
    blueprint_number = int(res[0])
    robot_cost.append([int(res[1]), 0, 0, 0])
    robot_cost.append([int(res[2]), 0, 0, 0])
    robot_cost.append([int(res[3]), int(res[4]), 0, 0])
    robot_cost.append([int(res[5]), 0, int(res[6]), 0])

    # calculate max resource costs for building a robot
    for r in robot_cost:
        for i in range(0,4):
            if r[i] > max_cost[i]:
                max_cost[i] = r[i]
    max_cost[3] = 999999

    search.cache_clear()
    score = search(0, 0, 0, 0, 1, 0, 0, 0, 24)
    print(f"Part 1 blueprint {blueprint_number}, Score: {score}")
    ans1 += blueprint_number * score

    # only do part 2 for the first 3 inputs
    if index < 3:
        search.cache_clear()
        score = search(0, 0, 0, 0, 1, 0, 0, 0, 32)
        print(f"Part 2 blueprint {blueprint_number}, Score: {score}")
        ans2 *= score


print(f"Part 1: {ans1}")
print(f"Part 2: {ans2}")
