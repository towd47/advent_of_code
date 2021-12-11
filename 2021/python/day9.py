def is_low_point(depths, row, col):
	point = depths[row][col]
	rows = len(depths)
	cols = len(depths[0])
	lower_than_above = (row == 0 or depths[row-1][col] > point)
	lower_than_below = (row == rows - 1 or depths[row+1][col] > point)
	lower_than_left = (col == 0 or depths[row][col-1] > point)
	lower_than_right = (col == cols - 1 or depths[row][col + 1] > point)
	return lower_than_above and lower_than_below and lower_than_left and lower_than_right

def adjacent_pts(pt, rows, cols):
	pts = []
	if pt[0] != 0:
		pts.append([pt[0] - 1, pt[1]])
	if pt[0] != rows - 1:
		pts.append([pt[0] + 1, pt[1]])
	if pt[1] != 0:
		pts.append([pt[0], pt[1] - 1])
	if pt[1] != cols - 1:
		pts.append([pt[0], pt[1] + 1])
	return pts


day9_input = open("../day_9_input.txt")
data = day9_input.readlines()

depths = []

for line in data:
	line = line.strip()
	depths.append(list(map(int, list(line))))

risk = 0
not_9s = 0

for i in range(len(depths)):
	for j in range(len(depths[0])):
		if depths[i][j] != 9:
			not_9s += 1
		if is_low_point(depths, i, j):
			risk = risk + depths[i][j] + 1

print(risk)

pos = [0, 0]

poses_to_check = [pos]
next_basin_pos = []

rows = len(depths)
cols = len(depths[0])

basin_size = 0
basins = []

while poses_to_check:
	for r in depths:
		for c in r:
			print(c, end=' ')
		print()
	input()
	[x, y] = poses_to_check.pop()
	if depths[x][y] != 'x':
		if depths[x][y] != 9:
			basin_size += 1
		adj = adjacent_pts([x, y], rows, cols)
	
		for ad in adj:
			if depths[ad[0]][ad[1]] != 'x':
				if depths[x][y] != 9:
					poses_to_check.append(ad)
				else:
					next_basin_pos.append(ad)
		depths[x][y] = 'x'
			
	if not poses_to_check:
		basins.append(basin_size)
		basin_size = 0
		if next_basin_pos:
			next_pos = next_basin_pos.pop()
			while depths[next_pos[0]][next_pos[1]] == 'x' and len(next_basin_pos) > 0:
				next_pos = next_basin_pos.pop()
			poses_to_check.append(next_pos)


basins = sorted(basins, reverse = True)

print(basins[0] * basins[1] * basins[2])
