INPUT_PATH = "../inputs/day_15_input.txt"

class Point:
	row = 0
	col = 0

def adjacent_pts(row, col, rows, cols):
	pts = []
	if row != 0:
		pt = Point()
		pt.row = row - 1
		pt.col = col
		pts.append(pt)
	if row != rows - 1:
		pt = Point()
		pt.row = row + 1
		pt.col = col
		pts.append(pt)
	if col != 0:
		pt = Point()
		pt.row = row
		pt.col = col - 1
		pts.append(pt)
	if col != cols - 1:
		pt = Point()
		pt.row = row
		pt.col = col + 1
		pts.append(pt)
	return pts


day15_input = open(INPUT_PATH)
data = day15_input.readlines()

risks = []
for x in data:
	x = x.strip()
	risks.append(list(map(int, list(x))))

score_grid = []
for x in range(len(risks[0])):
	score_grid.append([10000] * len(risks))

rows = len(risks)
cols = len(risks[0])

def find_scores(risks, score_grid):
	rows = len(risks)
	cols = len(risks[0])

	score_grid[0][0] = risks[0][0]

	adj = adjacent_pts(0, 0, rows, cols)
	start = Point()
	pts_to_check = [start]
	while pts_to_check:
		point = pts_to_check.pop(0)
		adjacents = adjacent_pts(point.row, point.col, rows, cols)
		for adj_point in adjacents:
			if score_grid[point.row][point.col] > score_grid[adj_point.row][adj_point.col] + risks[point.row][point.col]:
				score_grid[point.row][point.col] = score_grid[adj_point.row][adj_point.col] + risks[point.row][point.col]
				for adj_point in adjacents:
					if adj_point not in pts_to_check:
						pts_to_check.append(adj_point)
			elif score_grid[point.row][point.col] + risks[adj_point.row][adj_point.col] < score_grid[adj_point.row][adj_point.col]:
				score_grid[adj_point.row][adj_point.col] = score_grid[point.row][point.col] + risks[adj_point.row][adj_point.col]
				pts_to_check.append(adj_point)	
	return score_grid			
				
score_grid = find_scores(risks, score_grid)
print(score_grid[rows - 1][cols - 1] - score_grid[0][0])

big_risks = []
for j in range(5):
	for i in range(len(risks)):
		new_risks = []
		for k in range(5):
			new_risk = list(map(lambda x: ((x + j + k) % 10 + 1) if (x + j + k > 9) else (x + j + k), risks[i]))
			new_risks.extend(new_risk)
		big_risks.append(new_risks)

big_score_grid = []
for x in range(len(big_risks[0])):
	big_score_grid.append([10000] * len(big_risks))

rows = len(big_risks)
cols = len(big_risks[0])

big_score_grid = find_scores(big_risks, big_score_grid)

print(big_score_grid[rows-1][cols-1] - big_score_grid[0][0])
