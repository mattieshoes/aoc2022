#!/usr/bin/python3

def recursive_split(x, *args):
    y = []
    x = x.split(args[0])
    for part in x:
        if len(args) > 1:
            y += [recursive_split(part, *args[1:])]
        else:
            y += [part]
    return y


def tail(h, t):
    if abs(t[0]-h[0]) < 2 and abs(t[1]-h[1]) < 2:
        return t
    r = t[0]
    c = t[1]
    if t[0] < h[0]:
        r += 1
    elif t[0] > h[0]:
        r -= 1
    if t[1] < h[1]:
        c += 1
    elif t[1] > h[1]:
        c -= 1
    return(r, c)

with open('9.txt') as f:
    data = recursive_split(f.read().rstrip('\n'), '\n', ' ')

ans1 = {}
ans2 = {}

knots = [(0,0) for i in range(10)]
ans1[knots[1]] = 1
ans2[knots[9]] = 1

for line in data:
    offset = (0,0)
    if line[0] == 'U':
        offset = (-1,0)
    elif line[0] == 'D':
        offset = (1,0)
    elif line[0] == 'L':
        offset = (0, -1)
    elif line[0] == 'R':
        offset = (0, 1)
    for i in range(int(line[1])):
        knots[0] = (knots[0][0]+offset[0], knots[0][1]+offset[1])
        for i in range(1, 10):
            knots[i] = tail(knots[i-1], knots[i])
        ans1[knots[1]] = 1 
        ans2[knots[9]] = 1 

print(f"Part 1: {len(ans1)}")
print(f"Part 2: {len(ans2)}")



