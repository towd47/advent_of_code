import intcode_computer

def advent_5():
	f = open("5.txt", "r")
	intcode_str = f.readline()

	intcode = list(map(int, intcode_str.split(",")))

	intcode_computer.initialize_intcode(intcode)

advent_5()