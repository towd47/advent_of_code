from readInput import linesToList
import sys

def solve(filename='6'):
	lines = linesToList(filename)
	dirs = ['^', '>', 'v', '<']

	startPos = None
	startDir = None
	blocksByRow = {}
	blocksByCol = {}

	for row, line in enumerate(lines):
		for col, c in enumerate(line):
			if c in dirs:
				startPos = (row, col)
				startDir = c
			elif c == '#':
				if row in blocksByRow:
					blocksByRow[row].append(col)
				else:
					blocksByRow[row] = [col]

				if col in blocksByCol:
					blocksByCol[col].append(row)
				else:
					blocksByCol[col] = [row]

	print(p1(startPos, startDir, blocksByRow, blocksByCol, len(lines) - 1, len(lines[0]) - 1))

def p1(currPos, currDir, blocksByRow, blocksByCol, rowMax, colMax):
	visitedByCol = {}
	visitedByRow = {}
	while True:
		match currDir:
			case '^':
				dists = []
				if currPos[1] in blocksByCol:
					dists = [currPos[0] - blockpos if blockpos < currPos[0] else rowMax for blockpos in blocksByCol[currPos[1]]]
				if not dists or min(dists) == rowMax:
					if currPos[1] in visitedByCol:
						visitedByCol[currPos[1]].append((currPos[0], 0))
					else:
						visitedByCol[currPos[1]] = [(currPos[0], 0)]
					break

				closest = blocksByCol[currPos[1]][dists.index(min(dists))]

				if currPos[1] in visitedByCol:
					visitedByCol[currPos[1]].append((closest + 1, currPos[0]))
				else:
					visitedByCol[currPos[1]] = [(closest + 1, currPos[0])]

				currPos = (closest + 1, currPos[1])
				currDir = '>'
			case '>':
				dists = []
				if currPos[0] in blocksByRow:
					dists = [blockpos - currPos[1] if blockpos > currPos[1] else colMax for blockpos in blocksByRow[currPos[0]]]
				if not dists or min(dists) == colMax:
					if currPos[0] in visitedByRow:
						visitedByRow[currPos[0]].append((currPos[1], colMax))
					else:
						visitedByRow[currPos[0]] = [(currPos[1], colMax)]
					break
				closest = blocksByRow[currPos[0]][dists.index(min(dists))]

				if currPos[0] in visitedByRow:
					visitedByRow[currPos[0]].append((currPos[1], closest - 1))
				else:
					visitedByRow[currPos[0]] = [(currPos[1], closest - 1)]

				currPos = (currPos[0], closest - 1)
				currDir = 'v'
			case 'v':
				dists = []
				if currPos[1] in blocksByCol:
					dists = [blockpos - currPos[0] if blockpos > currPos[0] else rowMax for blockpos in blocksByCol[currPos[1]]]
				if not dists or min(dists) == rowMax:
					if currPos[1] in visitedByCol:
						visitedByCol[currPos[1]].append((currPos[0], rowMax))
					else:
						visitedByCol[currPos[1]] = [(currPos[0], rowMax)]
					break
				closest = blocksByCol[currPos[1]][dists.index(min(dists))]

				if currPos[1] in visitedByCol:
					visitedByCol[currPos[1]].append((currPos[0], closest - 1))
				else:
					visitedByCol[currPos[1]] = [(currPos[0], closest - 1)]

				currPos = (closest - 1, currPos[1])
				currDir = '<'
			case '<':
				dists = []
				if currPos[0] in blocksByRow:
					dists = [currPos[1] - blockpos if blockpos < currPos[1] else colMax for blockpos in blocksByRow[currPos[0]]]
				if not dists or min(dists) == colMax:
					if currPos[0] in visitedByRow:
						visitedByRow[currPos[0]].append((0, currPos[1]))
					else:
						visitedByRow[currPos[0]] = [(0, currPos[1])]
					break
				closest = blocksByRow[currPos[0]][dists.index(min(dists))]

				if currPos[0] in visitedByRow:
					visitedByRow[currPos[0]].append((closest + 1, currPos[1]))
				else:
					visitedByRow[currPos[0]] = [(closest + 1, currPos[1])]

				currPos = (currPos[0], closest + 1)
				currDir = '^'

	pts = set()
	for key in visitedByCol:
		[[pts.add((i, key)) for i in range(val[0], val[1] + 1)] for val in visitedByCol[key]]
	for key in visitedByRow:
		[[pts.add((key, i)) for i in range(val[0], val[1] + 1)] for val in visitedByRow[key]]

	return len(pts)



if __name__ == '__main__':
	if len(sys.argv) >= 2:
		filename = sys.argv[1]
		solve(filename)
	else:
		solve()