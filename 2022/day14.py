import copy
import curses
import time

def printCave(occupiedSpots, curC, lowest, left, right):
	curSet = set([(x[0], x[1]) for x in curC])
	stdscr.clear()
	if curC[0][0] > right:
		right = curC[0][0]
	elif curC[0][0] < left:
		left = curC[0][0]
	grid = []
	for i in range(50):
		grid.append([' '] * (right - left + 1))
	for i in range(left, right + 1):
		if curC[0][1] < 25:
			val = 0
		elif lowest + 2 - curC[0][1] < 25:
			val = lowest + 2 - 50
		else:
			val = curC[0][1] - 25
		for j in range(50):
			if (i, val + j) in occupiedSpots:
				grid[j][i - left] = occupiedSpots[(i, val + j)]
			elif (i, val + j) in curSet:
				grid[j][i - left] = "."

	for x in grid:
		for y in x:
			stdscr.addch(y)
		stdscr.addch("\n")
	stdscr.border()
	stdscr.refresh()

def setup():

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
					occupiedSpots[c] = '#'
			else:
				y = coord1[1]
				for i in range(min(coord1[0], coord2[0]), max(coord1[0], coord2[0]) + 1):
					c = (i, y)
					occupiedSpots[c] = "#"

	left -= 2
	right += 2

	return (occupiedSpots, lowest, left, right)

def step(occupiedSpots, curC, startC, floor=-1):
	newCur = []
	for x in curC:
		nextC = copy.copy(x)
		nextC[1] += 1
		if floor > 0 and x[1] == floor - 1:
			occupiedSpots[(x[0], x[1])] = '.'
		elif (nextC[0], nextC[1]) in occupiedSpots:
			nextC[0] -= 1
			if (nextC[0], nextC[1]) in occupiedSpots:
				nextC[0] += 2
				if (nextC[0], nextC[1]) in occupiedSpots:
					occupiedSpots[(x[0], x[1])] = '.'
				else:
					newCur.append(nextC)
			else:
				newCur.append(nextC)
		else:
			newCur.append(nextC)
	newCur.append(copy.copy(startC))
	return (occupiedSpots, newCur)

def p1(occupiedSpots, lowest, left, right, shouldDisplay):
	rocks = len(occupiedSpots)
	startC = [500, 0]
	curC = [copy.copy(startC)]
	if shouldDisplay:
		printCave(occupiedSpots, curC, lowest, left, right)
		time.sleep(.02)

	while curC[0][1] < lowest:
		occupiedSpots, curC = step(occupiedSpots, curC, startC)
		if shouldDisplay:
			printCave(occupiedSpots, curC, lowest, left, right)
			time.sleep(.02)

	sand = len(occupiedSpots) - rocks
	print(sand)

def p2(occupiedSpots, lowest, left, right, shouldDisplay):
	rocks = len(occupiedSpots)
	startC = [500, 0]
	curC = [copy.copy(startC)]
	if shouldDisplay:
		printCave(occupiedSpots, curC, lowest, left, right)
		time.sleep(.02)
	while (startC[0], startC[1]) not in occupiedSpots:
		occupiedSpots, curC = step(occupiedSpots, curC, startC, lowest + 2)
		if shouldDisplay:
			printCave(occupiedSpots, curC, lowest, left, right)
			time.sleep(.02)

	sand = len(occupiedSpots) - rocks
	print(sand)


def main():

	occupiedSpots, lowest, left, right = setup()

	occupiedSpotsWithFloor = copy.copy(occupiedSpots)

	p1(occupiedSpots, lowest, left, right, True)
	p2(occupiedSpotsWithFloor, lowest, left, right, False)


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.scrollok(True)
main()
