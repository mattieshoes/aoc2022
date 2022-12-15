#!/usr/bin/python3

import re

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

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

found = False
for x in range(4000000, -1, -1):
    y = 0
    while y < 4000001:
        loc = (x, y)
        max_ld = -999999
        for key in sensors.keys():
            ld = sensor_range[key] - distance(key, loc)
            if ld > max_ld:
                max_ld = ld
        if max_ld >= 0:
            y += max_ld + 1
            continue
        print(loc)
        ans2 = loc[0] * 4000000 + loc[1]
        found = True
        break
    if(found):
        break
            

print(f"Part 2: {ans2}")

