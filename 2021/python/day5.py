INPUT_PATH = "../inputs/day_5_input.txt"

def is_horiz(y1, y2):
	if y1 == y2:
		return True
	return False

def is_vert(x1, x2):
	if x1 == x2:
		return True
	return False

day5_input = open(INPUT_PATH)
data = day5_input.readlines()

pts = {}
for line in data:
	[p1, p2] = line.split("->")
	[x1, y1] = p1.split(",")
	[x2, y2] = p2.split(",")

	x1 = int(x1)
	x2 = int(x2)
	y1 = int(y1)
	y2 = int(y2)

	if is_horiz(y1, y2):
		if x1 > x2:
			step = -1
		else:
			step = 1
		for i in range(x1, x2 + step, step):
			key = "" + str(i) + "-" + str(y1)
			if key in pts:
				pts[key] = pts[key] + 1
			else:
				pts[key] = 1
	elif is_vert(x1, x2):
		if y1 > y2:
			step = -1
		else:
			step = 1
		for i in range(y1, y2 + step, step):
			key = "" + str(x1) + "-" + str(i)
			if key in pts:
				pts[key] = pts[key] + 1
			else:
				pts[key] = 1
	else:
		if x1 > x2:
			xstep = -1
		else:
			xstep = 1
		if y1 > y2:
			ystep = -1
		else:
			ystep = 1
		j = y1
		for i in range(x1, x2 + xstep, xstep):
			key = "" + str(i) + "-" + str(j)
			if key in pts:
				pts[key] = pts[key] + 1
			else:
				pts[key] = 1
			j += ystep

total = 0
for pt in pts:
	if pts[pt] > 1:
		total += 1

print(total)
	


