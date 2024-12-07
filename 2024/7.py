from readInput import yieldLines
import sys

def solve(filename='7'):
	lines = yieldLines(filename)

	equations = []
	for line in lines:
		line = line.strip().split(': ')
		line[0] = int(line[0])
		line[1] = [int(c) for c in line[1].split()]
		equations.append(line)

	print(sum([eq[0] if isValid(eq) else 0 for eq in equations]))
	print(sum([eq[0] if isValid2(eq) else 0 for eq in equations]))

	
def isValid(eq):
	tots = set()
	for val in eq[1]:
		if not tots:
			tots.add(val)
		else:
			temp = set()
			for v in tots:
				v1 = v * val
				v2 = v + val
				if v1 <= eq[0]:
					temp.add(v1)
				if v2 <= eq[0]:
					temp.add(v2)
				tots = temp

	return eq[0] in tots

def isValid2(eq):
	tots = set()
	for val in eq[1]:
		if not tots:
			tots.add(val)
		else:
			temp = set()
			for v in tots:
				v1 = v * val
				v2 = v + val
				v3 = int(f"{v}{val}")
				if v1 <= eq[0]:
					temp.add(v1)
				if v2 <= eq[0]:
					temp.add(v2)
				if v3 <= eq[0]:
					temp.add(v3)
				tots = temp

	return eq[0] in tots	


if __name__ == '__main__':
	if len(sys.argv) >= 2:
		filename = sys.argv[1]
		solve(filename)
	else:
		solve()