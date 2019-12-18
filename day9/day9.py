relativeBase = 0

def evaluateIntcode(stack):
  newpointer = 0
  newstack = stack.copy()
  while newstack[newpointer] != 99:
    newstack, newpointer = stepIntcode(newstack, newpointer)
  print("Ran until HALT")
  return newstack

def stepIntcode(stack, pointer):
  instruction, mode = getInstructionMode(stack[pointer])
  result, newpointer = None, None
  newstack = stack.copy()
  i = 10
  while result is None and newpointer is None:
    try:
      result, newpointer = operations[instruction](newstack, pointer, mode)
    except IndexError:
      newstack += [0] * i
      i *= 10
  return result, newpointer

def getInstructionMode(instruction: int):
  instructionString = str(instruction)
  actualInstruction = int(instructionString[len(instructionString)-2:])
  mode = instructionString[0:len(instructionString)-2].zfill(3)
  mode = list(reversed([int(x) for x in mode]))
  return actualInstruction, mode

def getActualValue(stack, pointer, mode):
  global relativeBase
  value = None
  if mode == 0:
    value = stack[stack[pointer]]
  elif mode == 1:
    value = stack[pointer]
  elif mode == 2:
    value = stack[relativeBase + stack[pointer]]
  return value

def intAdd(stack, pointer, mode):
  result = stack.copy()
  value1 = getActualValue(stack, pointer+1, mode[0])
  value2 = getActualValue(stack, pointer+2, mode[1])

  if mode[2] == 0:
    result[result[pointer+3]] = value1 + value2
  if mode[2] == 2:
    global relativeBase
    result[relativeBase + result[pointer+3]] = value1 + value2
  return result, pointer+4

def intMultiply(stack, pointer, mode):
  result = stack.copy()
  value1 = getActualValue(stack, pointer+1, mode[0])
  value2 = getActualValue(stack, pointer+2, mode[1])

  if mode[2] == 0:
    result[result[pointer+3]] = value1 * value2
  elif mode[2] == 2:
    global relativeBase
    result[relativeBase + result[pointer+3]] = value1 * value2
  return result, pointer+4

def intInput(stack, pointer, mode):
    result = stack.copy()
    if mode[0] == 0:
      result[result[pointer+1]] = int(input("input: "))
    elif mode[0] == 2:
      global relativeBase
      result[relativeBase + result[pointer+1]] = int(input("input: "))
    return result, pointer+2

def intOutput(stack, pointer, mode):
    output = None
    if mode[0] == 0:
      output = stack[stack[pointer+1]]
    elif mode[0] == 1:
      output = stack[pointer+1]
    elif mode[0] == 2:
      global relativeBase
      output = stack[relativeBase + stack[pointer+1]]
    
    if output:
      print("DEBUG | " + str(output))
    else:
      print("TEST | " + str(output))
    return stack, pointer+2

def intJumpIfTrue(stack, pointer, mode):
  nextpointer = pointer + 3
  value1 = getActualValue(stack, pointer + 1, mode[0])
  value2 = getActualValue(stack, pointer + 2, mode[1])
  if value1 != 0:
    nextpointer = value2
  return stack, nextpointer

def intJumpIfFalse(stack, pointer, mode):
  nextpointer = pointer + 3
  value1 = getActualValue(stack, pointer + 1, mode[0])
  value2 = getActualValue(stack, pointer + 2, mode[1])

  if value1 == 0:
    nextpointer = value2

  return stack, nextpointer

def intLessthan(stack, pointer, mode):
  result = stack.copy()
  value1 = getActualValue(stack, pointer + 1, mode[0])
  value2 = getActualValue(stack, pointer + 2, mode[1])

  if mode[2] == 0:
    result[result[pointer+3]] = 1 if value1 < value2 else 0
  elif mode[2] == 2:
    global relativeBase
    result[relativeBase + result[pointer+3]] = 1 if value1 < value2 else 0
  return result, pointer + 4

def intEquals(stack, pointer, mode):
  result = stack.copy()
  value1 = getActualValue(stack, pointer + 1, mode[0])
  value2 = getActualValue(stack, pointer + 2, mode[1])

  if mode[2] == 0:
    result[result[pointer+3]] = 1 if value1 == value2 else 0
  elif mode[2] == 2:
    global relativeBase
    result[relativeBase + result[pointer+3]] = 1 if value1 == value2 else 0
  return result, pointer + 4

def intAdjustRelativeBase(stack, pointer, mode):
  global relativeBase
  value1 = getActualValue(stack, pointer + 1, mode[0])
  relativeBase += value1
  return stack, pointer+2

operations = [
  None,
  intAdd,
  intMultiply,
  intInput,
  intOutput,
  intJumpIfTrue,
  intJumpIfFalse,
  intLessthan,
  intEquals,
  intAdjustRelativeBase
]

stack = []
with open('input.txt', 'r') as f:
    for c in f.readlines()[0].strip().split(','):
        stack.append(int(c))

evaluateIntcode(stack)
