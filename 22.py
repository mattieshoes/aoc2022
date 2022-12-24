#!/usr/bin/python3


def printboard():
    print()
    for r in range(len(layout)):
        for c in range(len(layout[r])):
            if r == loc[0] and c == loc[1]:
                if facing == 0:
                    print(">", end="")
                elif facing == 1:
                    print("v", end="")
                elif facing == 2:
                    print("<", end="")
                else:
                    print("^", end="")
            else:
                print(f"{layout[r][c]}", end="")
        print()

def move(n):
    global loc
    row = loc[0]
    col = loc[1]
    offset = offsets[facing]
    last = [row, col]
    while n > 0:
        row = (row + offset[0]) % len(layout)
        col = (col + offset[1]) % len(layout[row])
        if layout[row][col] == ' ':
            continue
        elif layout[row][col] == '.':
            last = [row, col]
            n -= 1
        elif layout[row][col] == '#':
            loc = last
            return
    loc = last

def rotate(d):
    global facing
    if d == 'R':
        facing = (facing + 1) % 4
    else:
        facing = (facing - 1) % 4


ans1 = 0
ans2 = 0

with open('22.txt') as f:
    layout,instructions = f.read().rstrip('\n').split('\n\n')
layout = layout.split('\n')

max_row_length = 0
for row in layout:
    if len(row) > max_row_length:
        max_row_length = len(row)

for r in range(len(layout)):
    l = len(layout[r])
    diff = max_row_length - l
    layout[r] = layout[r] + ' ' * diff

loc = [0]
for n, s in enumerate(layout[0]):
    if s == '.':
        loc.append(n)
        break
facing = 0

directions = []
offsets = [[0, 1], [1, 0], [0, -1], [-1, 0]]
val = 0
for c in instructions:
    if c == 'R' or c == 'L':
        if val > 0:
            directions.append(val)
            val = 0
        directions.append(c)
    else:
        v = int(c)
        val = val * 10 + v
if val > 0:
    directions.append(val)

for d in directions:
    print(f"{loc} {facing} -- {d} -- ", end="")
    if d == 'R' or d == 'L':
        rotate(d)
    else:
        move(d)
    print(f"{loc} {facing}")
    #printboard()

ans1 = 1000 * (loc[0]+1) + 4 * (loc[1]+1) + facing

print(f"Part 1: {ans1}")
print(f"Part 2: {ans2}")

