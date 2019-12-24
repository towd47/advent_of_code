import intcode_computer

def advent_2a():
	f = open("2.txt", "r")
	opcode_string = f.readline()
	opcode = list(map(int, opcode_string.split(",")))
	opcode[1] = 12
	opcode[2] = 2

	comp = intcode_computer.Intcode_computer(opcode)
	comp.run()

	return comp.intcode[0]

def advent_2b():

	f = open("2.txt", "r")
	opcode_string = f.readline()
	initial_opcode = list(map(int, opcode_string.split(",")))

	for noun in range(0, 99):
		for verb in range(0, 99):
			opcode = initial_opcode.copy()
			opcode[1] = noun
			opcode[2] = verb

			comp = intcode_computer.Intcode_computer(opcode)
			comp.run()


			if comp.intcode[0] == 19690720:
				return 100 * noun + verb

	return -1

print("2a: ", advent_2a())
print("2b: ", advent_2b())