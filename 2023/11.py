import readInput

def getRowsAndColsToExpand(lines):
    rowsToExpand = []

    for i, line in enumerate(lines):
        if len(set(line)) == 1 and line[0] == ".":
            rowsToExpand.append(i)

    transposed = ["".join(s) for s in zip(*lines)]

    colsToExpand = []
    for i, line in enumerate(transposed):
        if len(set(line)) == 1 and line[0] == ".":
            colsToExpand.append(i)

    return (rowsToExpand, colsToExpand)

def sumDistances(galaxies):
    sumPaths = 0
    while len(galaxies) > 1:
        gal = galaxies.pop()
        for galComp in galaxies:
            sumPaths += abs(gal[0] - galComp[0]) + abs(gal[1] - galComp[1])
    return sumPaths

def getGalaxies(lines, factor, rte, cte):
    galaxies = []
    for ri, row in enumerate(lines):
        for ci, _ in enumerate(row):
            if lines[ri][ci] == "#":
                expandedRowCount = len(list(filter(lambda x : x < ri, rte)))
                expandedColCount = len(list(filter(lambda x : x < ci, cte)))
                r1 = expandedRowCount * factor + ri - expandedRowCount
                c2 = expandedColCount * factor + ci - expandedColCount
                galaxies.append((r1, c2))
    return galaxies

def solve():
    lines = readInput.linesToList("11")

    rowsToExpand, colsToExpand = getRowsAndColsToExpand(lines)

    galaxies1 = getGalaxies(lines, 2, rowsToExpand, colsToExpand)
    galaxies2 = getGalaxies(lines, 1_000_000, rowsToExpand, colsToExpand)

    print(sumDistances(galaxies1))
    print(sumDistances(galaxies2))

if __name__ == "__main__":
    solve()