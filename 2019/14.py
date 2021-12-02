def read_input():
	f = open("14.txt", "r")
	lines = f.readlines()
	return lines

def advent_14a():
	lines = read_input()

	chemicals = {}

	for line in lines:
		reaction_inputs = []
		vals = line.split("=>")

		output = vals[-1].strip()
		outputs = output.split(" ")

		inputs = vals[0]
		inputs = inputs.split(",")
		for val in inputs:
			reaction_inputs.append(val.strip().split(" "))

		chemical = Chemical(outputs[1], outputs[0])
		chemicals[outputs[1]] = chemical

		while reaction_inputs:
			input_val = reaction_inputs.pop(0)
			name = input_val[1]
			num = input_val[0]

			chemical.add_input(Chemical(name, num))

	print(chemicals)

read_input()

class Chemical:
	
	def __init__(self, chemical_name, number):
		self.name = chemical_name
		self.number = number
		self.inputs = []

	def add_input(self, chemical):
		self.inputs.append(chemical)

advent_14a()