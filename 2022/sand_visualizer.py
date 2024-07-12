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
	stdscr.refresh()

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

def mainScreen():
	stdscr = curses.initscr()
	stdscr.border()

def main():



stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.scrollok(True)
main()