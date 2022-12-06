#!/usr/bin/python3


#with open('1.txt') as f:
#    elves = sorted(sum((int(n) for n in m.split('\n'))) for m in f.read().split('\n\n'))

with open('1.txt') as f:
    #split into elves based on double-newline
    elves = f.read().rstrip('\n').split('\n\n')

# Split each elf into items based on newline, so we have a list of lists
elves = [elf.split('\n') for elf in elves]

# Convert each item in each elf list into integers
elves = [[int(n) for n in elf] for elf in elves]

# replace the list of items with the sum of their values
# so we now have a list of sums instead of a list of lists
elves = [sum(elf) for elf in elves]

# sort the list of sums
elves.sort()

print(f"{elves[-1]}\n{sum(elves[-3:])}")
