class Intcode_computer:

	def __init__(self, intcode):
		self.intcode = intcode.copy()
		self.input_buffer = list()
		self.output = 0
		self.waiting_for_input = False
		self.finished = False
		self.pos = 0
		self.mode = ""

	def input(self, value):
		self.input_buffer.append(value)
		self.waiting_for_input = False

	def run(self):
		while not self.finished and not self.waiting_for_input:
			self.step()

	def step(self):
		instruction = self.intcode[self.pos] % 100
		self.mode = str(int(self.intcode[self.pos] / 100))[::-1]

		while len(self.mode) < 3:
			self.mode = self.mode + "0"

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
		elif instruction == 99:
			self.finished = True

	def instruction_1(self):
		pos1, pos2, pos3 = self.pos_params(3)
		self.intcode[pos3] = self.intcode[pos1] + self.intcode[pos2]
		self.pos += 4

	def instruction_2(self):
		pos1, pos2, pos3 = self.pos_params(3)
		self.intcode[pos3] = self.intcode[pos1] * self.intcode[pos2]
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
		self.output = self.intcode[pos1]
		self.pos += 2

	def instruction_5(self):
		pos1, pos2, _ = self.pos_params(2)
		if self.intcode[pos1] != 0:
			self.pos = self.intcode[pos2]
		else:
			self.pos += 3

	def instruction_6(self):
		pos1, pos2, _ = self.pos_params(2)
		if self.intcode[pos1] == 0:
			self.pos = self.intcode[pos2]
		else:
			self.pos += 3

	def instruction_7(self):
		pos1, pos2, pos3 = self.pos_params(3)
		if self.intcode[pos1] < self.intcode[pos2] :
			self.intcode[pos3] = 1
		else:
			self.intcode[pos3] = 0
		self.pos += 4

	def instruction_8(self):
		pos1, pos2, pos3 = self.pos_params(3)
		if self.intcode[pos1] == self.intcode[pos2] :
			self.intcode[pos3] = 1
		else:
			self.intcode[pos3] = 0
		self.pos += 4

	def pos_params(self, num_params):

		pos1 = self.pos + 1
		pos2 = self.pos + 2
		pos3 = self.pos + 3

		if self.mode[0] == "0":
			pos1 = self.intcode[pos1]
		if self.mode[1] == "0" and num_params > 1:
			pos2 = self.intcode[pos2]
		if self.mode[2] == "0" and num_params > 2:
			pos3 = self.intcode[pos3]

		return pos1, pos2, pos3