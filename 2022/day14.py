import copy


def printCave(occupiedSpots, curC, lowest, left, right):
	for i in range(lowest + 2):
		for j in range(left, right + 1):
			if (j, i) in occupiedSpots:
				print(occupiedSpots[(j, i)], end="")
			elif (j, i) == curC:
				print("s", end="")
			else:
				print(".", end="")
		print()
	print()

def printAroundCurC(occupiedSpots, curC, lowest):
	grid = []
	for i in range(max(0, curC[1] - 10), min(curC[1] + 11, lowest + 2)):
		grid.append(['.'] * 21)
	grid[curC[1] - max(0, curC[1] - 10)][11] = 's'
	for i in range(curC[0] - 10, curC[0] + 11):
		for j in range(max(0, curC[1] - 10), min(curC[1] + 11, lowest + 2)):
			pos = (i - curC[0] - 10, j - max(0, curC[1] - 10))
			if (i, j) in occupiedSpots:
				grid[pos[1]][pos[0]] = occupiedSpots[(i, j)]

	for x in grid:
		for y in x:
			print(y, end="")
		print()
	print()

f = open("input/14")

data = f.readlines()

occupiedSpots = dict()

lowest = 0
left = 500
right = 500
for line in data:
	coords = line.strip().split(" -> ")
	for i in range(len(coords) - 1):
		coord1 = list(map(int, coords[i].split(",")))
		coord2 = list(map(int, coords[i + 1].split(",")))
		lowest = max(lowest, coord1[1])
		lowest = max(lowest, coord2[1])
		left = min(left, coord1[0])
		left = min(left, coord2[0])
		right = max(right, coord1[0])
		right = max(right, coord2[0])

		if coord1[0] == coord2[0]:
			x = coord1[0]
			for i in range(min(coord1[1], coord2[1]), max(coord1[1], coord2[1]) + 1):
				c = (x, i)
				occupiedSpots[c] = 'r'
		else:
			y = coord1[1]
			for i in range(min(coord1[0], coord2[0]), max(coord1[0], coord2[0]) + 1):
				c = (i, y)
				occupiedSpots[c] = "r"

left -= 2
right += 2

occupiedSpotsWithFloor = copy.copy(occupiedSpots)

rocks = len(occupiedSpots)
startC = [500, 0]
curC = copy.copy(startC)

while curC[1] < lowest:
	nextC = copy.copy(curC)
	nextC[1] += 1
	if (nextC[0], nextC[1]) in occupiedSpots:
		nextC[0] -= 1
		if (nextC[0], nextC[1]) in occupiedSpots:
			nextC[0] += 2
			if (nextC[0], nextC[1]) in occupiedSpots:
				occupiedSpots[(curC[0], curC[1])] = 's'
				curC = copy.copy(startC)
			else:
				curC = nextC
		else:
			curC = nextC
	else:
		curC = nextC
	printAroundCurC(occupiedSpots, curC, lowest)
	input()

sand = len(occupiedSpots) - rocks
print(sand)

curC = copy.copy(startC)
while (startC[0], startC[1]) not in occupiedSpotsWithFloor:
	nextC = copy.copy(curC)
	nextC[1] += 1
	if curC[1] == lowest + 1:
		occupiedSpotsWithFloor[(curC[0], curC[1])] = 's'
		curC = copy.copy(startC)
	elif (nextC[0], nextC[1]) in occupiedSpotsWithFloor:
		nextC[0] -= 1
		if (nextC[0], nextC[1]) in occupiedSpotsWithFloor:
			nextC[0] += 2
			if (nextC[0], nextC[1]) in occupiedSpotsWithFloor:
				occupiedSpotsWithFloor[(curC[0], curC[1])] = 's'
				curC = copy.copy(startC)
			else:
				curC = nextC
		else:
			curC = nextC
	else:
		curC = nextC

sand = len(occupiedSpotsWithFloor) - rocks
print(sand)
