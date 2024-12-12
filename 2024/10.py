from readInput import linesToList
from coord import Coord 
import sys

def solve(filename='10'):
    grid = linesToList(filename)
    grid = [[int(x) for x in list(line)] for line in grid]
    p1(grid)
    p2(grid)

def p1(grid):
    startPts = []
    for i, e in enumerate(grid):
        for j, e2 in enumerate(e):
            if e2 == 0:
                startPts.append(Coord(i, j))

    rows = len(grid)
    cols = len(grid[0])
    tot = 0
    for pt in startPts:
        visitedCoords = set()
        ptsToVisit = [pt]
        while ptsToVisit:
            point = ptsToVisit.pop()
            visitedCoords.add(point)
            if point.val(grid) == 9:
                tot += 1
            else:
                adjacent = [c for c in point.adjacent() if c.inBounds(rows, cols)]
                for a in adjacent:
                    if a.val(grid) == point.val(grid) + 1:
                        if a in visitedCoords:
                            pass
                        else:
                            ptsToVisit.append(a)
                            visitedCoords.add(a)

    print(tot)

def p2(grid):
    startPts = []
    for i, e in enumerate(grid):
        for j, e2 in enumerate(e):
            if e2 == 0:
                startPts.append(Coord(i, j))

    print(sum([step(pt, grid) for pt in startPts]))


def step(currPos, grid):
    if currPos.val(grid) == 9:
        return 1

    adjacent = [pos for pos in currPos.adjacent() if pos.inBounds(len(grid), len(grid[0])) and pos.val(grid) == currPos.val(grid) + 1]
    if not adjacent:
        return 0

    return sum([step(pos, grid) for pos in adjacent])



if __name__ == '__main__':
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        solve(filename)
    else:
        solve()
