import intcode_computer

def advent_5():
	f = open("5.txt", "r")
	intcode_str = f.readline()

	intcode = list(map(int, intcode_str.split(",")))

	comp = intcode_computer.Intcode_computer(intcode)
	comp.input(1)
	comp.run()

	print("5a: ", comp.output)

	comp = intcode_computer.Intcode_computer(intcode)
	comp.input(5)
	comp.run()

	print("5b: ", comp.output)

advent_5()