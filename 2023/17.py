import readInput
import heapq

def readGrid(f):
    return [list(map(int, list(x))) for x in readInput.linesToList(f)]

def solve():
    grid = readGrid("test")
    p1(grid)

def p1(grid):
    start = (0, 0)
    goal = (len(grid) - 1, len(grid[0]) - 1)
    heat = getGridSpace(start, grid)
    gridMap = []
    for _ in range(len(grid)):
        row = []
        for _ in range(len(grid[0])):
            row.append(0)
        gridMap.append(row)
    gridMap[0][0] = heat
    path = []
    points = [(getGridSpace(start, gridMap) + dist(start, goal), start, path)]
    heapq.heapify(points)

    currp = heapq.heappop(points)
    while points:
        adj = getAdj(currp[1], grid)
        for x in adj:
            if getGridSpace(x[0], gridMap) != 0:
                continue
            score = getGridSpace(start, gridMap) + getGridSpace(x[0], grid) + dist(x[0], goal)
            path = currp[2].copy()
            path.append(x[1])
            gridMap[x[0][0]][x[0][1]] = getGridSpace(currp[1], gridMap) + getGridSpace(x[0], grid)
            if len(path) < 4 or len(set(path[-4:])) > 1:
                heapq.heappush(points, (score, x[0], path))
        currp = heapq.heappop(points)

    print(getGridSpace(currp[1], gridMap))

def printGrid(grid):
    for x in grid:
        print("".join([str(s) for s in x]))

def getAdj(coord, grid):
    row, col = coord
    rows = len(grid)
    cols = len(grid[0])
    adj = []
    if row != 0:
        adj.append(((row - 1, col), "U"))
    if row < rows - 1:
        adj.append(((row + 1, col), "D"))
    if col != 0:
        adj.append(((row, col - 1), "L"))
    if col < cols - 1:
        adj.append(((row, col + 1), "R"))
    return adj

def dist(c1, c2):
    return (abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]))

def getGridSpace(coord, grid):
    return grid[coord[0]][coord[1]]
    
def p1():
    return

if __name__ == "__main__":
    solve()