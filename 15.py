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


for k in sensors.keys():
    sensor_range[k] = distance(k, sensors[k])


# build sequence of edges 
seq = []
for k in sensors.keys():
    r = sensor_range[k]
    p0 = (k[0] + r + 1, k[1])
    p1 = (k[0], k[1] - r - 1)
    p2 = (k[0] - r - 1, k[1])
    p3 = (k[0], k[1] + r + 1)
    seq.append([p0, p1])
    seq.append([p1, p2])
    seq.append([p2, p3])
    seq.append([p3, p0])

# test one past edge against all other ranges
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


