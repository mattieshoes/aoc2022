#!/usr/bin/python3

import re

# simple pattern match to find folders inside the given path
def folder_size(path):
    sum = 0
    for k in fs.keys():
        if re.match(path, k):
            sum += fs[k]
    folders[path] = sum

with open('7.txt') as f:
    data = f.read().rstrip('\n').split('\n')

# fs contains files, folders contains folders, location and dataloc are for input parsing
fs = {}
folders = {}
location = ''
dataloc = 0

# manual parsing
while(dataloc < len(data)):
    if re.match(r"\$ cd ", data[dataloc]):
        m = re.match(r"\$ cd (.*)$", data[dataloc])
        dataloc += 1
        if m.group(1) == '..':
            t = location.rstrip('/').split('/')
            t.pop()
            location = '/'.join(t)
            location += '/'
        elif m.group(1) == '/':
            location = '/'
        else:
            location += m.group(1) + '/'
    elif re.match(r"\$ ls", data[dataloc]):
        dataloc += 1
        while dataloc < len(data) and data[dataloc][0] != '$':
            if re.match(r"dir", data[dataloc]):
                m = re.match(r"dir (.*)$", data[dataloc])
                folders[location + m.group(1) + "/"] = 0
            else:
                m = re.match(r"(\d+) (.*)", data[dataloc])
                fs[location + m.group(2)] = int(m.group(1))
            dataloc += 1


# calculate all folder sizes
# part 1: sum of folders < 1e5
s = 0
lst = folders.keys()
for k in lst:
    folder_size(k)
    if folders[k] <= 1e5:
        s += folders[k]

print(f"Sum: {s}")

# Part 2, smallest folder larger than a given size
folders["/"] = 0
folder_size("/")
needed =  folders["/"] - int(4e7)
smallest = 9e7
for k in folders.keys():
    if folders[k] >= needed and folders[k] < smallest:
        smallest = folders[k]
print(f"Smallest: {smallest}")
