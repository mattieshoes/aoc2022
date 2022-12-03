#!/usr/bin/python3

with open('1.txt') as f:
    vals = sorted(sum((int(n) for n in m.split('\n'))) for m in f.read().split('\n\n'))

print(f"{vals[-1]}\n{sum(vals[-3:])}")
