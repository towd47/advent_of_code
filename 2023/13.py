import readInput

def getPatterns():
    lines = readInput.yieldLines("13")

    patterns = []
    currentPattern = []

    for line in lines:
        line = line.strip()
        if line:
            currentPattern.append(line)
        else:
            patterns.append(currentPattern)
            currentPattern = []
    if currentPattern:
        patterns.append(currentPattern)
    
    return patterns

def isMirror(pattern, pos):
    p1 = pos
    p2 = pos + 1
    while p1 >= 0 and p2 < len(pattern):
        if pattern[p1] != pattern[p2]:
            return False
        p1 -= 1
        p2 += 1
    return True

def findMirror(pattern, ignore = -1):
    for i in range(len(pattern) - 1):
        if isMirror(pattern, i):
            score = (i + 1) * 100
            if score != ignore:
                return score
    pattern = ["".join(s) for s in zip(*pattern)]
    for i in range(len(pattern) - 1):
        if isMirror(pattern, i):
            score = i + 1
            if score != ignore:
                return score
    return -1

def flipBit(c):
    if c == ".":
        return "#"
    return "."

def findAdjustedMirror(pattern):
    originalMirrorScore = findMirror(pattern)
    score = -1
    x, y = (0, 0)
    while score == -1:
        adjustedPattern = pattern.copy()
        adjustedPattern[x] = adjustedPattern[x][:y] + flipBit(adjustedPattern[x][y]) + adjustedPattern[x][y+1:]
        score = findMirror(adjustedPattern, originalMirrorScore)
        y += 1
        if y == len(pattern[0]):
            y = 0
            x += 1
        if x == len(pattern):
            return originalMirrorScore
    return score
    


def p1(patterns):
    print(sum(map(findMirror, patterns)))

def p2(patterns):
    print(sum(map(findAdjustedMirror, patterns)))

def solve():
    patterns = getPatterns()
    p1(patterns)
    p2(patterns)

if __name__ == "__main__":
    solve()
