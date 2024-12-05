from readInput import yieldLines
import sys

def solve(filename='5'):
	lines = yieldLines(filename)
	rules = {}
	while (line := next(lines)) != "\n":
		a, b = list(map(int, line.split('|')))
		if a in rules:
			rules[a].append(b)
		else:
			rules[a] = [b]
	instructions = [[int(val) for val in line.split(',')] for line in lines]

	valid = []
	invalid = []

	[valid.append(instruction) if isValid(instruction, rules) else invalid.append(instruction) for instruction in instructions]

	print(p1(valid))
	print(p2(rules, invalid))

def p1(instructions):
	return sum([instruction[len(instruction)//2] for instruction in instructions])

def p2(rules, instructions):
	fixed = [fixInstruction(instruction, rules) for instruction in instructions]
	return p1(fixed)

def isValid(instruction, rules):
	for i, e in enumerate(instruction):
		if i > 0 and e in rules:
			for j, e2 in enumerate(rules[e]):
				if e2 in instruction[:i]:
					return False
	return True

def fixInstruction(instruction, rules):
	for i, e in enumerate(instruction):
		if i > 0 and e in rules:
			poses = []
			for _, e2 in enumerate(rules[e]):
				if e2 in instruction[:i]:
					poses.append(instruction[:i].index(e2))
			if poses:
				poses.sort()
				del instruction[i]
				instruction.insert(poses[0], e)

	return instruction


if __name__ == '__main__':
	if len(sys.argv) >= 2:
		filename = sys.argv[1]
		solve(filename)
	else:
		solve()