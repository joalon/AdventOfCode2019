#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


### Part 1 ###

part1 = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        x = math.floor(float(line.strip()) / 3) - 2
        part1.append(x)

print("Part 1 solution: " + str(sum(part1)))


### Part 2 ###

def calculateFuel(module):
    return math.floor(module / 3) - 2

def calculateTotalFuel(module):
    requiredFuel = calculateFuel(module)
    moduleFuel = [requiredFuel]

    while (requiredFuel := calculateFuel(requiredFuel)) > 0:
        moduleFuel.append(requiredFuel)

    return sum(moduleFuel)

part2 = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        x = calculateTotalFuel(float(line.strip()))
        part2.append(x)

print("Part 2 solution: " + str(sum(part2)))

