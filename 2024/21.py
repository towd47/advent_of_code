from readInput import yieldLines
import sys

buttonMap = {}
buttonMap['7'] = (0, 0)
buttonMap['8'] = (0, 1)
buttonMap['9'] = (0, 2)
buttonMap['4'] = (1, 0)
buttonMap['5'] = (1, 1)
buttonMap['6'] = (1, 2)
buttonMap['1'] = (2, 0)
buttonMap['2'] = (2, 1)
buttonMap['3'] = (2, 2)
buttonMap['0'] = (3, 1)
buttonMap['A'] = (3, 2)
buttonPrio = '^>v<'
buttonPrio2 = '<v^>'

arrowMap = {}
arrowMap['^'] = (0, 1)
arrowMap['A'] = (0, 2)
arrowMap['<'] = (1, 0)
arrowMap['v'] = (1, 1)
arrowMap['>'] = (1, 2)
arrowPrio = 'v><^'
arrowPrio2 = '<^v>'

def solve(filename='21'):
    lines = yieldLines(filename)
    lines = [line.strip() for line in lines]

    tot = 0
    for code in lines:
        print(code)
        start = buttonMap['A']
        numSeq = ''
        for c in code:
            end = buttonMap[c]
            dirs = getDirs(start, end)
            if (start[0] == 3 or end[0] == 3) and (start[1] == 0 or end[1] == 0):
                prio = buttonPrio
            else:
                prio = buttonPrio2
            for p in prio:
                if p in dirs:
                    numSeq = numSeq + p * dirs[p]
            numSeq = numSeq + 'A'
            start = end
        print(numSeq)

        start = arrowMap['A']
        arrowSeq = ''
        for c in numSeq:
            end = arrowMap[c]
            if start != end:
                dirs = getDirs(start, end)
                for p in arrowPrio:
                    if p in dirs:
                        arrowSeq = arrowSeq + p * dirs[p]
                arrowSeq += 'A'
            else:
                arrowSeq += 'A'
            start = end

        print(arrowSeq)

        start = arrowMap['A']
        arrowSeq1 = ''
        for c in arrowSeq:
            end = arrowMap[c]
            if start != end:
                dirs = getDirs(start, end)
                for p in arrowPrio:
                    if p in dirs:
                        arrowSeq1 = arrowSeq1 + p * dirs[p]
                arrowSeq1 += 'A'
            else:
                arrowSeq1 += 'A'
            start = end
        print(arrowSeq1)
        print(len(arrowSeq1))
        val = int(code[:-1])
        tot += val * len(arrowSeq1)
    print(tot)

def arrowBot(sequence):
    start = arrowMap['A']
    arrowSeq = ''
    for c in sequence:
        end = arrowMap[c]
        if start != end:
            dirs = getDirs(start, end)
            for p in arrowPrio:
                if p in dirs:
                    arrowSeq = arrowSeq + p * dirs[p]
            arrowSeq += 'A'
        else:
            arrowSeq += 'A'
        start = end
    return arrowSeq



def numMoves(p1, p2):
    dirs = list(getDirs(p1, p2).keys())
    presses = abs(p1[1] - p2[1]) + abs(p1[0] - p2[0])
    return dirs, presses + 1

def optimizeNumPad(code):
    buttons = []
    buttonMap = {}
    buttonMap['1'] = (0, 0)
    buttonMap['2'] = (0, 1)
    buttonMap['3'] = (0, 2)
    buttonMap['4'] = (1, 0)
    buttonMap['5'] = (1, 1)
    buttonMap['6'] = (1, 2)
    buttonMap['7'] = (2, 0)
    buttonMap['8'] = (2, 1)
    buttonMap['9'] = (2, 2)
    buttonMap['0'] = (3, 1)
    buttonMap['A'] = (3, 2)

    start = buttonMap['A']
    for b in code:
        end = buttonMap[b]
        dirs = getDirs(start, end)
        order = '^>v<'
        buttons.append(dirs, order)

    return buttons
    
def optimizeArrowPad(buttons):
    arrows = []
    buttonMap = {}
    buttonMap['^'] = (0, 1)
    buttonMap['A'] = (0, 2)
    buttonMap['<'] = (1, 0)
    buttonMap['v'] = (1, 1)
    buttonMap['>'] = (1, 2)

    start = buttonMap['A']
    order = 'v>^<'
    for b in buttons:
        ds, ors = b
        for o in ors:
            pass
            if o in ds:
                end = buttonMap[o[0]]
                dirs = getDirs(start, end)
                dirsb = getDirs(end, start)
                p = ds[o[0]]
                end = buttonMap[o[1]]
                dirs2 = getDirs(start, end)
                dirs2b = getDirs(end, start)
                p2 = ds[o[1]]
        else:
            for k in ds:
                pass


def getDirs(p1, p2):
    dirs = {}
    if p1[0] > p2[0]:
        dirs['^'] = p1[0] - p2[0]
    elif p1[0] < p2[0]:
        dirs['v'] = p2[0] - p1[0]
    if p1[1] > p2[1]:
        dirs['<'] = p1[1] - p2[1]
    elif p1[1] < p2[1]:
        dirs['>'] = p2[1] - p1[1]
    return dirs

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(sys.argv[1])
    else:
        solve()


# Number pad Robot
#     per button in code:
#         manhattan distance moves
#         1 or 2 directions
#         one press
#         represent as (directions[], mdist moves + 1)
#         mdist moves + 1 is the number of inputs to this bot
# 
# Arrow Robot #1 -> button robot
#     mdist moves from a -> d1
#     if d2, mdist moves from d1 -> d2
#     mdist moves from d1 or d2 -> a
#     
#     moves = mdist above sum
#     presses = presses from above + mdist sum
# 
# arrow robot #2 -> ar #1
    



# ex:
#     press 1
#     numpad needs input
#         ^^^<<a
#     arrow robot 1 needs input
#         <aaav<aa>>^a
#     arrow robot 2 needs input
#         v<<a>>^aaa<av<a>>^aavaa<^a>a
        
# 379A
# v<<A>>^AvA^Av<<A>>^AAv<A<A>>^AAvAA^<A>Av<A>^AA<A>Av<A<A>>^AAAvA^<A>A
# <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
# ---<---A->-A---<---AA--v-<---AA->>--^-A--v--AA-^-A--v-<---AAA->--^-A
# ---<---A->-A--v-<<---AA->--^-AA->-A--v--AA-^-A---<-v--AAA->--^-A
# -------^---A-------^^--------<<-------A----->>---A--------vvv------A
# -------^---A---------<<------^^---A----->>---A--------vvv------A
# -----------3--------------------------7----------9-----------------A
# -----------3----------------------7----------9-----------------A
