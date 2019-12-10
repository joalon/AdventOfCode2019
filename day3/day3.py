#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import namedtuple

Point = namedtuple('Point', 'x y')

def getAllPoints(stringList):

    start = Point(0, 0)
    steplist = [start]

    for ind in stringList:
        for step in range(int(ind[1:])):
            if ind[0] == 'U':
                start = Point(start.x, start.y + 1)
                steplist.append(start)
            elif ind[0] == 'D':
                start = Point(start.x, start.y - 1)
                steplist.append(start)
            elif ind[0] == 'L':
                start = Point(start.x - 1, start.y)
                steplist.append(start)
            elif ind[0] == 'R':
                start = Point(start.x + 1, start.y)
                steplist.append(start)

    return steplist

def getIntersectingPoints(line1, line2):
    return list(set(line1).intersection(set(line2)))

with open('input.txt', 'r') as f:

    lines = f.readlines()

    line1 = getAllPoints(lines[0].rstrip().split(','))
    line2 = getAllPoints(lines[1].rstrip().split(','))

    intersections = getIntersectingPoints(line1, line2)

    distances = [abs(t.x) + abs(t.y) for t in intersections] 
    distances.remove(0)

    print("Part 1 answer is: " + str(min(distances)))

