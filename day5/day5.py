#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Evaluation
def evaluateIntcode(stack):
    res = stepIntcode(stack, 0)
    while res[0][res[1]] != 99:
      res = stepIntcode(res[0], res[1])
    print("Ran until HALT")
    return res

def stepIntcode(stack, stackpointer):
    instruction, mode = getInstructionMode(stack[stackpointer])
#    print("Executing: " + str(instruction) + " " + str(stack[stackpointer:stackpointer+4]) + " in mode " + str(mode))
    result = operations[instruction][0](stack, stackpointer, mode)
    return (result, stackpointer + operations[instruction][1])

def getInstructionMode(instruction):
    return int(str(instruction)[len(str(instruction))-2:]), [int(x) for x in str(instruction)[0:len(str(instruction))-2]]

def intAdd(stack, pointer, mode):
    result = stack.copy()
    
    operand1, operand2 = None, None
    if not mode:
        operand1 = result[result[pointer+1]]
        operand2 = result[result[pointer+2]]
    else:
        if len(mode) == 1:
            if mode[0] == 1:
                operand1 = result[pointer+1]
            else:
                operand1 = result[result[pointer+1]]
            operand2 = result[result[pointer+2]]
        else:
            if mode[1] == 1:
                operand1 = result[pointer+1]
            else:
                operand1 = result[result[pointer+1]]

            if mode[0] == 1:
                operand2 = result[pointer+2] 
            else:
                operand2 = result[result[pointer+2]]

    result[result[pointer+3]] = operand1 + operand2
    return result

def intMultiply(stack, pointer, mode):
    result = stack.copy()

    operand1, operand2 = None, None
    if not mode:
        operand1 = result[result[pointer+1]]
        operand2 = result[result[pointer+2]]
    else:
        if len(mode) == 1:
            if mode[0] == 1:
                operand1 = result[pointer+1]
            else:
                operand1 = result[result[pointer+1]]
            operand2 = result[result[pointer+2]]
        else:
            if mode[1] == 1:
                operand1 = result[pointer+1]
            else:
                operand1 = result[result[pointer+1]]

            if mode[0] == 1:
                operand2 = result[pointer+2] 
            else:
                operand2 = result[result[pointer+2]]

    result[result[pointer+3]] = operand1 * operand2
    return result

def intInput(stack, pointer, mode):
    result = stack.copy()
    inp = int(input("input: "))
    result[result[pointer+1]] = inp
    return result

def intOutput(stack, pointer, mode):

    output = 0
    if not mode:
      output = stack[stack[pointer+1]]
    else:
      output = stack[pointer+1]

    if output:
      print("DEBUG | " + str(output))
    else:
      print("TEST | " + str(output))
    return stack

operations = {
    1: (intAdd, 4),
    2: (intMultiply, 4),
    3: (intInput, 2),
    4: (intOutput, 2)
}

stack = []
with open('input.txt', 'r') as f:
    for c in f.readlines()[0].strip().split(','):
        stack.append(int(c))

evaluateIntcode(stack)
