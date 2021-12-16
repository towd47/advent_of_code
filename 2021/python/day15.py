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

# for row in range(rows):
# 	for col in range(cols):
adj = adjacent_pts(0, 0, rows, cols)
pts_to_check = [[0, 0]]
while pts_to_check:
	# for z in range(len(score_grid)):
	# 	print(score_grid[z])
	# input()
	ad = pts_to_check.pop()
	ads_ads = adjacent_pts(ad[0], ad[1], rows, cols)
	ad_score = score_grid[ad[0]][ad[1]]
	for ads_ad in ads_ads:
		if ad_score > score_grid[ads_ad[0]][ads_ad[1]] + risks[ad[0]][ad[1]]:
			score_grid[ad[0]][ad[1]] = score_grid[ads_ad[0]][ads_ad[1]] + risks[ad[0]][ad[1]]
			for ads_ad in ads_ads:
				if ads_ad not in pts_to_check:
					pts_to_check.append(ads_ad)
		elif ad_score + risks[ads_ad[0]][ads_ad[1]] < score_grid[ads_ad[0]][ads_ad[1]]:
			score_grid[ads_ad[0]][ads_ad[1]] = ad_score + risks[ads_ad[0]][ads_ad[1]]
			pts_to_check.append(ads_ad)
				
				

print(score_grid)


