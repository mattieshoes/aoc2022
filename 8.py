#!/usr/bin/python3

import re

def score_offset(r, c, o):
    height = a[r][c]
    s = 0

    r += o[0]
    c += o[1]
    while(r >= 0 and r < len(a) and c >= 0 and c < len(a[0])):
        s += 1
        if a[r][c] >= height:
            break
        r += o[0]
        c += o[1]
    return s

def score(r, c):
    return score_offset(r, c, (0,1)) * \
           score_offset(r, c, (1,0)) * \
           score_offset(r, c, (-1,0)) * \
           score_offset(r, c, (0, -1))

def trees_seen(r, c, o):
    h = -1
    count = 0
    r += o[0]
    c += o[1]
    while(r >= 0 and r <len(a) and c >= 0 and c < len(a[0])):
        if a[r][c] > h:
            h = a[r][c]
            if not s[r][c]:
                s[r][c] = 1
                count += 1
        r += o[0]
        c += o[1]
    return count

ans1 = 0
ans2 = 0

with open('8.txt') as f:
    data = f.read().rstrip('\n').split('\n')

a = [[0 for x in range(len(data))] for x in range(len(data[0]))]
s = [[0 for x in range(len(data))] for x in range(len(data[0]))]

for r in range(len(a)):
    for c in range(len(a[0])):
        a[r][c] = int(data[r][c])

# Part 1 tree counting from all sides
for r in range(len(a)):
    ans1 += trees_seen(r, -1, (0, 1))
    ans1 += trees_seen(r, len(a[r]), (0, -1))
for c in range(len(a[0])):
    ans1 += trees_seen(-1, c, (1, 0))
    ans1 += trees_seen(len(a), c, (-1, 0))

# Part 2 score for each tree
for r in range(len(a)):
    for c in range(len(a[r])):
        s[r][c] = score(r, c)
        if s[r][c] > ans2:
            ans2 = s[r][c]

print(f"Part 1: {ans1}")
print(f"Part 2: {ans2}")

