#!/usr/bin/python3

import re
from copy import deepcopy

# does test, with humn=None for part 1
# or calculates difference for part 2 if provided a value for humn
def test(humn=None):
    solved = {}
    unsolved = {}
    for line in data:
        k, v = line.split(': ')
        if re.match(r'\d+', v):
            solved[k] = int(v)
        else:
            vals = v.split(' ')
            unsolved[k] = vals
    
    # the adjustments for part 2 solving
    if humn != None:
        solved['humn'] = humn
        unsolved['root'][1] = '=='
    
    while len(unsolved) > 0:
        for k in list(unsolved.keys()):
            if unsolved[k][0] in solved and unsolved[k][2] in solved:
                if unsolved[k][1] == '+':
                    solved[k] = solved[unsolved[k][0]] + solved[unsolved[k][2]]
                    del unsolved[k]
                elif unsolved[k][1] == '-':
                    solved[k] = solved[unsolved[k][0]] - solved[unsolved[k][2]]
                    del unsolved[k]
                elif unsolved[k][1] == '*':
                    solved[k] = solved[unsolved[k][0]] * solved[unsolved[k][2]]
                    del unsolved[k]
                elif unsolved[k][1] == '/':
                    solved[k] = solved[unsolved[k][0]] / solved[unsolved[k][2]]
                    del unsolved[k]
                elif unsolved[k][1] == '==':
                    return solved[unsolved[k][0]] - solved[unsolved[k][2]]
    return solved['root']

ans1 = 0
ans2 = 0
with open('21.txt') as f:
    data = f.read().rstrip('\n').split('\n')

ans1 = test()
print(f"Part 1: {ans1}")


# Simply plugs in values for humn and narrows down range until it gets a zero
min = -100000000000000
minval = test(min)
max = 100000000000000
maxval = test(max)
mult = 1
if minval > maxval:
    mult = -1

while True:
    midpoint = (min + max) // 2
    val = test(midpoint)

    if val * mult > 0:
        max = midpoint
        maxval = val
    elif val * mult < 0:
        min = midpoint
        minval = val
    elif val == 0:
        ans2 = midpoint
        break
    #print(f"Min: {min} ({minval})   Max: {max} ({maxval})")

print(f"Part 2: {ans2}")
