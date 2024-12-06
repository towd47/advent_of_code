from readInput import linesToList
import sys

def solve(filename='6'):
	lines = linesToList(filename)
	startPos, startDir = findStartPos(lines)

	print(p1Clean(startPos, startDir, lines))
	print(p2(startPos, startDir, lines))

def findStartPos(lines):
	dirs = ['^', '>', 'v', '<']
	for row, line in enumerate(lines):
		for col, c in enumerate(line):
			if c in dirs:
				return (row, col), c

def p1Clean(currPos, currDir, lines):
	pts = set()
	pts.add(currPos)
	while res := step(currPos, currDir, lines):
		pts.add(res[0])
		currPos = res[0]
		currDir = res[1]

	return len(pts)

def p2(startPos, startDir, lines):
	lines = [list(line) for line in lines]
	currPos = startPos
	currDir = startDir
	pts = set()
	turnpts = set()

	while res := step(currPos, currDir, lines):
		pt, d = res
		if pt == currPos:
			turnpts.add(pt)
			currDir = d
		else:
			pts.add(pt)
			currPos = pt

	pts.discard(startPos)

	tot = 0
	for pt in pts:
		lines[pt[0]][pt[1]] = '#'
		if doesItLoop(startPos, startDir, lines):
			tot += 1
		lines[pt[0]][pt[1]] = '.'
	return tot

def doesItLoop(currPos, currDir, lines):
	pts = set()
	pts.add((currPos, currDir))
	while res := step(currPos, currDir, lines):
		if res in pts:
			return True
		pts.add(res)
		currPos = res[0]
		currDir = res[1]
	return False

def step(currPos, currDir, lines):
	row, col = currPos
	match currDir:
		case '^':
			if row == 0:
				return None
			if lines[row-1][col] == '#':
				return (row, col), '>'
			else:
				return (row - 1, col), '^'
		case '>':
			if col == len(lines[0]) - 1:
				return None
			if lines[row][col+1] == '#':
				return (row, col), 'v'
			else:
				return (row, col + 1), '>'
		case 'v':
			if row == len(lines) - 1:
				return None
			if lines[row+1][col] == '#':
				return (row, col), '<'
			else:
				return (row + 1, col), 'v'
		case '<':
			if col == 0:
				return None
			if col == len(lines[0]) - 1:
				return None
			if lines[row][col-1] == '#':
				return (row, col), '^'
			else:
				return (row, col - 1), '<'

if __name__ == '__main__':
	if len(sys.argv) >= 2:
		filename = sys.argv[1]
		solve(filename)
	else:
		solve()
