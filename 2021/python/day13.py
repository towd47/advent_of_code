def fold_dots(dots, fold_pos, fold_direction):
	if fold_direction == 'x':
		coord = 0
	else:
		coord = 1

	new_dots = set()
	removed_dots = set()
	for dot in dots:
		if dot[coord] > fold_pos:
			removed_dots.add(dot)
			dot = list(dot)
			dot[coord] = dot[coord] - (dot[coord] - fold_pos) * 2
			dot = tuple(dot)
			new_dots.add(dot)

	return new_dots | (dots ^ removed_dots)


def get_fold(fold_str):
	split = fold_str.split()
	[axis, pos] = split[2].split('=')

	return (int(pos), axis)

def print_grid(grid):
	for y in range(len(grid[0])):
		line = ''
		for x in range(len(grid)):
			line = line + grid[x][y]
		print(line)

day13_input = open("../day_13_input.txt")
data = day13_input.readlines()

dots = set()
folds = []

on_dots = True
for x in data:
	x = x.strip()
	if not x:
		on_dots = False
		continue
	if on_dots:
		[x, y] = x.split(',')
		pt = (int(x), int(y))
		dots.add(pt)
	else:
		fold = get_fold(x)
		folds.append(fold)

index = 0
for fold in folds:
	dots = fold_dots(dots, fold[0], fold[1])
	if index == 0:
		print(len(dots))
		index = 1

max_x = 0
max_y = 0
for dot in dots:
	max_x = max(max_x, dot[0])
	max_y = max(max_y, dot[1])

grid = []

for x in range(max_x + 1):

	y = [' '] * (max_y + 1)
	grid.append(y)

for dot in dots:
	grid[dot[0]][dot[1]] = '#'


print_grid(grid)

