def advent2_1():

	f = open("advent2.txt", "r")

	lines = f.readlines()

	twos = 0
	threes = 0

	twoFound = False
	threeFound = False

	for line in lines:
		while len(line) > 1:
			if not twoFound and howManyApperances(line[0], line) == 2:
				twos += 1
				twoFound = True
			elif not threeFound and howManyApperances(line[0], line) == 3:
				threes += 1
				threeFound = True
			line = line.replace(line[0], "")
			if threeFound and twoFound:
				line = ""
		twoFound = False
		threeFound = False

	print(twos * threes)

def advent2_2():

	f = open("advent2.txt", "r")
	lines = f.readlines()

	string1 = ""
	string2 = ""

	for i in range(len(lines) - 1):
		for j in range(i + 1, len(lines)):
			if numCharsDifferent(lines[i], lines[j]) == 1:
				print(getSameChars(lines[i], lines[j]))
				break;


def getSameChars(string1, string2):
	string = ""
	for i in range(len(string1) - 1):
		if string1[i] == string2[i]:
			string = string + string1[i]
	return string

def numCharsDifferent(string1, string2):
	diff = 0
	for i in range(len(string1) - 1):
		if not string1[i] == string2[i]:
			diff += 1
	return diff


def howManyApperances(letter, string):
	appears = 0
	for c in string:
		if c == letter:
			appears += 1
			if appears > 3:
				return appears
	return appears

advent2_1()
advent2_2()