import math

def advent_10():
	f = open("10.txt", "r")

	lines = f.readlines()

	astroid_locations = []

	for line_num in range(0, len(lines)):
		line = lines[line_num]
		for char_num in range(0, len(line)):
			char = line[char_num]
			if char == "#":
				astroid_locations.append((line_num, char_num))

	max_vis = 0
	max_vis2 = 0
	max_vis_pos = None
	max_vis_angle_set = None

	for astroid in astroid_locations:
		other_astroids = astroid_locations.copy()
		other_astroids.remove(astroid)

		angle_set = set()

		while other_astroids:
			a = other_astroids.pop()
			xdiff = a[0] - astroid[0]
			ydiff = a[1] - astroid[1]

			angle = math.degrees(math.atan2(ydiff, xdiff))
			if angle >= 0:
				angle = 180 - angle
			if angle < 0:
				angle = 180 - angle
			angle_set.add(angle)			

		if len(angle_set) > max_vis:
			max_vis = len(angle_set)
			max_vis_pos = astroid
			max_vis_angle_set = angle_set

	print("10a: ", max_vis)

	other_astroids = astroid_locations.copy()
	other_astroids.remove(max_vis_pos)

	angle_astroids_dict = {}

	count = 0
	for astroid in other_astroids:
		xdiff = astroid[0] - max_vis_pos[0]
		ydiff = astroid[1] - max_vis_pos[1]

		angle = math.degrees(math.atan2(ydiff, xdiff))
		if angle >= 0:
			angle = 180 - angle
		if angle < 0:
			angle = 180 - angle

		angle_list = angle_astroids_dict.get(angle)
		if angle_list is None:
			angle_list = []
		angle_list.append(astroid)
		angle_astroids_dict[angle] = angle_list


	keys = list(angle_astroids_dict.keys())
	keys.sort()

	count = 0
	while keys and count < 200:
		count += 1
		key = keys.pop(0)
		angle_list = angle_astroids_dict.get(key)
		angle_list.sort(key = lambda x: abs(x[0] - max_vis_pos[0]) + abs(x[1] - max_vis_pos[1]))

		zapped_roid = angle_list.pop(0)
		if count == 200:
			print("10b: ", zapped_roid[1] * 100 + zapped_roid[0])
			return
		if angle_list:
			angle_astroids_dict[key] = angle_list
			keys.append(key)



def find_min_val(x, y):
	for i in range(2, max(abs(x), abs(y)) + 1):
		if x % i == 0 and y % i == 0:
			x = x / i
			y = y / i

	return int(x), int(y)



advent_10()


