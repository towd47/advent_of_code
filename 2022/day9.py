def directionVector(direction):
	if direction == "R":
		return (0, 1)
	if direction == "L":
		return (0, -1)
	if direction == "U":
		return (1, 0)
	if direction == "D":
		return (-1, 0)

def addTup(pos, vec):
	return (pos[0] + vec[0], pos[1] + vec[1])

def tooFar(pos1, pos2):
	if abs(pos1[0] - pos2[0]) > 1 or abs(pos1[1] - pos2[1]) > 1:
		return True
	return False

def moveRope(rope, directionVector, dist, tset, lset):
	for _ in range(dist):
		rope[0] = addTup(rope[0], directionVector)
		for i in range(1, len(rope)):
			if tooFar(rope[i], rope[i-1]):
				diag = (rope[i-1][0] - rope[i][0], rope[i-1][1] - rope[i][1])
				if abs(diag[0]) > 1:
					diag = (diag[0] / abs(diag[0]), diag[1])
				if abs(diag[1]) > 1:
					diag = (diag[0], diag[1] / abs(diag[1]))
				rope[i] = addTup(rope[i], diag)
				if i == 1:
					tset.add(rope[i])
				elif i == 9:
					lset.add(rope[i])
	return (rope, tset, lset)


f = open("input/09")

data = f.readlines()

rope = [(0, 0)] * 10

tvisit = set()
tvisit.add(rope[1])

lvisit = set()
lvisit.add(rope[9])

for x in data:
	x = x.strip()
	direction, dist = x.split()
	dirvec = directionVector(direction)
	dist = int(dist)

	rope, tvisit, lvisit = moveRope(rope, dirvec, dist, tvisit, lvisit)

print(len(tvisit))
print(len(lvisit))