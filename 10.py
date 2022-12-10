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

ans1 = 0

with open('10.txt') as f:
    data = recursive_split(f.read().rstrip('\n'), '\n', ' ')

X = [1]
cycle = 0
for line in data:
    if line[0] == 'addx':
        X.append(X[-1])
        X.append(X[-1])
        X[-1] += int(line[1])
    elif line[0] == 'noop':
        X.append(X[-1])

for i in range(20, 241, 40):
    ans1 += X[i-1]*i
print(f"Part 1: {ans1}")

screen = [' ' for i in range(241)]
for i in range(240):
    if abs(X[i] - (i%40)) < 2:
        screen[i] = '#'
for i in range(240):
    print(f"{screen[i]}", end='')
    if i%40 == 39:
        print()
