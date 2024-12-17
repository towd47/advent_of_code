from readInput import linesToList, yieldLines
from coord import Coord
import sys

def solve(filename='15'):
    lines = yieldLines(filename)
    grid = []
    while (line := next(lines)) != "\n":
        grid.append(list(line.strip()))

    movements = "".join([line.strip() for line in lines])

    boxes = set()
    walls = set()
    currPos = None
    for row, line in enumerate(grid):
        for col, val in enumerate(line):
            if val == '@':
                currPos = Coord(row, col)
            elif val == 'O':
                boxes.add(Coord(row, col))
            elif val == '#':
                walls.add(Coord(row, col))

    # printGrid(grid, walls, boxes, currPos)
    # input()
    for direction in movements:
        currPos = move(direction, currPos, walls, boxes)
        # print(direction)
        # printGrid(grid, walls, boxes, currPos)
        # input()

    # printGrid(grid, walls, boxes, currPos)
    print(sum([c.row * 100 + c.col for c in boxes]))

def printGrid(grid, walls, boxes, currPos):
    for row, line in enumerate(grid):
        l = []
        for col, val in enumerate(line):
            if Coord(row, col) in walls:
                l.append('#')
            elif Coord(row, col) in boxes:
                l.append('O')
            elif Coord(row, col) == currPos:
                l.append('@')
            else:
                l.append('.')
        print(''.join(l))

def move(direction, currPos, walls, boxes):
    nextPos = currPos
    match direction:
        case '<':
            d = Coord.cLeft                    
        case '^':
            d = Coord.cUp
        case '>':
            d = Coord.cRight
        case 'v':
            d = Coord.cDown

    boxesToMove = []
    blocked = False
    while True:
        nextPos = d(nextPos)
        if nextPos in walls:
            blocked = True
            break
        elif nextPos in boxes:
            boxesToMove.append(nextPos)
        else:
            break
    if not blocked:
        if boxesToMove:
            boxes.remove(boxesToMove[0])
            boxes.add(d(boxesToMove[-1]))
        currPos = d(currPos)
    return currPos


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        solve(filename)
    else:
        solve()

