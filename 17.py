#!/usr/bin/python3

from copy import deepcopy

# Finds max height of the stack
# Also clears out old bits far from the top
def maxHeight():
    global prev_max_height
    if len(board) == 0:
        return -1
    max_height = prev_max_height
    for k in list(board.keys()):
        if k[0] > max_height:
            max_height = k[0]
        if k[0] + 100 < max_height:
            del board[k]
    prev_max_height = max_height
    return max_height

# was used for debugging step 1
def printboard():
    h = maxHeight()
    for r in range(h, -1, -1):
        row = [' ' for i in range(7)]
        for k in board.keys():
            if k[0] == r:
                row[k[1]] = '#'
        line = '|' + ''.join(row) + '|'
        print(line)
    print("---------")
    
#moves a piece on the board
def move(shape, xoff, yoff):
    ns = {}
    for k in shape.keys():
        r = k[0] + yoff
        c = k[1] + xoff
        ns[(r, c)] = 1

    for k in ns.keys():
        if k[0] < 0 or k[1] < 0 or k[1] > 6:
            return [False, shape]
        for m in board.keys():
            if k == m:
                return [False, shape]
    return [True, ns]

# drops a new piece
def drop(shape):
    global tick
    mh = maxHeight()
    [result, shape] = move(shape, 2, mh + 4)

    while(result):
        d = data[tick % len(data)]
        if d == '<':
            [result, shape] = move(shape, -1, 0)
        elif d == '>':
            [result, shape] = move(shape, 1, 0)
        tick += 1
        [result, shape] = move(shape, 0, -1)

    for k in shape.keys():
        board[k] = 1

ans1 = 0
ans2 = 0

with open('test.txt') as f:
    data = f.read().rstrip('\n')

shapes = []
s = {(0,0): '#', (0,1): '#', (0,2): '#', (0,3): '#'}
shapes.append(s)
s = {(0,1): '#', (1,0): '#', (1,1): '#', (1,2): '#', (2,1): '#'}
shapes.append(s)
s = {(0,0): '#', (0,1): '#', (0,2): '#', (1,2): '#', (2,2): '#'}
shapes.append(s)
s = {(0,0): '#', (1,0): '#', (2,0): '#', (3,0): '#'}
shapes.append(s)
s = {(0,0): '#', (0,1): '#', (1,0): '#', (1,1): '#'}
shapes.append(s)

board = {}
tick = 0
cycle = {}
dropped = 0
prev_max_height = 0

# first manually does part 1
while dropped < 2022:
    drop(shapes[dropped % len(shapes)])
    dropped += 1
    k = (tick % len(data), dropped % len(shapes))
    mh = maxHeight()
    if k in cycle:
        cycle[k].append( (dropped, mh) )
    else:
        cycle[k] = [(dropped, mh)]
    print(f"Dropped: {dropped}   Height: {mh + 1} K: {k}")

ans1 = maxHeight() + 1

# Then does part 2 looking for cycles
# if we're on the same spot in the input and dropping the same piece, stores
# if we've hit that spot 3 times and the difference in heights and pieces dropped
# were the same the last two times, assume we've fallen into a stable cycle
# and skip ahead N cycles
drop_cycle_length = 0
height_cycle_length = 0
bonus_height = 0
bonus_cycles = 0
while dropped < 1000000000000:
    # check for cycle
    k = (tick % len(data), dropped % len(shapes))

    if k in cycle and len(cycle[k]) >= 3 and bonus_cycles == 0 and \
            cycle[k][-1][0] - cycle[k][-2][0] == cycle[k][-2][0] - cycle[k][-3][0] and \
            cycle[k][-1][1] - cycle[k][-2][1] == cycle[k][-2][1] - cycle[k][-3][1]:
        drop_cycle_length = cycle[k][-1][0] - cycle[k][-2][0]
        height_cycle_length = cycle[k][-1][1] - cycle[k][-2][1]
        bonus_cycles = (1000000000000 - dropped) // drop_cycle_length
        bonus_height = height_cycle_length * bonus_cycles
        bonus_dropped = bonus_cycles * drop_cycle_length
        dropped += bonus_dropped
        print(f"Drop cycle length: {drop_cycle_length}")
    else:    
        drop(shapes[dropped % len(shapes)])
        dropped += 1
    
    # add to cycle
    if bonus_height == 0:
        mh = maxHeight()
        k = (tick % len(data), dropped % len(shapes))
        if k in cycle:
            cycle[k].append( (dropped, mh) )
        else:
            cycle[k] = [(dropped, mh)]
    
    print(f"Dropped: {dropped}   Height: {maxHeight() + bonus_height + 1} K: {k}")

ans2 = maxHeight() + bonus_height + 1
print(f"Part 1: {ans1}")
print(f"Part 2: {ans2}")

