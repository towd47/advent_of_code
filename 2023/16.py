import readInput

def getGrid(f):
	lines = readInput.linesToList(f)
	lines = [list(x) for x in lines]
	return lines

def solve():
	grid = getGrid("16")
	print(p1(grid))
	print(p2(grid))

def p2(grid):
	edges = []
	for i, _ in enumerate(grid):
		edges.append(((i, 0), (0, 1)))
		edges.append(((i, len(grid[0]) - 1), (0, -1)))
	for i, _ in enumerate(grid[0]):
		edges.append(((0, i), (1, 0)))
		edges.append(((len(grid) - 1, i), (-1, 0)))

	maxEnergized = 0
	for x in edges:
		energized = p1(grid, x[0], x[1])
		maxEnergized = max(maxEnergized, energized)
	return maxEnergized

def p1(grid, laserPos = (0, 0), laserDir = (0, 1)):
	lasersToEval = [(laserDir, laserPos)]
	visited = set()
	visitedPos = set()

	while lasersToEval:
		laser = lasersToEval.pop()
		if not inGrid(laser[1], grid) or laser in visited:
			continue
		visited.add(laser)
		visitedPos.add(laser[1])
		lasersToEval.extend(nextLasers(laser, grid))
	
	return len(visitedPos)
	
def printVisited(visited, grid):
	rows = len(grid)
	cols = len(grid[0])

	newGrid = []
	for i in range(rows):
		newRow = []
		for j in range(cols):
			newRow.append(".")
		newGrid.append(newRow)

	for x in visited:
		newGrid[x[1][0]][x[1][1]] = "#"

	for x in newGrid:
		print("".join(x))
	print()

def inGrid(pos, grid):
	if pos[0] < 0 or pos[0] >= len(grid) or pos[1] < 0 or pos[1] >= len(grid[0]):
		return False
	return True

def nextLasers(laser, grid):
	d, pos = laser
	c = getCharInGrid(pos, grid)
	if c == ".":
		return [(d, applyDir(pos, d))]
	elif c == "/":
		d = (d[1] * -1, d[0] * -1)
		return [(d, applyDir(pos, d))]
		# 1, 0 -> 0, -1
		# 0, 1 -> -1, 0
	elif c == "\\":
		d = (d[1], d[0])
		return [(d, applyDir(pos, d))]
		# 1, 0 -> 0, 1
		# 0, -1 -> -1, 0
	elif c == "-":
		if d[0] == 0:
			return [(d, applyDir(pos, d))]
		else:
			d1 = (d[1], d[0])
			d2 = (d[1] * -1, d[0] * -1)
			return [(d1, applyDir(pos, d1)), (d2, applyDir(pos, d2))]
	elif c == "|":
		if d[1] == 0:
			return [(d, applyDir(pos, d))]
		else:
			d1 = (d[1], d[0])
			d2 = (d[1] * -1, d[0] * -1)
			return [(d1, applyDir(pos, d1)), (d2, applyDir(pos, d2))]
	return []

def applyDir(pos, dir):
	return (pos[0] + dir[0], pos[1] + dir[1])

def getCharInGrid(pos, grid):
	return grid[pos[0]][pos[1]]

if __name__ == "__main__":
	solve()