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

def getAdjS(coord, rows, cols, lines):
	row, col = coord
	adj = []
	if row != 0:
		if lines[row - 1][col] == "F" or lines[row - 1][col] == "7" or lines[row - 1][col] == "|":
			adj.append((row - 1, col))
	if row < rows - 1:
		if lines[row + 1][col] == "L" or lines[row + 1][col] == "J" or lines[row + 1][col] == "|":
			adj.append((row + 1, col))
	if col != 0:
		if lines[row][col - 1] == "L" or lines[row][col - 1] == "F" or lines[row][col - 1] == "-":
			adj.append((row, col - 1))
	if col < cols - 1:
		if lines[row][col + 7] == "7" or lines[row][col + 7] == "J" or lines[row][col + 1] == "-":
			adj.append((row, col + 1))
	return adj

def getAdjByLetter(coord, l):
	if l == "-":
		return [(coord[0], coord[1] - 1), (coord[0], coord[1] + 1)]
	if l == "|":
		return [(coord[0] - 1, coord[1]), (coord[0] + 1, coord[1])]
	if l == "7":
		return [(coord[0], coord[1] - 1), (coord[0] + 1, coord[1])]
	if l == "J":
		return [(coord[0], coord[1] - 1), (coord[0] - 1, coord[1])]
	if l == "L":
		return [(coord[0] - 1, coord[1]), (coord[0], coord[1] + 1)]
	if l == "F":
		return [(coord[0] + 1, coord[1]), (coord[0], coord[1] + 1)]
	return [(-1, -1), (-1, -1)]

def isValid(node, rows, cols):
	if node[0] < 0 or node[0] >= rows:
		return False
	if node[1] < 0 or node[1] >= cols:
		return False
	return True

def setOfAllEdges(chain):
	edgeSet = set()
	for i, e in enumerate(chain):
		j = (i+1) % len(chain)
		edgeSet.update(allEdges(e, chain[j]))
	return edgeSet

def allEdges(p1, p2):
	edges = set()
	if p1[0] == p2[0]:
		if p1[1] > p2[1]: edgeRange = range(p2[1], p1[1] + 1)
		else: edgeRange = range(p1[1], p2[1] + 1)
		for i in edgeRange:
			edges.add((p1[0], i))
	else:
		if p1[0] > p2[0]: edgeRange = range(p2[0], p1[0] + 1)
		else: edgeRange = range(p1[0], p2[0] + 1)
		for i in edgeRange:
			edges.add((i, p1[1]))
	return edges

def getGridAndSPos(f):
		
	lines = readInput.linesToList(f)
	strippedLines = []
	for line in lines:
		line = line.strip()
		strippedLines.append(line)
	lines = strippedLines

	sPos = None
	for row, line in enumerate(lines):
		for col, val in enumerate(line):
			if val == "S":
				sPos = (row, col)
				break
		if sPos:
			break
	return (lines, sPos)

def getChain(lines, sPos):
	nodes = set()
	nodes.add(sPos)

	rows = len(lines)
	cols = len(lines[0])

	chain = [sPos]

	nodesToStartFrom = getAdjS(sPos, rows, cols, lines)

	for node in nodesToStartFrom:
		nodes.add(node)
		chain.append(node)
		adj = getAdjByLetter(node, lines[node[0]][node[1]])
		if sPos not in adj:
			chain = [sPos]
			continue
		while isValid(adj[0], rows, cols) and isValid(adj[1], rows, cols) and (adj[0] not in nodes or adj[1] not in nodes):
			if adj[0] not in nodes:
				chain.append(adj[0])
				nodes.add(adj[0])
				adj = getAdjByLetter(adj[0], lines[adj[0][0]][adj[0][1]])
			elif adj[1] not in nodes:
				chain.append(adj[1])
				nodes.add(adj[1])
				adj = getAdjByLetter(adj[1], lines[adj[1][0]][adj[1][1]])
		if not isValid(adj[0], rows, cols) or not isValid(adj[1], rows, cols):
			chain = [sPos]
		else:
			break
	return chain
	
def applyDir(chainPoint, dir):
	return (chainPoint[0] + dir[0], chainPoint[1] + dir[1])

def newDir(l, dir):
	if l == "-" or l == "|":
		return dir
	if l == "7" or l == "L" or l == "S":
		return rotateRight(dir)
	if l == "J" or l == "F":
		return rotateLeft(dir)
	return (-1, -1)

# (0, 1) F (1, 0)

def rotateLeft(dir):
	return (dir[1], dir[0])

def rotateRight(dir):
	return (dir[1] * -1, dir[0] * -1)

def printGrid(rows, cols, chainSet):
	for i in range(rows):
		line = ""
		for j in range(cols):
			if (i, j) in chainSet:
				line += "#"
			else:
				line += "."
		print(line)

def printWithInsidePts(rows, cols, chainset, visited, lines):
	for i in range(rows):
		line = ""
		for j in range(cols):
			if (i, j) in chainSet:
				line += lines[i][j]
			elif (i, j) in visited:
				line += "#"
			else:
				line += "."
		print(line)


lines, sPos = getGridAndSPos("10")
chain = getChain(lines, sPos)
print(int(len(chain) / 2))

rows = len(lines)
cols = len(lines[0])

chainSet = setOfAllEdges(chain)
chain = [(x, y, lines[x][y]) for (x, y) in chain]
highest = (10000000, -1)
for i, e in enumerate(chain):
	if (e[0] < highest[0]):
		highest = (e[0], i)


insidePoints = []
startPoint = chain[highest[1]]
d = (1, 0)

for i in range(highest[1], len(chain) + highest[1]):
	i = i % len(chain)
	p2 = applyDir(chain[i], d)
	if i != highest[1]:
		d = newDir(chain[i][2], d)
	p = applyDir(chain[i], d)
	if p not in chainSet:
		insidePoints.append(p)
	if p2 not in chainSet:
		insidePoints.append(p2)

visited = set()
visited.update(chainSet)

while insidePoints:
	pt = insidePoints.pop()
	if pt in visited:
		continue
	visited.add(pt)
	adj = getAdj(pt, rows, cols)
	insidePoints.extend(adj)

print(len(visited) - len(chainSet))

