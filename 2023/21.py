import readInput

def getAdj(coord, rows, cols):
	row, col = coord
	adj = []
	if row != 0:
		adj.append((row - 1, col))
	if row < rows - 1:
		adj.append((row + 1, col))
	if col != 0:
		adj.append((row, col - 1))
	if col < cols - 1:
		adj.append((row, col + 1))
	return adj

lines = readInput.linesToList("21")
sPos = (0, 0)

for i, row in enumerate(lines):
	for j, e in enumerate(row):
		if e == "S":
			sPos = (i, j)

posToCheck = [sPos]
posMap = dict()
posMap[sPos] = 0
rows = len(lines)
cols = len(lines[0])

while posToCheck:
	pos = posToCheck.pop(0)
	if posMap[pos] < 64:
		adj = getAdj(pos, rows, cols)
		for x in adj:
			if x not in posMap and lines[x[0]][x[1]] == ".":
				posMap[x] = posMap[pos] + 1
				posToCheck.append(x)

tot = 0
for x in posMap:
	if posMap[x] % 2 == 0:
		tot += 1

print(tot)
