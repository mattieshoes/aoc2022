#!/usr/bin/python3

import re, copy
from collections import OrderedDict

# rotates a rectangular block of text
def rotate(lines, clockwise=True):
    t = ['' for i in range(len(lines[0]))]
    if clockwise:
        lines.reverse()
    for i in range(len(lines[0])):
        for line in lines:
            t[i] += line[i]
    return t

with open('5.txt') as f:
    layout, lines = f.read().split('\n\n')
layout = layout.split('\n')
lines = lines.split('\n')

stacks = OrderedDict()

# rotate the layout clockwise so we can parse horizontally
rotated = rotate(layout)
for line in rotated:
    if line[0] != ' ':
        stacks[line[0]] = re.findall(r"\w", line[1:])

# make a deep copy of the stacks so part 1 and 2 can be independent
stacks2 = copy.deepcopy(stacks)

for line in lines:
    vals = re.findall(r"\d+", line)
    count = int(vals[0])
    f = vals[1]
    t = vals[2]

    # for part 1, reverse the moved chunk
    stacks[t] += reversed(stacks[f][-count:])
    stacks[f] = stacks[f][:-count]

    # for part 2, no reverse
    stacks2[t] += stacks2[f][-count:]
    stacks2[f] = stacks2[f][:-count]

for i in stacks.keys():
    print(stacks[i][-1], end='')
print()

for i in stacks2.keys():
    print(stacks2[i][-1], end='')
print()
