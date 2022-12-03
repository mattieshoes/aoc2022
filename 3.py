#!/usr/bin/python3

def priority(n):
    if(n.isupper()):
        return ord(n)-ord('A') + 27
    return ord(n) - ord('a') + 1

with open('3.txt') as f:
    lines = f.readlines()
lines = [item.rstrip() for item in lines]

my_sum = 0
for line in lines:
    matching = set()
    n = len(line)//2
    for i in line[:n]:
        if i in line[n:]:
            matching.add(i)
    for item in matching:
        my_sum += priority(item)
print(f"Sum: {my_sum}")

my_sum = 0
for n in range(0, len(lines), 3):
    for i in lines[n]:
        if i in lines[n+1] and i in lines[n+2]:
           my_sum += priority(i)
           break
print(f"Sum: {my_sum}")
