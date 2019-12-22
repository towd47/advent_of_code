import intcode_computer

def advent_2a():
	f = open("2.txt", "r")
	opcode_string = f.readline()
	opcode = list(map(int, opcode_string.split(",")))

	opcode = intcode_computer.initialize_state(opcode, 12, 2)

	return opcode[0]

def advent_2b():

	f = open("2.txt", "r")
	opcode_string = f.readline()
	initial_opcode = list(map(int, opcode_string.split(",")))

	for noun in range(0, 99):
		for verb in range(0, 99):

			opcode = initial_opcode.copy()
			opcode = intcode_computer.initialize_state(opcode, noun, verb)

			if opcode[0] == 19690720:
				return 100 * noun + verb

	return -1

print(advent_2a())
print(advent_2b())