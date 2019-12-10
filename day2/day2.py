#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Part 1 ###

def splitInstr(flat_list):
    result = []

    i = 0
    running = True
    while running:
        if flat_list[i] != 99:
            result.append(flat_list[i:i+4])
            i += 4
        else:
            result.append([flat_list[i]])
            i += 1
            running = False

    return result


def solvePart1(string_list):
    data = [int(f) for f in string_list]
    chunks = splitInstr(data)

    variables = [1 for x in range(150)]

    for instr in chunks:
        if instr[0] == 1:
            variables[instr[3]] = variables[instr[1]] + variables[instr[2]]
        if instr[0] == 2:
            variables[instr[3]] = variables[instr[1]] * variables[instr[2]]

    print(variables)


with open('input.txt', 'r') as f:
    data = f.readline().strip().split(',')

    solvePart1(data)

### Part 2 ###


### ... solved it but don't remember how!?
