import sys
import copy

lines = sys.stdin.readlines()
cucs = []
for line in lines:
	line = line.strip()
	cucs.append(list(line))

def step(cucs):
	changed = False
	new_cucs = []
	for i in range(len(cucs)):
		new_cucs.append(['.'] * len(cucs[0]))
	for i in range(len(cucs)):
		for j in range(len(cucs[0])):
			next_cuc = j+1
			if j+1 == len(cucs[0]):
				next_cuc = 0
			if cucs[i][j] == '>' and cucs[i][next_cuc] == '.':
				new_cucs[i][next_cuc] = '>'
				changed = True
			elif cucs[i][j] == '>':
				new_cucs[i][j] = '>'

	for i in range(len(cucs[0])):
		for j in range(len(cucs)):
			next_cuc = j+1
			if j+1 == len(cucs):
				next_cuc = 0
			if cucs[j][i] == 'v' and new_cucs[next_cuc][i] == '.' and cucs[next_cuc][i] != 'v':
				new_cucs[next_cuc][i] = 'v'
				changed = True
			elif cucs[j][i] == 'v':
				new_cucs[j][i] = 'v'

	return new_cucs, changed

cucs, changed = step(cucs)
i = 1
while changed:
	i += 1
	cucs, changed = step(cucs)
print(i)