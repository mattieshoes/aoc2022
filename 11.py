#!/usr/bin/python3

import re
from copy import deepcopy

def recursive_split(x, *args):
    y = []
    x = x.split(args[0])
    for part in x:
        if len(args) > 1:
            y += [recursive_split(part, *args[1:])]
        else:
            y += [part]
    return y


def round(part=1):
    for monkey in range(len(data)):
        while len(items[monkey]) > 0:
            count[monkey] += 1
            item = items[monkey].pop(0)
            item = pow(item, op_pow[monkey]) * op_mult[monkey] + op_add[monkey]
            if part == 1:
                item = item // 3
            if item % test_div[monkey] == 0:
                items[test_true[monkey]].append(item)
            else:
                items[test_false[monkey]].append(item)
        for i in range(len(data)):
            for j in range(len(items[i])):
                items[i][j] = items[i][j] % magic_number


with open('11.ex') as f:
    data = recursive_split(f.read().rstrip('\n'), '\n\n', '\n')
items = [[] for i in range(len(data))]
op_add = [0 for i in range(len(data))]
op_mult = [1 for i in range(len(data))]
op_pow = [1 for i in range(len(data))]
test_div = [0 for i in range(len(data))]
test_true = [0 for i in range(len(data))]
test_false = [0 for i in range(len(data))]
count = [0 for i in range(len(data))]
count2 = [0 for i in range(len(data))]

for monkey in range(len(data)):
    for line in data[monkey]:
        if re.match(r'\s*Starting items:', line):
            v = re.findall(r'\d+', line)
            for m in v:
                items[monkey].append(int(m))
        elif re.match(r'\s*Operation:', line):
            v = re.findall(r'\d+', line)
            if(len(v) == 0):
                op_pow[monkey] = 2
            else:
                if re.search(r'\+', line):
                    op_add[monkey] = int(v[0])
                else:
                    op_mult[monkey] = int(v[0])
        elif re.match(r'\s*Test:', line):
            v = re.findall(r'\d+', line)
            test_div[monkey] = int(v[0])
        elif re.match(r'\s*If true:', line):
            v = re.findall(r'\d+', line)
            test_true[monkey] = int(v[0])
        elif re.match(r'\s*If false:', line):
            v = re.findall(r'\d+', line)
            test_false[monkey] = int(v[0])

ans1 = 0
ans2 = 0

# lcm of divisor tests, used to keep anxiety numbers from growing forever
# (lcm because they're all prime, so no need to find something better)
magic_number = 1
for i in test_div:
    magic_number *= i

items2 = deepcopy(items)

# Part 1
for i in range(20):
    round(part=1)
count.sort()
ans1 = count[-1] * count[-2]
print(f"Part 1: {ans1}")

count = count2
items = items2
# Part 2
for i in range(10000):
    round(part=2)
count.sort()
ans2 = count[-1] * count[-2]
print(f"Part 2: {ans2}")

