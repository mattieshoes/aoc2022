#!/usr/bin/python3

def find_start(data, n):
    for i in range(n, len(data)+1):
        if len(set(data[i-n:i])) == n:
            return i

with open('6.txt') as f:
    data = f.read().rstrip('\n')

print(find_start(data, 4))
print(find_start(data, 14))
