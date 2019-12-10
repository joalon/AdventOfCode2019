#!/usr/bin/env python
# -*- coding: utf-8 -*-


### Part 1 ###

inputRange = range(248345, 746315)

def matchesPassword(inp):

    adjecentDigits = False
    for num, c in enumerate(str(inp)):
        if num == 0:
            continue

        if int(c) < int(str(inp)[num-1]):
            return False

        if c == str(inp)[num-1]:
            adjecentDigits = True

    return adjecentDigits


result = []
for i in inputRange:
    res = matchesPassword(i)
    if res:
        result.append(i)

print("Part 1 solution is: " + str(len(result)))


