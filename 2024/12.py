from readInput import linesToList
import sys
from coord import Coord

def solve(filename='12'):
    grid = [list(line) for line in linesToList(filename)]
    
    visitedSet = set()
    areas = []

    for row, line in enumerate(grid):
        for col, val in enumerate(line):
            c = Coord(row, col)
            if c not in visitedSet:
                area = findArea(Coord(row, col), grid)
                visitedSet.update(area)
                areas.append(area)

    print(sum([calcPrice(a, grid) for a in areas]))

    
def findArea(pt, grid):
    area = set()
    area.add(pt)
    ptsToCheck = [pt]

    while ptsToCheck:
        pt = ptsToCheck.pop()
        adj = pt.adjacent()
        adj = [a for a in adj if not a in area and a.inBounds(len(grid), len(grid[0])) and a.val(grid) == pt.val(grid)]
        ptsToCheck.extend(adj)
        area.update(adj)

    return area

def calcPrice(area, grid):
    rows = len(grid)
    cols = len(grid[0])
    edges = 0
    for pt in area:
        adj = [a for a in pt.adjacent() if not a.inBounds(rows, cols) or a.val(grid) != pt.val(grid)]
        edges += len(adj)
    return edges * len(area)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(sys.argv[1])
    else:
        solve()
