#!/usr/bin/python3

import re, copy

# list elves split by double-newlines
with open('5.txt') as f:
    layout, lines = f.read().split('\n\n')
    layout = layout.split('\n')
    lines = lines.split('\n')

loc = {}
stacks = {}
ordering = []

# parse the last layout line for order, name, and location of stacks
k = layout.pop()
for pos in range(len(k)):
    if k[pos] != ' ':
        stacks[k[pos]] = []
        loc[k[pos]] = pos
        ordering.append(k[pos])

# iterate backwards over the rest of the layout for stacks
for line in reversed(layout):
    for key in loc.keys():
        if line[loc[key]] != ' ':
            stacks[key].append(line[loc[key]])

# make a deep copy of the stacks so part 1 and 2 can be independent
stacks2 = copy.deepcopy(stacks)

for line in lines:
    vals = re.findall(r"(\d+)", line)
    count = int(vals[0])
    f = vals[1]
    t = vals[2]

    # for part 1, iteratively move one item at a time
    for i in range(0, count):
        item = stacks[f].pop()
        stacks[t].append(item)

    # for part 2, move all at once
    stacks2[t] += stacks2[f][-count:]
    stacks2[f] = stacks2[f][:-count]

for i in ordering:
    print(stacks[i][-1], end='')
print()

for i in ordering:
    print(stacks2[i][-1], end='')
print()
