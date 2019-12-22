def advent3_1():

	lines = loadLinesFromFile()

	fabric = [[0 for i in range(1000)] for j in range(1000)]

	for x in lines:
		instructionList = x.split()
		startX = int(instructionList[2].split(',')[0])
		startY = int(instructionList[2].split(',')[1][:len(instructionList[2].split(',')[1]) - 1])

		dim1 = int(x.split()[3].split('x')[0])
		dim2 = int(x.split()[3].split('x')[1])

		for k in range(startX, startX+dim1):
			for l in range(startY, startY+dim2):
				fabric[k][l] += 1

	total = 0
	for i in range(1000):
		for j in range(1000):
			if fabric[i][j] >= 2:
				total += 1

	print(total)

def advent3_2():

	lines = loadLinesFromFile()

	fabric = [[0 for i in range(1000)] for j in range(1000)]

	possibleClaims = list(range(1, len(lines) + 1))

	for x in lines:
		instructionList = x.split()

		fillVal = int(instructionList[0][1:])
		startX = int(instructionList[2].split(',')[0])
		startY = int(instructionList[2].split(',')[1][:len(instructionList[2].split(',')[1]) - 1])

		dim1 = int(x.split()[3].split('x')[0])
		dim2 = int(x.split()[3].split('x')[1])

		for k in range(startX, startX+dim1):
			for l in range(startY, startY+dim2):
				if not fabric[k][l] == 0:
					possibleClaims[fabric[k][l] - 1] = 0
					possibleClaims[fillVal - 1] = 0
				else:
					fabric[k][l] = fillVal

	for y in possibleClaims:
		if not y == 0:
			print(y)



def loadLinesFromFile():
	f = open("advent3.txt", "r")
	lines = f.readlines()
	return lines

advent3_1()
advent3_2()



