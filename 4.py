#!/usr/bin/python3

with open('4.txt') as f:
    groups = [g.split(',') for g in f.read().split('\n')]

ans1 = 0
ans2 = 0

for pair in groups:
    a = [int(n) for n in pair[0].split('-')]
    b = [int(n) for n in pair[1].split('-')]

    # a engulfs b
    if a[0] <= b[0] and a[1] >= b[1]:
        ans1 += 1;
    # b engulfs a
    elif a[0] >= b[0] and a[1] <= b[1]: # b engulfs a
        ans1 += 1;

    # count non-overlaps
    if a[1] < b[0] or a[0] > b[1]:
        ans2 += 1

#invert for ones that do overlap
ans2 = len(groups) - ans2 


print(f"Part 1: {ans1}")
print(f"Part 2: {ans2}")
