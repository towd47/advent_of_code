from readInput import yieldLines
from coord import Coord
import sys

def solve(filename='18'):
    lines = yieldLines(filename)

    coords = []
    for line in lines:
        col, row = line.strip().split(',')
        col = int(col)
        row = int(row)
        coords.append(Coord(row, col))

    walls = set()
    [walls.add(c) for c in coords[:1024]]

    steps = stepsToFinish(Coord(0, 0), Coord(70, 70), 71, 71, walls)

    print(steps)

def stepsToFinish(startpos, endpos, rows, cols, walls):
    currpos = startpos
    ptsToCheck = [(currpos, 0)]
    visited = set()
    visited.add(currpos)
    while ptsToCheck:
        pt, dist = ptsToCheck.pop(0)
        visited.add(pt)
        adj = [adj for adj in pt.adjacent() if adj not in walls and adj not in visited and adj.inBounds(rows, cols)]
        for a in adj:
            if a == endpos:
                return dist + 1
            visited.add(a)
            ptsToCheck.append((a, dist + 1))
    return None

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(sys.argv[1])
    else:
        solve()
