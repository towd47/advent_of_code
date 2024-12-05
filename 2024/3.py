from readInput import yieldLines
import re
import sys

def solve(filename='3'):
	lines = [line for line in yieldLines(filename)]
	lines = "".join(lines)
	print(p1(lines))
	print(p2(lines))

def p1(lines):
	matches = re.findall(r'mul\(([\d]{1,3},[\d]{1,3})\)', lines)
	return sum([int(m) * int(n) for m, n in (match.split(',') for match in matches)])

def p2(lines):
	matches = re.findall(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', lines)
	do = True
	tot = 0
	for m in matches:
		match m:
			case "do()":
				do = True
			case "don't()":
				do = False
			case _:
				if do:
					m = m.strip("mul()").split(',')
					tot += int(m[0]) * int(m[1])
	return tot

if __name__ == '__main__':
	if len(sys.argv) >= 2:
		filename = sys.argv[1]
		solve(filename)
	else:
		solve()