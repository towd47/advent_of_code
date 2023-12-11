import readInput



lines = readInput.linesToList("11")

expandedHLines = []

for line in lines:
    line = line.strip()
    if len(set(line)) == 1 and line[0] == ".":
        expandedHLines.append(line)
    expandedHLines.append(line)

transposed = ["".join(s) for s in zip(*expandedHLines)]

expandedSpace = []
for line in transposed:
    if len(set(line)) == 1 and line[0] == ".":
        expandedSpace.append(line)
    expandedSpace.append(line)

expandedSpace = ["".join(s) for s in zip(*expandedSpace)]

galaxies = []
for ri, row in enumerate(expandedSpace):
    for ci, col in enumerate(row):
        if expandedSpace[ri][ci] == "#":
            galaxies.append((ri, ci))

def sumDistances(galaxies):
    sumPaths = 0
    while len(galaxies) > 1:
        gal = galaxies.pop()
        for galComp in galaxies:
            sumPaths += abs(gal[0] - galComp[0]) + abs(gal[1] - galComp[1])
    return sumPaths

print(sumDistances(galaxies))