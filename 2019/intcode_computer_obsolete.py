def initialize_intcode(intcode):
	return process_intcode(0, intcode, None)

def initialize_intcode_with_state(intcode, state):

	return process_intcode(0, intcode, state)

def initialize_state(intcode, arg1, arg2):
	intcode[1] = arg1
	intcode[2] = arg2
	state = None

	return process_intcode(0, intcode, state)

def process_intcode(pos, intcode, state):
	running = True
	result = None
	while running:

		instruction = intcode[pos] % 100
		mode = str(int(intcode[pos] / 100))[::-1]

		while len(mode) < 3:
			mode = mode + "0"

		if instruction == 1:
			pos, intcode = instruction_1(mode, pos, intcode)
		elif instruction == 2:
			pos, intcode = instruction_2(mode, pos, intcode)
		elif instruction == 3:
			pos, intcode, state = instruction_3(mode, pos, intcode, state)
		elif instruction == 4:
			pos, state = instruction_4(mode, pos, intcode, state)
		elif instruction == 5:
			pos = instruction_5(mode, pos, intcode)
		elif instruction == 6:
			pos = instruction_6(mode, pos, intcode)
		elif instruction == 7:
			pos, intcode = instruction_7(mode, pos, intcode)
		elif instruction == 8:
			pos, intcode = instruction_8(mode, pos, intcode)
		elif instruction == 99:
			result = instruction_99(intcode, state)
			running = False
		else:
			print(instruction)
			throw("Invalid instruction")

	return result

def instruction_1(mode, pos, intcode):
	pos1, pos2, pos3 = pos_params(mode, pos, intcode, 3)
	intcode[pos3] = intcode[pos1] + intcode[pos2]
	return pos + 4, intcode

def instruction_2(mode, pos, intcode):
	pos1, pos2, pos3 = pos_params(mode, pos, intcode, 3)
	intcode[pos3] = intcode[pos1] * intcode[pos2]
	return pos + 4, intcode

def instruction_3(mode, pos, intcode, state):
	pos1, _, _ = pos_params(mode, pos, intcode, 1)
	if state is not None:
		intcode[pos1] = state.pop()
	else:
		input_val = input("Instruction 3 input:")
		intcode[pos1] = int(input_val)
	return pos + 2, intcode, state

def instruction_4(mode, pos, intcode, state):
	pos1, _, _ = pos_params(mode, pos, intcode, 1)
	if state is not None:
		state.append(intcode[pos1])
	else:
		print(intcode[pos1])
	return pos + 2, state

def instruction_5(mode, pos, intcode):
	pos1, pos2, _ = pos_params(mode, pos, intcode, 2)
	if intcode[pos1] != 0:
		return intcode[pos2]
	else:
		return pos + 3

def instruction_6(mode, pos, intcode):
	pos1, pos2, _ = pos_params(mode, pos, intcode, 2)
	if intcode[pos1] == 0:
		return intcode[pos2]
	else:
		return pos + 3

def instruction_7(mode, pos, intcode):
	pos1, pos2, pos3 = pos_params(mode, pos, intcode, 3)
	if intcode[pos1] < intcode[pos2]:
		intcode[pos3] = 1
	else:
		intcode[pos3] = 0

	return pos + 4, intcode

def instruction_8(mode, pos, intcode):
	pos1, pos2, pos3 = pos_params(mode, pos, intcode, 3)
	if intcode[pos1] == intcode[pos2]:
		intcode[pos3] = 1
	else:
		intcode[pos3] = 0

	return pos + 4, intcode

def instruction_99(intcode, state):
	if state is not None:
		return state
	else:
		return intcode

def pos_params(mode, pos, intcode, num_params):

	pos1 = pos + 1
	pos2 = pos + 2
	pos3 = pos + 3

	if mode[0] == "0":
		pos1 = intcode[pos1]
	if mode[1] == "0" and num_params > 1:
		pos2 = intcode[pos2]
	if mode[2] == "0" and num_params > 2:
		pos3 = intcode[pos3]

	return pos1, pos2, pos3
