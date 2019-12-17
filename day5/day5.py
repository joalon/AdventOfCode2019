def evaluateIntcode(stack):
  newpointer = 0
  newstack = stack.copy()
  while newstack[newpointer] != 99:
    newstack, newpointer = stepIntcode(newstack, newpointer)
  print("Ran until HALT")
  return newstack

def stepIntcode(stack, stackpointer):
  instruction, mode = getInstructionMode(stack[stackpointer])
  result, newpointer = operations[instruction](stack, stackpointer, mode)
  return result, newpointer

def getInstructionMode(instruction: int):
  instructionString = str(instruction)
  actualInstruction = int(instructionString[len(instructionString)-2:])
  mode = instructionString[0:len(instructionString)-2].zfill(3)
  mode = list(reversed([int(x) for x in mode]))
  return actualInstruction, mode

def intAdd(stack, pointer, mode):
  result = stack.copy()
  
  value1, value2 = None, None
  if mode[0] == 0:
    value1 = result[result[pointer+1]]
  elif mode[0] == 1:
    value1 = result[pointer+1]

  if mode[1] == 0:
    value2 = result[result[pointer+2]]
  elif mode[1] == 1:
    value2 = result[pointer+2]

  result[result[pointer+3]] = value1 + value2
  return result, pointer+4

def intMultiply(stack, pointer, mode):
  result = stack.copy()

  value1, value2 = None, None
  if mode[0] == 0:
    value1 = result[result[pointer+1]]
  elif mode[0] == 1:
    value1 = result[pointer+1]

  if mode[1] == 0:
    value2 = result[result[pointer+2]]
  elif mode[1] == 1:
    value2 = result[pointer+2]
  result[result[pointer+3]] = value1 * value2
  return result, pointer+4

def intInput(stack, pointer, mode):
    result = stack.copy()
    result[result[pointer+1]] = int(input("input: "))
    return result, pointer+2

def intOutput(stack, pointer, mode):
    output = None
    if mode[0] == 1:
      output = stack[pointer+1]
    elif mode[0] == 0:
      output = stack[stack[pointer+1]]

    if output:
      print("DEBUG | " + str(output))
    else:
      print("TEST | " + str(output))
    return stack, pointer+2

def intJumpIfTrue(stack, pointer, mode):
  nextpointer = pointer + 3

  value1, value2 = None, None
  if mode[0] == 0:
    value1 = stack[stack[pointer+1]]
  elif mode[0] == 1:
    value1 = stack[pointer+1]

  if mode[1] == 0:
    value2 = stack[stack[pointer+2]]
  elif mode[1] == 1:
    value2 = stack[pointer+2]

  if value1 != 0:
    nextpointer = value2

  return stack, nextpointer

def intJumpIfFalse(stack, pointer, mode):
  nextpointer = pointer + 3

  value1, value2= None, None
  if mode[0] == 0:
    value1 = stack[stack[pointer+1]]
  elif mode[0] == 1:
    value1 = stack[pointer+1]

  if mode[1] == 0:
    value2 = stack[stack[pointer+2]]
  elif mode[1] == 1:
    value2 = stack[pointer+2]

  if value1 == 0:
    nextpointer = value2

  return stack, nextpointer

def intLessthan(stack, pointer, mode):
  result = stack.copy()

  value1, value2 = None, None
  if mode[0] == 0:
    value1 = result[result[pointer+1]]
  elif mode[0] == 1:
    value1 = result[pointer+1]

  if mode[1] == 0:
    value2 = result[result[pointer+2]]
  elif mode[1] == 1:
    value2 = result[pointer+2]

  result[result[pointer+3]] = 1 if value1 < value2 else 0
  return result, pointer + 4

def intEquals(stack, pointer, mode):
  result = stack.copy()

  value1, value2 = None, None
  if mode[0] == 0:
    value1 = result[result[pointer+1]]
  elif mode[0] == 1:
    value1 = result[pointer+1]

  if mode[1] == 0:
    value2 = result[result[pointer+2]]
  elif mode[1] == 1:
    value2 = result[pointer+2]

  result[result[pointer+3]] = 1 if value1 == value2 else 0

  return result, pointer + 4

operations = [
  None,
  intAdd,
  intMultiply,
  intInput,
  intOutput,
  intJumpIfTrue,
  intJumpIfFalse,
  intLessthan,
  intEquals
]

stack = []
with open('input.txt', 'r') as f:
    for c in f.readlines()[0].strip().split(','):
        stack.append(int(c))

evaluateIntcode(stack)
