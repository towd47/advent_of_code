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

	nodesToStartFrom = getAdj(sPos, rows, cols)

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
		if dir[0] == 0:
			return rotateRight(dir)
		return rotateLeft(dir)
	if l == "J" or l == "F":
		if dir[0] == 0:
			return rotateLeft(dir)
		return rotateRight(dir)
	return (-1, -1)

def rotateLeft(dir):
	return (dir[1], dir[0] * -1)

def rotateRight(dir):
	return (dir[1] * -1, dir[0])

lines, sPos = getGridAndSPos("10")
chain = getChain(lines, sPos)
print(int(len(chain) / 2))

rows = len(lines[0])
cols = len(lines)

chainSet = setOfAllEdges(chain)
chain = [(x, y, lines[x][y]) for (x, y) in chain]
highest = (10000000, -1)
for i, e in enumerate(chain):
	if (e[0] < highest[0]):
		highest = (e[0], i)

print(highest)

insidePoints = []
startPoint = chain[highest[1]]
dir = (1, 0)

for i in range(highest[0], len(chain) + highest[0]):
	i = i % len(chain)
	if i != highest[0]:
		dir = newDir(chain[i][2], dir)
	insidePoints.append(applyDir(chain[i], dir))

visitedSet = set()
visitedSet.update(chainSet)
for x in insidePoints:
	if x in visitedSet:
		continue
	nodesToCheck = [x]
	while nodesToCheck:
		node = nodesToCheck.pop()
		visitedSet.add(node)
		adj = getAdj(node, rows, cols)
		for y in adj:
			if y not in visitedSet:
				nodesToCheck.append(y)

print(len(visitedSet) - len(chain))


