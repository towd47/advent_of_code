import readInput

def lineToInstruction(line):
	line = line.strip()
	d, n, c = line.split()
	c = c.strip("()")
	n = int(n)

	return (d, n, c)

def hexToInst(hexCode):
	n = hexCode[1:-1]
	d = hexCode[-1]
	if d == "0":
		d = "R"
	elif d == "1":
		d = "D"
	elif d == "2":
		d = "L"
	else:
		d = "U"
	n = int(n, 16)
	return (d, n)

def getVector(d):
	if d == "U":
		return (0, 1)
	if d == "D":
		return (0, -1)
	if d == "R":
		return (1, 0)
	return (-1, 0)

def getCorners(instructions):
	p = (0, 0)
	pts = [p]
	for d, n in instructions:
		v = getVector(d)
		v = (v[0] * n, v[1] * n)
		p = addPoint(p, v)
		pts.append(p)
	return pts

def addTurnDirToCorners(corners):
	p = 0
	highest = corners[0][0]
	for i, e in corners:
		if e[0] > highest:
			p = i
	

def addPoint(p, v):
	return (p[0] + v[0], p[1] + v[1])

def solve():
	lines = readInput.yieldLines("test")
	instructions = list(map(lineToInstruction, lines))
	p1Ins = [(x, y) for (x, y, _) in instructions]
	p2Ins = [hexToInst(x) for (_, _, x) in instructions]
	p1(p1Ins)
	p2(p2Ins)



def p1(instructions):
	pts = getCorners(instructions)
	print(pts)

def p2(instructions):
	pts = getCorners(instructions)
	

if __name__ == "__main__":
	solve()


