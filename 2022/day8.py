def arrProd(arr):
	prod = 1
	for x in arr:
		prod *= x
	return prod

f = open("input/08")

data = f.readlines()

grid = []

for x in data:
	x = x.strip()
	grid.append(list(map(int, x)))

visible = set()

for i in range(len(grid)):
	highest = -1
	pos = 0
	while highest < 9 and pos < len(grid[0]):
		if grid[i][pos] > highest:
			visible.add((i, pos))
			highest = grid[i][pos]
		pos += 1

	highest = -1
	pos = len(grid[0]) - 1
	while highest < 9 and pos >= 0:
		if grid[i][pos] > highest:
			visible.add((i, pos))
			highest = grid[i][pos]
		pos -= 1

for i in range(len(grid[0])):
	highest = -1
	pos = 0
	while highest < 9 and pos < len(grid):
		if grid[pos][i] > highest:
			visible.add((pos, i))
			highest = grid[pos][i]
		pos += 1

	highest = -1
	pos = len(grid) - 1
	while highest < 9 and pos >= 0:
		if grid[pos][i] > highest:
			visible.add((pos, i))
			highest = grid[pos][i]
		pos -= 1

print(len(visible))

viewgrid = []

for i in range(len(grid)):
	viewgrid.append([])
	for j in range(len(grid[0])):
		viewgrid[i].append([0, 0, 0, 0])


for i in range(len(grid)):
	lastseen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for j in range(len(grid[0])):
		height = grid[i][j]
		viewgrid[i][j][0] = j - lastseen[height]
		lastseen = [j] * (height + 1) + lastseen[height + 1:]

for i in range(len(grid)):
	lastseen = [len(grid[0]) - 1] * 10
	for j in range(len(grid[0]) - 1, -1, -1):
		height = grid[i][j]
		viewgrid[i][j][1] = lastseen[height] - j
		lastseen = [j] * (height + 1) + lastseen[height + 1:]

for i in range(len(grid[0])):
	lastseen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for j in range(len(grid)):
		height = grid[j][i]
		viewgrid[j][i][2] = j - lastseen[height]
		lastseen = [j] * (height + 1) + lastseen[height + 1:]

for i in range(len(grid[0])):
	lastseen = [len(grid) - 1] * 10
	for j in range(len(grid) - 1, -1, -1):
		height = grid[j][i]
		viewgrid[j][i][3] = lastseen[height] - j
		lastseen = [j] * (height + 1) + lastseen[height + 1:]

highscore = 0
for x in viewgrid:
	for y in x:
		score = arrProd(y)
		highscore = max(score, highscore)

print(highscore)

