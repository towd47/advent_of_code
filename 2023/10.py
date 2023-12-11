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

print(chain)
print(int(len(chain) / 2))





