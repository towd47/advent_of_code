import re

def pairDist(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def overlap(r1, r2):
	return r1[0] <= r2[1] and r2[0] <= r1[1]

f = open("input/15")

data = f.readlines()

pairs = []

TARGETLINE = 2000000



for x in data:
	x = re.sub(r'[^0-9,:]', '', x)
	x = x.split(':')
	sensor = list(map(int, x[0].split(',')))
	beacon = list(map(int, x[1].split(',')))

	pairs.append((sensor, beacon))


ranges = []
beaconsInTarget = set()
for x in pairs:
	s = x[0]
	b = x[1]
	d = pairDist(s, b)
	
	toY = abs(s[1] - TARGETLINE)

	if toY <= d:
		left = d - toY
		p1 = s[0] - left
		p2 = s[0] + left
		if p1 < p2:
			ranges.append((p1, p2))
		else:
			ranges.append((p2, p1))

		if b[1] == TARGETLINE:
			beaconsInTarget.add((b[0], b[1]))


changes = True
while changes:
	changes = False
	pos = 0
	while pos < len(ranges) - 1:
		pos1 = pos + 1
		while pos1 < len(ranges):
			if overlap(ranges[pos], ranges[pos1]):
				ranges[pos] = (min(ranges[pos][0], ranges[pos1][0]), max(ranges[pos][1], ranges[pos1][1]))
				ranges.pop(pos1)
				changes = True
			else:
				pos1 += 1
		pos += 1

tot = 0



for x in ranges:
	tot += x[1] - x[0] + 1

print(tot - len(beaconsInTarget))


# 5394423
