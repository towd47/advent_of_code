from readInput import oneString
import sys

def solve(filename='11'):
	line = oneString(filename).strip().split()

	for _ in range(25):
		vals = fullStep(vals)

	print(sum([vals[v] for v in vals]))

	for _ in range(50):
		vals = fullStep(vals)

	print(sum([vals[v] for v in vals]))


def fullStep(vals):
	newVals = dict()
	for val in vals:
		amount = vals[val]
		nextStep = step(val)
		for v in nextStep:
			if v in newVals:
				newVals[v] += amount
			else:
				newVals[v] = amount
	return newVals

def step(val):
	if int(val) == 0:
		return ['1']

	l = len(val)
	if l % 2 == 0:
		v1 = val[:l//2]
		v2 = val[l//2:]
		v2 = v2.lstrip('0')
		if not v2:
			v2 = '0'
		return [v1, v2]

	return [str(int(val) * 2024)]

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        solve(filename)
    else:
        solve()