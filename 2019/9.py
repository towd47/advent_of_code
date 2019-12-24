import intcode_computer

def advent_9a():
	return run_intcode(1)

def advent_9b():
	return run_intcode(2)

def run_intcode(input):
	f = open("9.txt", "r")
	intcode_str = f.readline()

	intcode_base = list(map(int, intcode_str.split(",")))

	comp = intcode_computer.Intcode_computer(intcode_base)
	comp.input(input)
	comp.run()

	return comp.output

print("9a: ", advent_9a())
print("9b: ", advent_9b())