#!/usr/bin/python3

with open('1.txt') as f:
    lines = f.readlines()
lines = [line.rstrip('\n') for line in lines]

temp_sum = 0
calories = []
for line in lines:
    if not line:
        calories.append(temp_sum)
        temp_sum = 0
    else:
        temp_sum += int(line)
calories.append(temp_sum)
calories.sort(reverse=True)

print(f"Max: {calories[0]}")
print(f"Top Three: {sum(calories[:3])}")
