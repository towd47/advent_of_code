import readInput

def applyMap(val, currMap):
    for x in currMap:
        if val >= x[1] and val < x[1] + x[2]:
            return val - x[1] + x[0]
    return val

def applyAllMaps(val, maps):
    for x in maps:
        val = applyMap(val, x)
    return val

def overlaps(r1, r2):
    remaining = []
    overlap = None
    maxStart = max(r1[0], r2[0])
    minEnd = min(r1[1], r2[1])
    if max(r1[0], r2[0]) <= min(r1[1], r2[1]):
        overlap = (maxStart, minEnd)
    if overlap:
        if r1[0] < maxStart:
            remaining.append((r1[0], maxStart - 1))
        if r1[1] > minEnd:
            remaining.append((minEnd + 1, r1[1]))
    return (overlap, remaining)

def applyMapR(rs, currMap):
    rLeft = rs
    rOut = []
    while rLeft:
        r = rLeft.pop()
        overFound = False
        remaining = []
        for x in currMap:
            over, remain = overlaps(r, (x[1], x[1] + x[2] - 1))
            if over:
                overFound = True
                overR = over[1] - over[0]
                diff = over[0] - x[1]
                rOut.append((x[0] + diff, x[0] + overR + diff))
            if remain:
                remaining.extend(remain)
        if not overFound:
            rOut.append(r)
        else:
            rLeft.extend(remaining)
            
    return rOut

def applyAllMapsR(seedR, maps):
    for x in maps:
        seedR = applyMapR(seedR, x)
    return min([x for (x, y) in seedR])
        

lines = readInput.yieldLines("5")

seeds = next(lines).strip().split(":")[1]
seeds = [int(x) for x in seeds.split()]

seedRanges = []
for i, e in enumerate(seeds):
    if i % 2 == 0:
        seedRanges.append((e, e + seeds[i+1] - 1))

maps = []

currentMap = []
for line in lines:
    line = line.strip()
    if not line:
        if currentMap:
            maps.append(currentMap)
            currentMap = []
    elif line[0].isdigit():
        currentMap.append([int(x) for x in line.split()])
if currentMap:
    maps.append(currentMap)



locs = []
for x in seeds:
    locs.append(applyAllMaps(x, maps))

print(min(locs))

locs2 = []
for x in seedRanges:
    locs2.append(applyAllMapsR([x], maps))

print(min(locs2))