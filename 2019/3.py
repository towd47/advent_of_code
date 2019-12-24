def read_input():
	f = open("3.txt", "r")
	path1 = f.readline()
	path2 = f.readline()

	return path1.split(","), path2.split(",")

def advent_3a():
	path1, path2 = read_input()

	path1_segments = find_segments(path1)
	path2_segments = find_segments(path2)

	intersections = find_intersections(path1_segments, path2_segments)

	min_dist = 100000
	for point in intersections:
		dist = abs(point[0]) + abs(point[1])
		if dist < min_dist:
			min_dist = dist

	return min_dist

def advent_3b():
	path1, path2 = read_input()

	path1_segments = find_segments(path1)
	path2_segments = find_segments(path2)

	intersections = find_intersections(path1_segments, path2_segments)

	min_dist = 10000000
	for intersection in intersections:
		dist = path_dist_to_point(path1, intersection) + path_dist_to_point(path2, intersection)
		if dist < min_dist:
			min_dist = dist

	return min_dist

def dist(point1, point2):
	return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def path_dist_to_point(path, point):
	current_pos = (0, 0)
	total_dist = 0

	for instruction in path:
		distance = int(instruction[1:])
		end_pos = path_pos_coverage(instruction, current_pos)

		if is_point_on_line(point, current_pos, end_pos):
			total_dist += dist(point, (current_pos[0], current_pos[1]))
			return total_dist
		else:
			total_dist += distance

		current_pos = end_pos

	return total_dist

		

def is_point_on_line(point, start_pos, end_pos):
	return point in line_points(start_pos, end_pos)

def find_segments(path):
	segments = list()
	current_pos = (0, 0)
	for path_instruction in path:
		end_pos = path_pos_coverage(path_instruction, current_pos)
		segments.append((current_pos, end_pos))
		current_pos = end_pos

	return segments

def find_intersections(path1_segments, path2_segments):
	intersections = set()

	for segment1 in path1_segments:
		for segment2 in path2_segments:
			intersecting_points = set(line_points(segment1[0], segment1[1])) & set(line_points(segment2[0], segment2[1]))
			if len(intersecting_points) > 0:
				intersections.update(intersecting_points)

	intersections.discard((0, 0))

	return intersections

def path_pos_coverage(path_instruction, start_pos) :
	direction = path_instruction[0]
	distance = int(path_instruction[1:])

	if direction == "U":
		end_pos = (start_pos[0], start_pos[1] + distance)
	elif direction == "R":
		end_pos = (start_pos[0] + distance, start_pos[1])
	elif direction == "L":
		end_pos = (start_pos[0] - distance, start_pos[1])
	elif direction == "D":
		end_pos = (start_pos[0], start_pos[1] - distance)
	else:
		end_pos = start_pos

	return end_pos

def is_vertical(start_pos, end_pos):
	if (start_pos[0] == end_pos[0]) :
		return True
	else:
		return False

def line_points(start_pos, end_pos):
	points = list()
	if is_vertical(start_pos, end_pos):
		if start_pos[1] > end_pos[1]:
			yrange = range(end_pos[1], start_pos[1] + 1)
		else :
			yrange = range(start_pos[1], end_pos[1] + 1)
		
		for y in yrange:
			points.append((start_pos[0], y))
	else :
		if start_pos[0] > end_pos[0]:
			x_range = range(end_pos[0], start_pos[0] + 1)
		else :
			x_range = range(start_pos[0], end_pos[0] + 1)
		
		for x in x_range:
			points.append((x, start_pos[1]))

	return points

print("3a: ", advent_3a())
print("3b: ", advent_3b())
