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

    score, path = p1(startPos, endPos, facing, walls)
    print(score)
    p2(score, startPos, endPos, facing, walls)

def p1(startPos, endPos, facing, walls):
    pq = []
    score = 0
    visited = set()
    visited.add(startPos)
    heapq.heappush(pq, (priorityCalc(startPos, endPos, score), (startPos, facing, score, [(startPos, facing, score)])))
    
    while pq:
        pt, facing, score, path = heapq.heappop(pq)[1]
        if pt == endPos:
            return score, path
        adj = [adj for adj in pt.adjacent() if adj not in walls and adj not in visited]
        for a in adj:
            if getByFacing(pt, a) == facing:
                newScore = score + 1
                heapq.heappush(pq, (priorityCalc(a, endPos, newScore), (a, facing, newScore, path + [(a, facing, newScore)])))
            else:
                newScore = score + 1001
                heapq.heappush(pq, (priorityCalc(a, endPos, newScore), (a, getByFacing(pt, a), newScore, path + [(a, getByFacing(pt, a), newScore)])))
            visited.add(a)

def p2(bestScore, startPos, endPos, facing, walls):
    pq = []
    score = 0
    visitedDict = {}
    visitedDict[(startPos, facing)] = score
    bestPaths = set()
    heapq.heappush(pq, (priorityCalc(startPos, endPos, score), (startPos, facing, score, [startPos])))
    
    while pq:
        # for val in visitedDict:
        #     print(val[0], val[1], visitedDict[val]) 
        # input()
        pt, facing, score, path = heapq.heappop(pq)[1]
        # for i in range(15):
        #     line = []
        #     for j in range(15):
        #         if Coord(i, j) in walls:
        #             line.append('#')
        #         elif Coord(i, j) in path:
        #             line.append('O')
        #         else:
        #             line.append('.')
        #     print("".join(line))
        # input()    
        if pt == endPos:
            bestPaths.update(path)
        adj = [adj for adj in pt.adjacent() if adj not in walls]
        for a in adj:
            if getByFacing(pt, a) == facing:
                newScore = score + 1
            else:
                newScore = score + 1001
            newFacing = getByFacing(pt, a)
            if (a, newFacing) in visitedDict and newScore > visitedDict[(a, newFacing)]:
                continue
            visitedDict[(a, newFacing)] = newScore
            if priorityCalc(a, endPos, newScore) <= bestScore:
                heapq.heappush(pq, (priorityCalc(a, endPos, newScore), (a, getByFacing(pt, a), newScore, path + [a])))
    print(len(bestPaths))
 
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
