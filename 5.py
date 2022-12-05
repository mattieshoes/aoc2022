#!/usr/bin/python3

import re
from collections import OrderedDict
from copy import deepcopy

with open('5.txt') as f:
    layout, lines = [n.split('\n') for n in f.read().split('\n\n')]

stacks = re.findall(r"[^ ]", layout[-1])
stacks = OrderedDict(zip(stacks, ['' for i in range(len(stacks))]))
for line in layout[-2::-1]:
    matchlist = re.finditer(r"\w", line)
    for m in matchlist:
        stacks[layout[-1][m.span()[0]]] += m.group(0)

# make a deep copy of the stacks so part 1 and 2 can be independent
stacks2 = deepcopy(stacks)

for line in lines:
    vals = re.findall(r"\d+", line)
    count = int(vals[0])
    f = vals[1]
    t = vals[2]

    # for part 1, reverse the moved chunk
    stacks[t] += stacks[f][-1:-count-1:-1]
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
