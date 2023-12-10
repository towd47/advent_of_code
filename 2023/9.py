import readInput

def predictNext(history):
	diffL = diffList(history)
	if len(set(diffL)) == 1:
		return history[-1] + diffL[-1]
	return history[-1] + predictNext(diffL)

def predictPrev(history):
	diffL = diffList(history)
	if len(set(diffL)) == 1:
		return history[0] - diffL[0]
	return history[0] - predictPrev(diffL)

def diffList(list):
	diff = []
	for i, e in enumerate(list):
		if i == len(list) - 1:
			continue
		diff.append(list[i+1] - e)
	return diff

def lineToHist(line):
	hist = [int(x) for x in line.split()]
	return hist

def p1(historys):
	return sum(list(map(predictNext, historys)))

def p2(historys):
	return sum(list(map(predictPrev, historys)))

lines = readInput.yieldLines("9")
historys = []

for line in lines:
	historys.append(lineToHist(line))

print(p1(historys))
print(p2(historys))