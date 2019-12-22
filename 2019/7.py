import intcode_computer
import itertools

def advent_7a():
	f = open("7.txt", "r")
	intcode_str = f.readline()

	intcode_base = list(map(int, intcode_str.split(",")))

	base = [0, 1, 2, 3, 4]
	phases = itertools.permutations(base)
	max_val = 0
	
	for state in phases:
		result = 0
		state = list(state)
		while state:
			intcodea = intcode_base.copy()
			comp = intcode_computer.Intcode_computer(intcodea)
			comp.input(state.pop(0))
			comp.input(result)
			comp.run()

			result = comp.output

		max_val = max(result, max_val)

	return max_val

def advent_7b():

	f = open("7.txt", "r")
	intcode_str = f.readline()

	intcode_base = list(map(int, intcode_str.split(",")))

	phases = itertools.permutations(range(5, 10))

	max_val = 0
	
	for state in phases:
		state_copy = list(state)
		result = 0

		computers = list()

		for phase in state:
			comp = intcode_computer.Intcode_computer(intcode_base.copy())
			comp.input(phase)
			computers.append(comp)

		while not computers[0].finished:
			computers[0].input(result)
			computers[0].run()
			result = computers[0].output
			computers.append(computers.pop(0))
			
			
		max_val = max(result, max_val)

	return max_val

def manual():
	f = open("7.txt", "r")
	intcode_str = f.readline()

	intcode_base = list(map(int, intcode_str.split(",")))
	intcode_computer.initialize_intcode(intcode_base.copy())

print(advent_7a())
print(advent_7b())

