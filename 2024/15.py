from readInput import linesToList, yieldLines
from coord import Coord
import sys

def solve(filename='15'):
    lines = yieldLines(filename)
    grid = []
    while (line := next(lines)) != "\n":
        grid.append(list(line.strip()))

    movements = "".join([line.strip() for line in lines])
    p1(grid, movements)
    p2(grid, movements)

def p1(grid, movements):
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

def p2(grid, movements):
    currPos = None
    walls = set()
    boxes = set()
    wideGrid = []
    for row, line in enumerate(grid):
        newLine = []
        for col, val in enumerate(line):
            if val == '.':
                newLine.extend(['.','.'])
            elif val == 'O':
                newLine.extend(['[',']'])
                boxes.add(Coord(row, col * 2))
                boxes.add(Coord(row, col * 2 + 1))
            elif val == '#':
                newLine.extend(['#', '#'])
                walls.add(Coord(row, col * 2))
                walls.add(Coord(row, col * 2 + 1))
            else:
                newLine.extend(['@', '.'])
                currPos = Coord(row, col * 2)
        wideGrid.append(newLine)
    
    for direction in movements:
        currPos, boxes = move2(direction, currPos, walls, boxes, wideGrid)

    # for line in wideGrid:
    #     print("".join(line))
    tot = 0
    for row, line in enumerate(wideGrid):
        for col, val in enumerate(line):
            if Coord(row, col).val(wideGrid) == '[':
                tot += row * 100 + col
    print(tot)

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

def move2(direction, currPos, walls, boxes, grid):
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
    if direction in ('<', '>'):
        while not blocked:
            nextPos = d(nextPos)
            if nextPos in walls:
                blocked = True
            elif nextPos in boxes:
                boxesToMove.append(nextPos)
                nextPos = d(nextPos)
                boxesToMove.append(nextPos)
            else:
                break
        if not blocked:
            if boxesToMove:
                boxes.remove(boxesToMove[0])
                boxes.add(d(boxesToMove[-1]))
                if direction == '<':
                    grid[currPos.row].pop(boxesToMove[-1].col - 1)
                else:
                    grid[currPos.row].pop(boxesToMove[-1].col + 1)
                grid[currPos.row].insert(currPos.col, '.')
    else:
        boxPoses = set()
        nextPoses = set()
        nextPoses.add(nextPos)
        while not blocked:
            nextPoses = set([d(nextPos) for nextPos in nextPoses])
            complements = set()
            blanks = set()
            for pos in nextPoses:
                if pos in walls:
                    blocked = True
                elif pos in boxes:
                    if pos.val(grid) == ']':
                        p = pos.left()
                    else:
                        p = pos.right()
                    complements.add(p)
                    boxPoses.add(p)
                    boxPoses.add(pos)
                else:
                    blanks.add(pos)
            nextPoses = (nextPoses | complements) - blanks
            if not nextPoses:
                break
        if not blocked:
            boxes = boxes - boxPoses
            boxPoses = list(boxPoses)
            boxPoses.sort()
            if direction == 'v':
                boxPoses.reverse()

            for pos in boxPoses:
                movedPos = d(pos)
                grid[movedPos.row][movedPos.col] = pos.val(grid)
                grid[pos.row][pos.col] = '.'
                boxes.add(movedPos)
                
    if not blocked:
        newPos = d(currPos)
        grid[newPos.row][newPos.col] = '@'
        grid[currPos.row][currPos.col] = '.'
        return newPos, boxes
    return currPos, boxes

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        solve(filename)
    else:
        solve()

