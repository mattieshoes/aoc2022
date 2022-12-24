#!/usr/bin/python3


# finds cheapest node in set to expand
def find_cheapest(open_set):
    minCost = 9999999
    minKey = ()
    for k in open_set.keys():
        if open_set[k] < minCost:
            minCost = open_set[k]
            minKey = k
    return minKey

# ghetto A* type search  
def astar():
    while open_set:
        q = find_cheapest(open_set)
        closed_set[q] = open_set[q]
        del open_set[q]
        for move in moves:
            new_loc = (q[0] + move[0], q[1] + move[1], q[2] + 1)
            if len(boards) <= new_loc[2]:
                move_blizzards()
                boards.append(board)
            if new_loc[0] >= 0 and new_loc[0] < len(board) \
               and (not boards[new_loc[2]][new_loc[0]][new_loc[1]]):
                dist = abs(new_loc[0] - exit[0]) + abs(new_loc[1] - exit[1])
                if new_loc[0] == exit[0] and new_loc[1] == exit[1]:
                    return new_loc[2]
                elif new_loc not in closed_set:
                    open_set[new_loc] = new_loc[2] + dist

# for debugging
def print_board(n):
    print()
    for r in boards[n]:
        for c in r:
            if not c:
                print('.', end='')
            else:
                if len(c) == 1:
                    print(c[0], end = '')
                else:
                    print(len(c), end = '')
        print()

# moves blizzards one step forward on board.
# old board state is stored in a list, boards, so I don't have to un-update
def move_blizzards():
    global board
    # setup empty board
    new_board = []
    for r, row in enumerate(board):
        new_board.append([])
        for c, col in enumerate(row):
            new_board[-1].append([])

    # place items on new board
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            for i, item in enumerate(col):
                if item == '#':
                    new_board[r][c].append(item)
                else:
                    nr = (r + directions[item][0] - 1) % height + 1
                    nc = (c + directions[item][1] - 1) % width + 1
                    new_board[nr][nc].append(item)
    # switcheroo
    board = new_board


ans1 = 0
ans2 = 0

with open('24.txt') as f:
    data = f.read().rstrip('\n').split('\n')

# parse input into initial board state
# each square is a list of items so we can handle multiple items
# handy that empty lists (ie. empty squares) evaluate to False
board = []
for line in data:
    board.append([])
    for col, char in enumerate(line):
        board[-1].append([])
        if char != '.':
            board[-1][-1].append(char)

moves = [(1, 0), (0, 1), (0, 0), (0, -1), (-1, 0)]
directions  = {'v': (1, 0), '>': (0, 1), '#': (0, 0), '<': (0, -1), '^': (-1, 0)}
height = len(board) - 2
width = len(board[0]) - 2
loc = (0, 1, 0)
exit = (len(board) - 1, len(board[0]) - 2)
boards = [board]

# pathfind to end for Ans1
open_set = {loc: 0}
closed_set = {}
ans1 = astar()

print(f"Part 1: {ans1}")

# switch location and exit to pathfind back to the start
loc = (exit[0], exit[1], ans1)
exit = (0,1)
open_set = {loc: 0}
closed_set = {}
ans2 = astar()

# switch location and exit again to pathfind BACK to the end
loc = (0, 1, ans2)
exit = exit = (len(board) - 1, len(board[0]) - 2)
open_set = {loc: 0}
closed_set = {}
ans2 = astar()

print(f"Part 2: {ans2}")
