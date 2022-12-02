#!/usr/bin/python3

with open('2.txt') as f:
    lines = f.readlines()
lines = [line.rstrip('\n') for line in lines]

score = 0
alt_score = 0
for line in lines:
    letters = line.split(" ")
    vals = [ord(letters[0]) - ord('A'), ord(letters[1]) - ord('X')]
    result = (vals[1] - vals[0] + 1) % 3
    score += vals[1] + 1 + result * 3
    throw = (vals[0] + vals[1] - 1) % 3
    alt_score += vals[1] * 3 + throw + 1

print(f"Score: {score}")
print(f"Alt score: {alt_score}")
