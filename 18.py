#!/usr/bin/python3

# searches the square around the weird 3d shape, counting times it encounters the 3d shape
# ie. missing the internal, unreachable bubbles
def search():
    global ans2
    while len(unvisited) > 0:
        s, _ = unvisited.popitem()
        visited[s] = 1
        for dim in range(3):
            for offset in [-1, 1]:
                vals = list(s)
                vals[dim] += offset
                nk = tuple(vals)
                if nk[0] < minval[0] or nk[1] < minval[1] or nk[2] < minval[2] or \
                   nk[0] > maxval[0] or nk[1] > maxval[1] or nk[2] > maxval[2]:
                    continue
                if nk in drops:
                    ans2 += 1
                elif nk not in visited and nk not in unvisited:
                    unvisited[nk] = 1
                    
                

def recursive_split(x, *args):
    y = []
    x = x.split(args[0])
    for part in x:
        if len(args) > 1:
            y += [recursive_split(part, *args[1:])]
        else:
            y += [part]
    return y

ans1 = 0
ans2 = 0

with open('18.txt') as f:
    data = recursive_split(f.read().rstrip('\n'), '\n', ',')

# throw data into a hash with an (x, y, z) tuple for keys
drops = {}
for line in data:
    x, y, z = int(line[0]), int(line[1]), int(line[2])
    drops[(x,y,z)] = 1

# part 1 solution
sa = 0
for key in drops.keys():
    for dim in range(0, 3):
        for offset in [-1, 1]:
            n = [key[0], key[1], key[2]]
            n[dim] += offset
            m = tuple(n)
            if m not in drops:
                ans1 += 1
print(f"Part 1: {ans1}")


# part 2 solution.
# define bounds of the 3d shape
minval = [999, 999, 999]
maxval = [-999, -999, -999]
for key in drops.keys():
    for dim in range(0, 3):
        if key[dim] < minval[dim]:
            minval[dim] = key[dim]
        if key[dim] > maxval[dim]:
            maxval[dim] = key[dim]
# make the cuboid bigger so it includes a boundary layer
for i in range(3):
    minval[i] -= 1
    maxval[i] += 1

# search from outside the shape
visited = {}
unvisited = {}
unvisited[(minval[0], minval[1], minval[2])] = 1
search()

print(f"Part 2: {ans2}")

