from readInput import linesToList
import sys


def solve(filename='8'):
    grid = linesToList(filename)
    posDict = dict()

    for row, line in enumerate(grid):
        for col, val in enumerate(line):
            if val != '.':
                if val in posDict:
                    posDict[val].append((row, col))
                else:
                    posDict[val] = [(row, col)]

    rows = len(grid)
    cols = len(grid[0])

    anodes = set()
    for key in posDict:
        poses = posDict[key]
        for i, p1 in enumerate(poses):
            for j, p2 in enumerate(poses[i+1:]):
                diff = subPts(p1, p2)
                a1 = addPts(p1, diff)
                a2 = subPts(p2, diff)
                if checkbounds(a1, rows, cols):
                    anodes.add(a1)
                if checkbounds(a2, rows, cols):
                    anodes.add(a2)

    print(len(anodes))
    for key in posDict:
        poses = posDict[key]
        for i, p1 in enumerate(poses):
            for j, p2 in enumerate(poses[i+1:]):
                anodes.add(p1)
                anodes.add(p2)
                diff = subPts(p1, p2)
                a1 = addPts(p1, diff)
                while checkbounds(a1, rows, cols):
                    anodes.add(a1)
                    a1 = addPts(a1, diff)
                a2 = subPts(p2, diff)
                while checkbounds(a2, rows, cols):
                    anodes.add(a2)
                    a2 = subPts(a2, diff)
    print(len(anodes))

def checkbounds(pt, rows, cols):
    if pt[0] < 0 or pt[0] >= rows:
        return False
    if pt[1] < 0 or pt[1] >= cols:
        return False
    return True

def addPts(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def subPts(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1])

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        solve(filename)
    else:
        solve()