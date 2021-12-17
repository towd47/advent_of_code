def adjacent_pts(row, col, rows, cols):
	pts = []
	if row != 0:
		pts.append([row - 1, col])
	if row != rows - 1:
		pts.append([row + 1, col])
	if col != 0:
		pts.append([row, col - 1])
	if col != cols - 1:
		pts.append([row, col + 1])
	return pts

day15_input = open("../day_15_input.txt")
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

score_grid[0][0] = risks[0][0]

adj = adjacent_pts(0, 0, rows, cols)
pts_to_check = [[0, 0]]
while pts_to_check:
	ad = pts_to_check.pop(0)
	ads_ads = adjacent_pts(ad[0], ad[1], rows, cols)
	for ads_ad in ads_ads:
		if score_grid[ad[0]][ad[1]] > score_grid[ads_ad[0]][ads_ad[1]] + risks[ad[0]][ad[1]]:
			score_grid[ad[0]][ad[1]] = score_grid[ads_ad[0]][ads_ad[1]] + risks[ad[0]][ad[1]]
			for ads_ad in ads_ads:
				if ads_ad not in pts_to_check:
					pts_to_check.append(ads_ad)
		elif score_grid[ad[0]][ad[1]] + risks[ads_ad[0]][ads_ad[1]] < score_grid[ads_ad[0]][ads_ad[1]]:
			score_grid[ads_ad[0]][ads_ad[1]] = score_grid[ad[0]][ad[1]] + risks[ads_ad[0]][ads_ad[1]]
			pts_to_check.append(ads_ad)				
				

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

big_score_grid[0][0] = big_risks[0][0]

adj = adjacent_pts(0, 0, rows, cols)
pts_to_check = [[0, 0]]
while pts_to_check:
	ad = pts_to_check.pop(0)
	ads_ads = adjacent_pts(ad[0], ad[1], rows, cols)
	for ads_ad in ads_ads:
		if big_score_grid[ad[0]][ad[1]] > big_score_grid[ads_ad[0]][ads_ad[1]] + big_risks[ad[0]][ad[1]]:
			big_score_grid[ad[0]][ad[1]] = big_score_grid[ads_ad[0]][ads_ad[1]] + big_risks[ad[0]][ad[1]]
			for ads_ad in ads_ads:
				if ads_ad not in pts_to_check:
					pts_to_check.append(ads_ad)
		elif big_score_grid[ad[0]][ad[1]] + big_risks[ads_ad[0]][ads_ad[1]] < big_score_grid[ads_ad[0]][ads_ad[1]]:
			big_score_grid[ads_ad[0]][ads_ad[1]] = big_score_grid[ad[0]][ad[1]] + big_risks[ads_ad[0]][ads_ad[1]]
			pts_to_check.append(ads_ad)		

print(big_score_grid[rows-1][cols-1] - big_score_grid[0][0])
