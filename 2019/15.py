import intcode_computer
import curses

def advent_15a():

	comp = setup()

	pos = (0,0)
	positions = {}
	positions[pos] = 's'

	moves = []

	output = 0
	starting = True

	# minx = 0
	# miny = 0
	# maxx = 0
	# maxy = 0

	while moves or starting:
		retrace = False
		direction = pick_dir(pos, positions)

		if direction == -1:
			direction = reverse_dir(moves.pop())
			retrace = True
		
		comp.input(direction)
		comp.run_pause_on_input_and_output()
		output = comp.output

		new_pos = get_new_pos(pos, direction)

		# minx = min(new_pos[0], minx)
		# maxx = max(new_pos[0], maxx)
		# miny = min(new_pos[1], miny)
		# maxy = max(new_pos[1], maxy)

		if output == 0:
			positions[new_pos] = '#'
		elif output == 1:
			positions[new_pos] = '.'
			if not retrace:
				moves.append(direction)
				starting = False
			pos = new_pos
		elif output == 2:
			positions[new_pos] = 'o'
			if not retrace:
				moves.append(direction)
				starting = False
			pos = new_pos

	# map_str = ''
	# for y in range(maxy, miny - 1, -1):
	# 	for x in range(minx, maxx + 1):
	# 		char = positions.get((x, y))
	# 		if char == None:
	# 			char = ' '
	# 		map_str += char
	# 	map_str += '\n'

	# print(map_str)



	curr = (0, 0)
	checked_pos = set()
	checked_pos.add(curr)

	pos_to_check = [[curr, 0]]

	oxygen_found = False

	while pos_to_check or not oxygen_found:
		checking = pos_to_check.pop(0)
		curr = checking[0]
		dist = checking[1]
		for adj in adjacent_pos(curr):
			if not checked_pos.__contains__(adj) and positions[adj] == '.':
				pos_to_check.append([adj, dist + 1])
				checked_pos.add(adj)
			if positions[adj] == 'o':
				return dist + 1

	return -1

def adjacent_pos(pos):
	adj = []
	for i in range(1, 5):
		adj.append(get_new_pos(pos, i))

	return adj

def reverse_dir(direction):
	if direction == 1:
		return 2
	if direction == 2:
		return 1
	if direction == 3:
		return 4
	if direction == 4:
		return 3

def pick_dir(pos, positions):
	if positions.get((pos[0], pos[1] + 1)) is None:
		return 1
	elif positions.get((pos[0], pos[1] - 1)) is None:
		return 2
	elif positions.get((pos[0] - 1, pos[1])) is None:
		return 3
	elif positions.get((pos[0] + 1, pos[1])) is None:
		return 4
	else:
		return -1
		
def get_new_pos(pos, direction):
	if direction == 1:
		return (pos[0], pos[1] + 1)
	if direction == 2:
		return (pos[0], pos[1] - 1)
	if direction == 3:
		return (pos[0] - 1, pos[1])
	if direction == 4:
		return (pos[0] + 1, pos[1])

def setup():
	f = open("15.txt", "r")
	intcode_str = f.readline()
	intcode = list(map(int, intcode_str.split(",")))

	comp = intcode_computer.Intcode_computer(intcode)
	return comp



print(advent_15a())