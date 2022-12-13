import heapq
import copy

class Coord(object):
	def __init__(self, row, col):
		self.row = row
		self.col = col

def getAdj(coord, rowlim, collim):
	coords = []
	if coord.row - 1 >= 0:
		coords.append(Coord(coord.row - 1, coord.col))
	if coord.row + 1 < rowlim:
		coords.append(Coord(coord.row + 1, coord.col))
	if coord.col - 1 >= 0:
		coords.append(Coord(coord.row, coord.col - 1))
	if coord.col + 1 < collim:
		coords.append(Coord(coord.row, coord.col + 1))
	return coords

def dist(coord1, coord2):
	return abs(coord1.row - coord2.row) + abs(coord1.col - coord2.col)

class Node(object):
	def __init__(self, value, coord):
		self.value = value
		self.connections = []
		self.backConnections = []
		self.coord = coord
		self.visited = False
		self.stepsToReach = 0

	def addConnection(self, connection):
		self.connections.append(connection)

	def addBackwardsConnection(self, connection):
		self.backConnections.append(connection)

	def __gt__(self, node2):
		return self.value > node2.value
		

f = open("input/12")

data = f.readlines()

grid = []

for x in data:
	x = x.strip()
	grid.append([ord(y) for y in x])

startVal = ord('S')
endVal = ord('E')
startCoord = None
endCoord = None

nodegrid = []
for _ in range(len(grid)):
	nodegrid.append([])
for i in range(len(grid)):
	for j in range(len(grid[i])):
		coord = Coord(i, j)
		node = Node(grid[i][j], coord)
		if grid[i][j] == startVal:
			startCoord = coord
			node.value = ord('a')
		if grid[i][j] == endVal:
			endCoord = coord
			node.value = ord('z')
		nodegrid[i].append(node)


rowlim = len(nodegrid)
collim = len(nodegrid[0])

for i in range(len(nodegrid)):
	for j in range(len(nodegrid[i])):
		adjcords = getAdj(Coord(i, j), rowlim, collim)
		for x in adjcords:
			if nodegrid[x.row][x.col].value <= nodegrid[i][j].value + 1:
				nodegrid[i][j].addConnection(nodegrid[x.row][x.col])
				nodegrid[x.row][x.col].addBackwardsConnection(nodegrid[i][j])


nodesToCheck = []
nodesToCheck.append((0, nodegrid[startCoord.row][startCoord.col]))
nodesToCheck[0][1].visited = True

heapq.heapify(nodesToCheck)
atEnd = False
while not atEnd:
	curNode = heapq.heappop(nodesToCheck)[1]
	for x in curNode.connections:
		if x.visited == False:
			x.visited = True
			x.stepsToReach = curNode.stepsToReach + 1
			heapq.heappush(nodesToCheck, (x.stepsToReach, x))
			if x.coord.row == endCoord.row and x.coord.col == endCoord.col:
				atEnd = True

mindist = nodegrid[endCoord.row][endCoord.col].stepsToReach

print(mindist)

nodesToCheck = []
nodesToCheck.append((0, nodegrid[endCoord.row][endCoord.col]))
nodesToCheck[0][1].visited = True

for nodes in nodegrid:
	for node in nodes:
		node.visited = False
		node.stepsToReach = 0

atEnd = False
while not atEnd:
	curNode = heapq.heappop(nodesToCheck)[1]
	for x in curNode.backConnections:
		if x.visited == False:
			x.visited = True
			x.stepsToReach = curNode.stepsToReach + 1
			heapq.heappush(nodesToCheck, (x.stepsToReach, x))
			if x.value == ord('a'):
				print(x.stepsToReach)
				atEnd = True



















