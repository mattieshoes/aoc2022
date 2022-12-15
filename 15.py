#!/usr/bin/python3

import re

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def check(point):
    if point[0] < 0 or point[0] > 4000000 or point[1] < 0 or point[1] > 4000000:
        return False
    for k in sensors.keys():
        if distance(k, point) <= sensor_range[k]:
            return False
    return True

ans1 = 0
ans2 = 0
sensors = {}
sensor_range = {}

with open('15.txt') as f:
    data = f.read().rstrip('\n').split('\n')

for line in data:
    n = re.findall(r'[0-9\-]+', line)
    sensors[(int(n[0]), int(n[1]))] = (int(n[2]), int(n[3]))

for k in sensors.keys():
    sensor_range[k] = distance(k, sensors[k])

y_val = 2000000
y_val = 10
nots = {}
for key in sensors.keys():
    dist = distance(key, sensors[key])
    d2y = distance(key, (key[0], y_val))
    leftover_dist = dist - d2y
    for x_val in range(key[0] - leftover_dist, key[0] + leftover_dist):
        nots[(x_val, y_val)] = 1
ans1 = len(nots) 
print(f"Part 1: {ans1}")
nots.clear()

potential = {}
for k1 in sensors.keys():
    for k2 in sensors.keys():
        if k1 == k2:
            continue
        a = k1[0], k1[1] - sensor_range[k1] - 1
        b = k2[0], k2[1] + sensor_range[k2] + 1
        offset = (b[0] - a[0], b[1]-a[1])
        diff = offset[1] - offset[0]
        if diff == 2:
            potential[k1] = 1

# build perimeter side with potential solution
seq = []
for k in potential.keys():
    r = sensor_range[k]
    p2 = (k[0] - r - 1, k[1])
    p3 = (k[0], k[1] + r + 1)
    seq.append([p2, p3])

# test against all other ranges
found = False
for s in seq:
    xoff = 1
    yoff = 1
    if s[1][0] < s[0][0]:
        xoff *= -1
    if s[1][1] < s[0][1]:
        yoff *= -1
    for x, y in zip(range(s[0][0], s[1][0] + xoff, xoff), range(s[0][1], s[1][1]+yoff, yoff)):
        if check((x, y)):
            found = True
            ans2 = x * 4000000 + y
            print(f"Part 2: {ans2}")
            break
    if found:
        break
