#!/usr/bin/env python
# -*- coding: utf-8 -*-

inp = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        for char in line.strip():
            inp.append(int(char))

def getPattern(pattern, phase, length):
    newpattern = []

    i = 0
    while len(newpattern) < length+1:
        for unused in range(phase):
            newpattern.append(pattern[i])
        i = (i+1) % len(pattern)

    return newpattern[1:length+1]

result = []
for i in range(100):
    for i in range(1, len(inp)+1):
        pattern = getPattern([0,1,0,-1], i, len(inp))
        resultingint = abs(sum([x * y for x, y in zip(inp, pattern)]))
        resultingint = resultingint if len(str(resultingint)) == 1 else int(str(resultingint)[-1:])
        result.append(resultingint)
    inp = result.copy()
    result = []

print("Part 1 solution is: " + str(inp[0:8]))
