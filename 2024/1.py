import readInput
from collections import Counter

def solve():
	lines = readInput.yieldLines("1")
	l = map(parseLine, lines)
	a, b = list(map(list, zip(*l)))
	print(p1(a, b))
	print(p2(a, b))


def p1(a, b):
	a.sort()
	b.sort()
	return sum([abs(b - a) for a, b in zip(a, b)])

def p2(a, b):
	bCounts = Counter(b)
	return sum([x * bCounts[x] for x in a])


def parseLine(line):
	return list(map(int, line.strip().split()))

if __name__ == "__main__":
	solve()