import intcode_computer

def advent_17a():
	comp = setup()

	output = []
	while not comp.finished:
		comp.run_pause_on_input_and_output()
		output.append(comp.output)

	map_string = ''

	for val in output:
		map_string += ascii(val)

	print(map_string)

def setup():
	f = open("17.txt", 'r')
	intcode_str = f.readline()
	intcode = list(map(int, intcode_str.split(",")))

	comp = intcode_computer.Intcode_computer(intcode)
	return comp

advent_17a()