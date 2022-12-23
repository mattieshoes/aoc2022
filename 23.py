#!/usr/bin/python3

# prints board. returns number of empty squares in the minimum bounding box for answer 1
def printboard():
    print()
    minrow = 999999
    maxrow = -999999
    mincol = 999999
    maxcol = -99999
    for e in elf:
        r = e[0]
        c = e[1]
        minrow = min(r, minrow)
        maxrow = max(r, maxrow)
        mincol = min(c, mincol)
        maxcol = max(c, maxcol)
    count = 0
    for row in range(minrow, maxrow + 1):
        for col in range(mincol, maxcol + 1):
            if (row, col) in elf:
                print("#", end="")
            else:
                print(".", end="")
                count += 1
        print()
    return count


# does turn.  Returns the number of moves made for part 2
def turn():
    global elf
    global checks
    global checks_off
    
    # do proposed moves calculations
    elflist = list(elf.keys())
    for e in elflist:
        row = e[0]
        col = e[1]
        dirs = []
        for direction in checks:
            found = False
            for offset in direction:
                if (row+offset[0], col+offset[1]) in elf:
                    found = True
            dirs.append(found)
        #print(f"Checks: {dirs}")
        if dirs[0] == False and dirs[1] == False and dirs[2] == False and dirs[3] == False:
            continue
        for idx, d in enumerate(dirs):
            if d == False:
                elf[(row, col)] = (row + checks_off[idx][0], col + checks_off[idx][1])
                break

    # resolve collisions
    collisions = {}
    for e in elflist:
        if elf[e] in collisions:
            collisions[elf[e]] += 1
        else:
            collisions[elf[e]] = 1
    for c in list(collisions.keys()):
        if collisions[c] == 1:
            del collisions[c]
    for e in elflist:
        if elf[e] in collisions:
            elf[e] = e

    # do moves
    newelf = {}
    count = 0
    for e in elflist:
        if elf[e] != e:
            count += 1
        newelf[elf[e]] = elf[e]
    elf = newelf
    r = checks.pop(0)
    checks.append(r)
    r = checks_off.pop(0)
    checks_off.append(r)
    return count

ans1 = 0
ans2 = 0

with open('23.txt') as f:
    data = f.read().rstrip('\n').split('\n')

# turn elves into a hash so I don't have to worry about bounding boxes or memory
elf = {}
for row, line in enumerate(data):
    for col in range(len(line)):
        if line[col] == '#':
            elf[(row, col)] = (row, col)

# checks for North, South, East, West
checks = [[(-1, -1), (-1, 0), (-1, 1)], \
          [(1, -1),  (1, 0),  (1, 1) ], \
          [(-1, -1), (0, -1), (1, -1)], \
          [(-1, 1),  (0, 1),  (1, 1)]]

# the offsets for the directions
checks_off = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# solve part 1 by iterating 10 times and finding empty squares
count = 0
for i in range(10):
    count = turn()
ans1 = printboard()
print(f"Part 1: {ans1}")

# solve part 2 by iterating until no elves move
rnd = 10
while count != 0:
    count = turn()
    print(f"Round: {rnd}, moves: {count}")
    rnd += 1
ans2 = rnd
print(f"Part 2: {ans2}")
