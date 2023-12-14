import readInput
from copy import deepcopy

def spin(platform):
    for _ in range(4):
        platform = tilt(platform) 
        platform = list(zip(*platform[::-1]))
        platform = [list(x) for x in platform]        
    return platform

def tilt(platform):
    for i, row in enumerate(platform):
        if i == 0:
            continue
        for j, _ in enumerate(row):
            if platform[i][j] == "O":
                newPos = moveUp((i, j), platform)
                platform[i][j] = "."
                platform[newPos[0]][newPos[1]] = "O"
    return platform
    
def moveUp(pos, platform):
    while pos[0] > 0 and platform[pos[0] - 1][pos[1]] == ".":
        pos = (pos[0] - 1, pos[1])
    return pos

def load(platform):
    loadTot = 0
    for i, row in enumerate(platform):
        for j, _ in enumerate(row):
            if platform[i][j] == "O":
                loadTot += len(platform) - i
    return loadTot

def platformToHashable(platform):
    return "".join(["".join(x) for x in platform])

def printPlatform(platform):
    for x in platform:
        print("".join(x))

def p1(platform):
    print(load(tilt(platform)))

def p2(platform):
    platformDict = dict()
    indexDict = dict()
    platHash = platformToHashable(platform)
    count = 0
    while platHash not in platformDict:
        indexDict[count] = deepcopy(platform)
        platformDict[platHash] = count
        count += 1
        platform = spin(platform)
        platHash = platformToHashable(platform)


    patternStart = platformDict[platHash]
    patternNum = count - patternStart

    patternPos = (1_000_000_000 - patternStart) % patternNum
    print(load(indexDict[patternPos + patternStart]))

def solve():
    platform = readInput.linesToList("14")
    platform = [list(s) for s in platform]

    platformP1 = deepcopy(platform)
    p1(platformP1)
    p2(platform)

if __name__ == "__main__":
    solve()