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
    a = set(line[:len(line)//2])
    b = set(line[len(line)//2:])
    overlap = a.intersection(b)
    for item in overlap:
        my_sum += priority(item)
print(f"Sum: {my_sum}")

my_sum = 0
for n in range(0, len(lines), 3):
    a = set(lines[n])
    b = set(lines[n+1])
    c = set(lines[n+2])
    overlap = a.intersection(b).intersection(c)
    for item in overlap:
        my_sum += priority(item)
print(f"Sum: {my_sum}")
