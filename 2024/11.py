from readInput import oneString
import sys

def solve(filename='11'):
	line = oneString(filename).strip().split()
	valmap = dict()

	print(sum([doSteps(25, 0, val, valmap) for val in line]))
	print(sum([doSteps(75, 0, val, valmap) for val in line]))
	# for key in valmap:
	# 	print(key, valmap[key])

def doSteps(totSteps, steps, val, valmap):
	if val not in valmap:
		valmap[val] = computeSteps(val)
	s, vs = valmap[val]
	if steps + s > totSteps:
		return 1
	if steps + s == totSteps:
		return 2
	return sum([doSteps(totSteps, steps + s, v1, valmap) for v1 in vs])

def computeSteps(val):
	next_vals = step(val)
	steps = 1
	while len(next_vals) == 1:
		next_vals = step(next_vals[0])
		steps += 1
	return steps, next_vals

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