from readInput import yieldLines

def solve():
	lines = [[int(x) for x in x.strip().split()] for x in yieldLines('2')]
	print(p1(lines))
	print(p2(lines))

def p1(lines):
	return sum([safe1(line) for line in lines])

def p2(lines):
	return sum([safe2(line) for line in lines])

def safe1(line):
	inc = line[1] - line[0] > 0
	for i, e in enumerate(line):
		if i < len(line) - 1:
			diff = line[i + 1] - e
			if diff == 0 or (inc and diff < 0) or (not inc and diff > 0):
				return False
			if abs(diff) > 3:
				return False
	return True

def safe2(line):
	if len(line) <= 2:
		return True
	if safe1(line):
		return True

	inc = [0] * (len(line) - 1)
	dec = [0] * (len(line) - 1)
	errors = [0] * (len(line) - 1)
	for i, e in enumerate(line):
		if i < len(line) - 1:
			diff = line[i + 1] - e
			if diff > 0:
				inc[i] = 1 
			if diff < 0:
				dec[i] = 1
			if diff == 0:
				errors[i] = 1
			if abs(diff) > 3:
				errors[i] = 1

	if min(sum(inc), sum(dec)) > 1:
		return False
	if sum(inc) > sum(dec):
		for i, e in enumerate(dec):
			if e == 1:
				errors[i] = 1
	if sum(inc) <= sum(dec):
		for i, e in enumerate(inc):
			if e == 1:
				errors[i] = 1
	i = errors.index(1)
	l1 = line[:i] + line[i+1:]
	l2 = line[:i+1] + line[i+2:]
	return safe1(l1) or safe1(l2)

if __name__ == '__main__':
	solve()