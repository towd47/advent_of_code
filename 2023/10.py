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
		if p1[0] > p2[0]: edgeRange = range(p2[1], p1[1] + 1)
		else: edgeRange = range(p1[1], p2[1] + 1)
		for i in edgeRange:
			edges.add((p1[0], i))
	else:
		if p1[1] > p2[1]: edgeRange = range(p2[0], p1[0] + 1)
		else: edgeRange = range(p1[0], p2[0] + 1)
		for i in edgeRange:
			edges.add((p1[1], i))
	return edges

lines = readInput.linesToList("10")
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

nodes = set()
nodes.add(sPos)

rows = len(lines[0])
cols = len(lines)

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

print(int(len(chain) / 2))

doubledChain = [(x * 2, y * 2) for (x, y) in chain]

chainSet = setOfAllEdges(doubledChain)

edgeSet = set()
for i in range(cols * 2):
	edgeSet.add((0, i))
	edgeSet.add((rows * 2 - 1, i))
for i in range(rows * 2):
	edgeSet.add((i, 0))
	edgeSet.add((i, cols * 2 - 1))

visitedSet = set()
visitedSet.update(chainSet)
for x in edgeSet:
	if x in visitedSet:
		continue
	nodesToCheck = [x]
	while nodesToCheck:
		node = nodesToCheck.pop()
		visitedSet.add(node)
		adj = getAdj(node, rows * 2, cols * 2)
		for y in adj:
			if y not in visitedSet:
				nodesToCheck.append(y)
print(len(visitedSet) / (rows * 2 * cols * 2))




