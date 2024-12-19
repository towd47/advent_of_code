from readInput import yieldLines
from coord import Coord
import sys
import heapq

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
    print(len(coords))

    num = 1024
    dist = 0
    startpos = Coord(0, 0)
    endpos = Coord(70, 70)
    rows = 71
    cols = 71
    path = [startpos]
    while ptPop := bestFirstPath(startpos, endpos, rows, cols, walls, dist, path):
        pathset = set(path)
        blocked = False
        blockedPos = None
        while not blocked:
            c = coords[num]
            num += 1
            walls.add(c)
            if c in pathset:
                blocked = True
                blockedPos = path.index(c)
        dist = blockedPos - 1
        startPos = path[blockedPos - 1]
        path = path[:blockedPos]
    print(coords[num - 1])


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

def bestFirstPath(startpos, endpos, rows, cols, walls, dist, path):
    pts = []
    heapq.heappush(pts, (priority(startpos, endpos, dist), startpos, dist, path))
    while pts:
        ptPop = heapq.heappop(pts)
        _, pt, dist, path = ptPop
        adj = [adj for adj in pt.adjacent() if adj not in walls and adj.inBounds(rows, cols)]
        for a in adj:
            if a == endpos:
                return ptPop
            heapq.heappush(pts, (priority(a, endpos, dist + 1), a, dist + 1, path + [a]))

    return None

def priority(pos, endpos, steps):
    return abs(pos.row - endpos.row) + abs(pos.col - endpos.col) + steps

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(sys.argv[1])
    else:
        solve()
