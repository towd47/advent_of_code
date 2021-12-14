def next_step_octopus(octopus):
	flashes = 0
	rows = len(octopus)
	cols = len(octopus[0])
	for row in range(rows):
		for col in range(cols):
			octopus[row][col] += 1
	
	pts_to_check = []
	for row in range(rows):
		for col in range(cols):
			if octopus[row][col] > 9:
				flashes += 1
				for ad in adjacent_pts(row, col, rows, cols):
					octopus[ad[0]][ad[1]] += 1
					pts_to_check.append(ad)
				octopus[row][col] = -50

	while pts_to_check:
		pt = pts_to_check.pop()
		if octopus[pt[0]][pt[1]] > 9:
			flashes += 1
			for ad in adjacent_pts(pt[0], pt[1], rows, cols):
				octopus[ad[0]][ad[1]] += 1
				pts_to_check.append(ad)
			octopus[pt[0]][pt[1]] = -50


	for row in range(rows):
		for col in range(cols):
			if octopus[row][col] < 0:
				octopus[row][col] = 0
	return [flashes, octopus]

def list_of_list_sum(l):
	total = 0
	for x in l:
		total += sum(x)
	return total

def adjacent_pts(x, y, rows, cols):
	adj = []
	if x > 0:
		adj.append([x - 1, y])
		if y > 0:
			adj.append([x - 1, y - 1])
		if y < cols - 1:
			adj.append([x - 1, y + 1])
	if y > 0:
		adj.append([x, y - 1])
		if x < rows - 1:
			adj.append([x + 1, y - 1])
	if x < rows - 1:
		adj.append([x + 1, y])
		if y < cols - 1:
			adj.append([x + 1, y + 1])
	if y < cols - 1:
		adj.append([x, y + 1])

	return adj

day11_input = open("../day_11_input.txt")
data = day11_input.readlines()

octopus = []
for line in data:
	line = line.strip()
	octopus.append(list(map(int, list(line))))

flashes = 0
steps = 0
while list_of_list_sum(octopus) != 0:
	steps += 1
	[new_flashes, octopus] = next_step_octopus(octopus)
	if steps < 100:
		flashes += new_flashes

print(flashes)
print(steps)
