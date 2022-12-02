#!/usr/bin/python3

with open('1.txt') as f:
    vals = sorted([sum([int(n) for n in line.split('\n')]) for line in f.read().split('\n\n')], reverse=True)

print(f"{vals[0]}\n{sum(vals[:3])}")
