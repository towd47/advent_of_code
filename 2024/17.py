from readInput import yieldLines
import sys
import re

def solve(filename='17'):
    lines = yieldLines(filename)

    regA = re.search(r'(\d+)', next(lines)).group(0)
    regB = re.search(r'(\d+)', next(lines)).group(0)
    regC = re.search(r'(\d+)', next(lines)).group(0)

    next(lines)

    instructions = [int(x) for x in re.findall(r'\d', next(lines))]

    regs = {}
    regs['A'] = int(regA)
    regs['B'] = int(regB)
    regs['C'] = int(regC)

    print(','.join([str(d) for d in doInstructions(instructions, regs)]))
    
    instructions.reverse()
    a = instructions[0]
    possibilities = calcNext(a, instructions)
    minPoss = min(possibilities)
    instructions.reverse()
    print(minPoss)

def calcNext(val, ins):
    if not ins:
        return [val]
    poss = []
    for v in range(val * 8, val * 8 + 8):
        if calc(v) == ins[0]:
            poss.append(v)
    vals = [calcNext(v, ins[1:]) for v in poss]
    newVals = []
    [newVals.extend(v) for v in vals]
    return newVals

def calc(a):
    return ((a % 8) ^ 3 ^ ((a // (2 ** ((a % 8) ^ 3))) ^ 5)) % 8 

#     searching = True
#     startVal = 1
#     while searching and startVal < 100_000_000:
#         regs = setStartingRegs(startVal)
#         try:
#             out = doInstructionsMatch(instructions, regs)
#             if out:
#                 print(out[0], out[1])
#                 input()
#             # if out:
#             #     searching = False
#         except e:
#             print(e)
#             pass
#         if searching:
#             startVal += 1
#     print(startVal)
    
def setStartingRegs(val):
    regs = {}
    regs['A'] = val
    regs['B'] = 0
    regs['C'] = 0
    return regs

def doInstructions(instructions, regs):
    out = []
    pointer = 0
    while pointer < len(instructions):
        val = doOperator(instructions[pointer], instructions[pointer+1], out, regs)
        if val == None:
            pointer += 2
        else:
            pointer = val
            
    return out

# def doInstructionsMatch(instructions, regs):
#     states = set()
#     out = []
#     startVal = regs['A']
#     pointer = 0
#     states.add((str(instructions), regs['A'], regs['B'], regs['C'], pointer))
#     while pointer < len(instructions):
#         val = doOperator(instructions[pointer], instructions[pointer+1], out, regs)
#         if val == None:
#             pointer += 2
#         else:
#             pointer = val
#         if out != instructions[:len(out)]:
#             return 
#         if (str(instructions), regs['A'], regs['B'], regs['C'], pointer) in states:
#             return
#         states.add((str(instructions), regs['A'], regs['B'], regs['C'], pointer))
#     return startVal, out

def doOperator(op, opand, out, regs):
    match op:
        case 0:
            regs['A'] = regs['A'] // 2 ** comboValue(opand, regs)
        case 1:
            regs['B'] = regs['B'] ^ (opand % 8)
        case 2:
            regs['B'] = comboValue(opand, regs) % 8
        case 3:
            if regs['A'] != 0:
                return opand
        case 4:
            regs['B'] = regs['B'] ^ regs['C']
        case 5:
            out.append(comboValue(opand, regs) % 8)
        case 6:
            regs['B'] = regs['A'] // 2 ** comboValue(opand, regs)
        case 7:
            regs['C'] = regs['A'] // 2 ** comboValue(opand, regs)

def comboValue(opand, regs):
    match opand:
        case _ as x if 0 <= x < 4:
            return x
        case 4:
            return regs['A']
        case 5:
            return regs['B']
        case 6:
            return regs['C']
        case _:
            raise(f'invalid opand literal: {opand}')

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(sys.argv[1])
    else:
        solve()
