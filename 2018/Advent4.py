def advent4_1():
	lines = loadLinesFromFile()

	guardList = []
	minutesAsleep = []

	orderedLines = orderChronologically(lines)
	for x in orderedLines:
		print(x)

def orderChronologically(lines):
	if isinstance(lines, str):
		newLines = []
		newLines.append(lines)
		lines = newLines

	if len(lines) == 1:
		return lines
	firstHalf = lines[:int(len(lines)/2)]
	secondHalf = lines[int(len(lines)/2):]

	orderedFirstHalf = orderChronologically(firstHalf)
	orderedSecondHalf = orderChronologically(secondHalf)

	mergedList = []

	while len(orderedFirstHalf) > 0 or len(orderedSecondHalf) > 0:
		if len(orderedFirstHalf) == 0:
			mergedList = mergedList + orderedSecondHalf
			orderedSecondHalf = []
		elif len(orderedSecondHalf) == 0:
			mergedList = mergedList + orderedFirstHalf
			orderedFirstHalf = []
		elif getTimeFromStr(orderedFirstHalf[0]) < getTimeFromStr(orderedSecondHalf[0]):
			mergedList.append(orderedFirstHalf.pop(0))
		else:
			mergedList.append(orderedSecondHalf.pop(0))

	return mergedList


def getTimeFromStr(string):
	splitEntry = string.split()
	year = splitEntry[0][1:].split('-')[0]
	month = splitEntry[0].split('-')[1]
	day = splitEntry[0].split('-')[2]

	hour = splitEntry[1].split(':')[0]
	minute = splitEntry[1].split(':')[1][:-1]

	timestamp = year + month + day + hour + minute

	return int(timestamp)


def loadLinesFromFile():
	f = open("advent4.txt", "r")
	lines = f.readlines()
	return lines

advent4_1()