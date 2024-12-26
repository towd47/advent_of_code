from readInput import yieldLines
import re
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
arrowPrio2 = '<v^>'

def solve(filename='21'):
    lines = yieldLines(filename)
    lines = [line.strip() for line in lines]

    tot = 0
    tot25 = 0
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

        arrowpts = toParts(numSeq)
        for _ in range(2):
            arrowpts = arrowBotE(arrowpts)
        l = partLen(arrowpts)
        tot += calcVal(code, l)

        for _ in range(23):
            arrowpts = arrowBotE(arrowpts)
        l = partLen(arrowpts)
        tot25 += calcVal(code, l)
    print(tot)
    print(tot25)

def calcVal(code, l):
    return int(code[:-1]) * l

def partLen(parts):
    return sum([len(p) * parts[p] for p in parts])

def arrowBot(sequence):
    start = arrowMap['A']
    arrowSeq = ''
    for i, c in enumerate(sequence):
        end = arrowMap[c]
        if start != end:
            dirs = getDirs(start, end)
            if (start[0] == 0 or end[0] == 0) and (start[1] == 0 or end[1] == 0):
                prio = arrowPrio
            else:
                prio = arrowPrio2
            for p in prio:
                if p in dirs:
                    arrowSeq = arrowSeq + p * dirs[p]
            arrowSeq += 'A'
        else:
            arrowSeq += 'A'
        start = end
    return arrowSeq

def arrowBotE(parts):
    seq = ''
    nextParts = {}
    for p in parts:
        nextPart = arrowBot(p)
        nps = toParts(nextPart)
        for p1 in nps:
            if p1 in nextParts:
                nextParts[p1] += parts[p] * nps[p1]
            else:
                nextParts[p1] = parts[p] * nps[p1]
    return nextParts

def toParts(seq):    
    parts = {}
    matches = re.findall(r'[^A]*A', seq)
    for m in matches:
        if m in parts:
            parts[m] += 1
        else:
            parts[m] = 1
    return parts

def numMoves(p1, p2):
    dirs = list(getDirs(p1, p2).keys())
    presses = abs(p1[1] - p2[1]) + abs(p1[0] - p2[0])
    return dirs, presses + 1

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

