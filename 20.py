#!/usr/bin/python3

ans1 = 0
ans2 = 0

with open('20.txt') as f:
    data = [int(line) for line in f.read().rstrip('\n').split('\n')]

order = []
orig = []
for idx, line in enumerate(data):
    orig.append(line)
    order.append(idx)

for idx, val in enumerate(orig):
    cur_loc = order.index(idx)                          # moving idx at location cur_loc
    order = order[:cur_loc] + order[cur_loc + 1:]       # removing from ordered list
    new_loc = (cur_loc + val) % len(order)              # finding new location
    order = order[:new_loc] + [idx] + order[new_loc:]   # slotting it in

ans1 = orig[order[(order.index(orig.index(0)) + 1000) % len(order)]] + \
       orig[order[(order.index(orig.index(0)) + 2000) % len(order)]] + \
       orig[order[(order.index(orig.index(0)) + 3000) % len(order)]]
print(f"Part 1: {ans1}")



order = []
orig = []
for idx, line in enumerate(data):
    orig.append(line * 811589153)
    order.append(idx)

for s in range(10):
    for idx, val in enumerate(orig):
        cur_loc = order.index(idx)                          # moving idx at location cur_loc
        order = order[:cur_loc] + order[cur_loc + 1:]       # removing from ordered list
        new_loc = (cur_loc + val) % len(order)              # finding new location
        order = order[:new_loc] + [idx] + order[new_loc:]   # slotting it in

ans2 = orig[order[(order.index(orig.index(0)) + 1000) % len(order)]] + \
       orig[order[(order.index(orig.index(0)) + 2000) % len(order)]] + \
       orig[order[(order.index(orig.index(0)) + 3000) % len(order)]]

print(f"Part 2: {ans2}")

