import heapq

INPUT_PATH = "../inputs/day_15_input.txt"

class Point:
	row = 0
	col = 0
	score = 0

	def __lt__(self, other):
		return self.score < other.score

	def id(self):
		return self.row * 10000 + self.col

	def __str__(self):
		return "Row: " + str(self.row) + " Col: " + str(self.col) + " Score: " + str(self.score)

def adjacent_pts(point, rows, cols):
	pts = []
	row = point.row
	col = point.col
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

def best_first(risks):
	start = Point()
	start.score = risks[0][0]

	points = {}
	points[start.id()] = start
	points_to_check = [start]
	heapq.heapify(points_to_check)

	rows = len(risks)
	cols = len(risks[0])
	while points_to_check:
		point = heapq.heappop(points_to_check)
		adj = adjacent_pts(point, rows, cols)
		for pt in adj:
			if pt.id() not in points:
				pt.score = point.score + risks[pt.row][pt.col]
				points[pt.id()] = pt
				heapq.heappush(points_to_check, pt)

	end = points[(rows - 1) * 10000 + cols - 1]

	print(end.score - start.score)

day15_input = open(INPUT_PATH)
data = day15_input.readlines()

risks = []
for x in data:
	x = x.strip()
	risks.append(list(map(int, list(x))))

big_risks = []
for j in range(5):
	for i in range(len(risks)):
		new_risks = []
		for k in range(5):
			new_risk = list(map(lambda x: ((x + j + k) % 10 + 1) if (x + j + k > 9) else (x + j + k), risks[i]))
			new_risks.extend(new_risk)
		big_risks.append(new_risks)

best_first(risks)
best_first(big_risks)
