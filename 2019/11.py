import intcode_computer

def advent_11a():
	f = open("11.txt", "r")

	intcode_str = f.readline()

	intcode = list(map(int, intcode_str.split(",")))

	comp = intcode_computer.Intcode_computer(intcode)

	pos = (0, 0)
	direction = 1

	panel_colors = {}

	output = []

	while not comp.finished:
		comp.run_pause_on_input_and_output()
		if comp.waiting_for_input:
			color = panel_colors.get(pos)
			if color == 1:
				comp.input(1)
			else:
				comp.input(0)
		elif comp.sent_output:
			output.append(comp.output)

			if len(output) == 2:
				panel_colors[pos] = output[0]
				direction = next_direction(direction, output[1])
				pos = new_pos(direction, pos)
				output.clear()

	return len(panel_colors)

def advent_11b():
	f = open("11.txt", "r")

	intcode_str = f.readline()

	intcode = list(map(int, intcode_str.split(",")))

	comp = intcode_computer.Intcode_computer(intcode)

	pos = (0, 0)
	direction = 1

	panel_colors = {}
	panel_colors[pos] = 1

	output = []

	while not comp.finished:
		comp.run_pause_on_input_and_output()
		if comp.waiting_for_input:
			color = panel_colors.get(pos)
			if color == 1:
				comp.input(1)
			else:
				comp.input(0)
		elif comp.sent_output:
			output.append(comp.output)

			if len(output) == 2:
				panel_colors[pos] = output[0]
				direction = next_direction(direction, output[1])
				pos = new_pos(direction, pos)
				output.clear()

	max_x = 0
	max_y = 0
	min_x = 0
	min_y = 0

	for key in panel_colors.keys():
		max_x = max(max_x, key[0])
		min_x = min(min_x, key[0])
		max_y = max(max_y, key[1])
		min_y = min(min_y, key[1])

	output_string = ""

	for x in range(min_x, max_x + 1):
		for y in range(min_y, max_y + 1):
			cur_pos = (x, y)

			color = panel_colors.get(cur_pos)
			if color == 1:
				output_string += "#"
			else:
				output_string += " "
		output_string += "\n"


	return output_string

def next_direction(direction, turn_val):
	if turn_val == 0:
		new_dir = direction - 1
	else:
		new_dir = direction + 1

	if new_dir == 0:
		new_dir = 4
	if new_dir == 5:
		new_dir = 1

	return new_dir

def new_pos(direction, pos):
	if direction == 1:
		new_pos = (pos[0], pos[1] + 1)
	elif direction == 2:
		new_pos = (pos[0] + 1, pos[1])
	elif direction == 3:
		new_pos = (pos[0], pos[1] - 1)
	elif direction == 4:
		new_pos = (pos[0] - 1, pos[1])

	return new_pos

print("11a: ", advent_11a())
print("11b: ", advent_11b())

