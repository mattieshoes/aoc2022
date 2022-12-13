#!/usr/bin/python3

import functools

def recursive_split(x, *args):
    y = []
    x = x.split(args[0])
    for part in x:
        if len(args) > 1:
            y += [recursive_split(part, *args[1:])]
        else:
            y += [part]
    return y

# custom comparison as defined by problem
def comp(a, b):
    if type(a) is list and type(b) is list:
        ml = len(a)
        if len(b) < ml:
            ml = len(b)
        for i in range(ml):
            result = comp(a[i], b[i])
            if result != 0:
                return result
        if len(a) > len(b):
            return 1
        elif len(b) > len(a):
            return -1
        else:
            return 0
    elif type(a) is int and type(b) is int:
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0
    elif type(a) is list and type(b) is int:
        return comp(a, [b])
    elif type(a) is int and type(b) is list:
        return comp([a], b)
        
ans1 = 0
ans2 = 0

with open('13.txt') as f:
    data = recursive_split(f.read().rstrip('\n'), '\n\n', '\n')

idx = 1
p2list = []
for pair in data:
    a = eval(pair[0])
    b = eval(pair[1])
    p2list.append(a)
    p2list.append(b)
    result = comp(a, b)
    if result == -1:
        ans1 += idx
    idx += 1
print(f"Part 1: {ans1}")

p2list.append([[2]])
p2list.append([[6]])
s = sorted(p2list, key=functools.cmp_to_key(comp))
two_sentinel = 0
six_sentinel = 0
for i in range(len(s)):
    if s[i] == [[2]]:
       two_sentinel = i + 1 
    elif s[i] == [[6]]:
        six_sentinel = i + 1
ans2 = two_sentinel * six_sentinel

print(f"Part 2: {ans2}")

