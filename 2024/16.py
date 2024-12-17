from readInput import yieldLines
from coord import Coord
import sys
import heapq

def solve(filename='16'):
    grid = [list(line.strip()) for line in yieldLines(filename)]

    walls = set()
    for row, line in enumerate(grid):
        for col, val in enumerate(line):
            if val == '#':
                walls.add(Coord(row, col))
            elif val == 'S':
                startPos = Coord(row, col)
            elif val == 'E':
                endPos = Coord(row, col)

    facing = '>'

    print(p1(startPos, endPos, facing, walls, grid))

def p1(startPos, endPos, facing, walls, grid):
    pq = []
    score = 0
    visited = set()
    visited.add(startPos)
    heapq.heappush(pq, (priorityCalc(startPos, endPos, score), (startPos, facing, score)))
    
    while pq:
        pt, facing, score = heapq.heappop(pq)[1]
        if pt == endPos:
            return score
        adj = [adj for adj in pt.adjacent() if adj not in walls and adj not in visited]
        for a in adj:
            if getByFacing(pt, a) == facing:
                newScore = score + 1
                heapq.heappush(pq, (priorityCalc(a, endPos, newScore), (a, facing, newScore)))
            else:
                newScore = score + 1001
                heapq.heappush(pq, (priorityCalc(a, endPos, newScore), (a, getByFacing(pt, a), newScore)))
            visited.add(a)

def getByFacing(pt, adj):
    if pt.row > adj.row:
        return '^'
    if pt.row < adj.row:
        return 'v'
    if pt.col > adj.col:
        return '<'
    if pt.col < adj.col:
        return '>'
    return None

def priorityCalc(pos, endPos, score):
    return abs(pos.row - endPos.row) + abs(pos.col - endPos.col) + score

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(sys.argv[1])
    else:
        solve()

# 135552 - too high
