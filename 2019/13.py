import intcode_computer

def advent_13a():
	comp = setup()

	grid = {}

	output = []
	while not comp.finished:
		comp.run_pause_on_input_and_output()
		output.append(comp.output)

		if len(output) == 3:
			if output[2] == 2:
				pos = (output[0], output[1])
				grid[pos] = 2
			output.clear()

	print("13a: ", len(grid))

def advent_13b():
	comp = setup()
	comp.set_memory_value(0, 2)

	grid = {}
	output = []
	while not comp.finished:
		comp.run_pause_on_input_and_output()
		output.append(comp.output)

		if len(output) == 3:
			pos = (output[0], output[1])
			grid[pos] = output[2]
			output.clear()

		if comp.waiting_for_input:
			print("WAITING FOR INPUT")
			draw_grid(grid)
			comp.input(int(input()))

def draw_grid(grid):
	keys = grid.keys()
	max_x = 0
	max_y = 0
	for key in keys:
		max_x = max(max_x, key[0])
		max_y = max(max_y, key[1])

	drawing = ""
	for i in range(0, max_x + 1):
		for j in range(0, max_y + 1):
			drawing = drawing + str(grid[(i, j)])
		drawing = drawing + "\n"

	print(drawing)

def setup():
	f = open("13.txt", "r")
	intcode_str = f.readline()
	intcode = list(map(int, intcode_str.split(",")))

	comp = intcode_computer.Intcode_computer(intcode)
	return comp

advent_13a()
advent_13b()