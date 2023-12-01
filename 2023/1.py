import readInput

def getFirstAndLastNumDigits(s):
	n = [x for x in s if x.isdigit()]
	return int(n[0] + n[-1])

def getFirstAndLastNumSAndD(s):
	numWords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	replacements = ["o1e", "t2o", "t3e", "4", "5e", "6", "7n", "e8t", "n9e"]
	for x in zip(numWords, replacements):
		s = s.replace(x[0], x[1])
	return getFirstAndLastNumDigits(s)

def day1():
	total1 = 0
	total2 = 0

	for line in readInput.yieldLines("1"):
		total1 += getFirstAndLastNumDigits(line)
		total2 += getFirstAndLastNumSAndD(line)

	print(f'day1 p1: {total1}')
	print(f'day1 p2: {total2}')

if __name__ == "__main__":
	day1()