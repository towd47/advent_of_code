class Intcode_computer:

	def __init__(self, intcode):
		self.intcode = self.convert_to_dict(intcode)
		self.input_buffer = list()
		self.output = 0
		self.waiting_for_input = False
		self.finished = False
		self.pos = 0
		self.mode = ""
		self.relative_base = 0
		self.sent_output = False

	def input(self, value):
		self.input_buffer.append(value)
		self.waiting_for_input = False

	def run(self):
		while not self.finished and not self.waiting_for_input:
			self.step()

	def run_pause_on_input_and_output(self):
		self.sent_output = False
		while not self.finished and not self.waiting_for_input and not self.sent_output:
			self.step()

	def step(self):

		instruction = self.get_intcode_value(self.pos) % 100
		self.mode = str(int(self.get_intcode_value(self.pos) / 100))[::-1]

		while len(self.mode) < 3:
			self.mode = self.mode + "0"

		#print("STEP VALUES: ", instruction, self.mode, self.pos, self.input_buffer)

		if instruction == 1:
			self.instruction_1()
		elif instruction == 2:
			self.instruction_2()
		elif instruction == 3:
			self.instruction_3()
		elif instruction == 4:
			self.instruction_4()
		elif instruction == 5:
			self.instruction_5()
		elif instruction == 6:
			self.instruction_6()
		elif instruction == 7:
			self.instruction_7()
		elif instruction == 8:
			self.instruction_8()
		elif instruction == 9:
			self.instruction_9()
		elif instruction == 99:
			self.finished = True
		else:
			raise ValueError("Instruction value must match an existing instruction.")

	def instruction_1(self):
		pos1, pos2, pos3 = self.pos_params(3)
		self.intcode[pos3] = self.get_intcode_value(pos1) + self.get_intcode_value(pos2)
		self.pos += 4

	def instruction_2(self):
		pos1, pos2, pos3 = self.pos_params(3)
		self.intcode[pos3] = self.get_intcode_value(pos1) * self.get_intcode_value(pos2)
		self.pos += 4

	def instruction_3(self):
		if self.input_buffer:
			pos1, _, _ = self.pos_params(1)
			self.intcode[pos1] = self.input_buffer.pop(0)
			self.pos += 2
		else:
			self.waiting_for_input = True

	def instruction_4(self):
		pos1, _, _ = self.pos_params(1)
		self.output = self.get_intcode_value(pos1)
		self.sent_output = True
		#print(self.output)
		self.pos += 2

	def instruction_5(self):
		pos1, pos2, _ = self.pos_params(2)
		if self.get_intcode_value(pos1) != 0:
			self.pos = self.get_intcode_value(pos2)
		else:
			self.pos += 3

	def instruction_6(self):
		pos1, pos2, _ = self.pos_params(2)
		if self.get_intcode_value(pos1) == 0:
			self.pos = self.get_intcode_value(pos2)
		else:
			self.pos += 3

	def instruction_7(self):
		pos1, pos2, pos3 = self.pos_params(3)
		if self.get_intcode_value(pos1) < self.get_intcode_value(pos2) :
			self.intcode[pos3] = 1
		else:
			self.intcode[pos3] = 0
		self.pos += 4

	def instruction_8(self):
		pos1, pos2, pos3 = self.pos_params(3)
		if self.get_intcode_value(pos1) == self.get_intcode_value(pos2) :
			self.intcode[pos3] = 1
		else:
			self.intcode[pos3] = 0
		self.pos += 4

	def instruction_9(self):
		pos1, _, _ = self.pos_params(1)
		self.relative_base += self.get_intcode_value(pos1)
		self.pos += 2

	def pos_params(self, num_params):
		#print("PARAM VALS: ", self.mode, self.pos, self.relative_base)

		pos1 = self.pos + 1
		pos2 = self.pos + 2
		pos3 = self.pos + 3

		if self.mode[0] == "2":
			pos1 = self.relative_base + self.get_intcode_value(pos1)
		if self.mode[0] == "0":
			pos1 = self.get_intcode_value(pos1)
		if self.mode[1] == "2":
			pos2 = self.relative_base + self.get_intcode_value(pos2)
		if self.mode[1] == "0" and num_params > 1:
			pos2 = self.get_intcode_value(pos2)
		if self.mode[2] == "2":
			pos3 = self.relative_base + self.get_intcode_value(pos3)
		if self.mode[2] == "0" and num_params > 2:
			pos3 = self.get_intcode_value(pos3)
		
		return pos1, pos2, pos3

	def convert_to_dict(self, intcode):
		intcode_dict = {}
		for val in range(0, len(intcode)):
			intcode_dict[val] = intcode[val]

		return intcode_dict

	def get_intcode_value(self, pos):
		if pos < 0:
			raise ValueError("Position values should be >= 0")
		val = self.intcode.get(pos)
		if val is None:
			val = 0
			self.intcode[pos] = 0
		return val

	def set_memory_value(self, address, value):
		self.intcode[address] = value




