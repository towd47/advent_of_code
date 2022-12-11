# python3 day24.py < ../inputs/day_24_input.txt

import sys
import copy

class ALU:
	
	def __init__(self, num, instructions):
		self.inputs = list(str(num))
		self.instructions = instructions
		self.variables = {'w':0, 'x':0, 'y':0, 'z':0}

	def run(self):
		while self.instructions:
			inst = self.instructions.pop(0)
			if inst.cmd == 'inp':
				self.inp(inst)
			elif inst.cmd == 'add':
				self.add(inst)
			elif inst.cmd == 'mul':
				self.mul(inst)
			elif inst.cmd == 'div':
				self.div(inst)
			elif inst.cmd == 'mod':
				self.mod(inst)
			elif inst.cmd == 'eql':
				self.eql(inst)

	def inp(self, inst):
		val = int(self.inputs.pop(0))
		self.variables[inst.var1] = val
		# print(self.variables)
		# print(val)

	def add(self, inst):
		if inst.var2 in self.variables:
			self.variables[inst.var1] = self.variables[inst.var1] + self.variables[inst.var2]
		else:
			self.variables[inst.var1] = self.variables[inst.var1] + int(inst.var2)

	def mul(self, inst):
		if inst.var2 in self.variables:
			self.variables[inst.var1] = self.variables[inst.var1] * self.variables[inst.var2]
		else:
			self.variables[inst.var1] = self.variables[inst.var1] * int(inst.var2)

	def div(self, inst):
		if inst.var2 in self.variables:
			self.variables[inst.var1] = int(self.variables[inst.var1] / self.variables[inst.var2])
		else:
			self.variables[inst.var1] = int(self.variables[inst.var1] / int(inst.var2))

	def mod(self, inst):
		if inst.var2 in self.variables:
			self.variables[inst.var1] = self.variables[inst.var1] % self.variables[inst.var2]
		else:
			self.variables[inst.var1] = self.variables[inst.var1] % int(inst.var2)

	def eql(self, inst):
		val = 0
		if inst.var2 in self.variables:
			b = self.variables[inst.var2]
		else:
			b = int(inst.var2)
		if self.variables[inst.var1] == b:
			val = 1
		self.variables[inst.var1] = val

	def result(self):
		return self.variables['z']

class Instruction:
	cmd = ''
	var1 = ''
	var2 = ''

	def __str__(self):
		return self.cmd + ' ' + str(self.var1) + ' ' + str(self.var2)

instructions = []
lines = sys.stdin.readlines()
for line in lines:
	line = line.strip().split()
	inst = Instruction()
	inst.cmd = line[0]
	inst.var1 = line[1]
	if len(line) > 2:
		inst.var2 = line[2]
	instructions.append(inst)

num = 11911911716111

# last2 = ['16', '27', '38', '49']
# last22 = ['17', '28', '39']
# NUM CAN BE BROKEN INTO SECTIONS : XX, 9119, X, YZ where Y in last22 and Z in last2, WWW
# CAN BRUTE FORCE TEST FOR LOWEST MAGNITUDE WITH : XXX and WWW seperately using highest or lowest combinations of YZ

# w1 and 2 no restrictions yet, lower vals = lower num on same mag
# w3 and w4 must be 9 and 1
# w5 and 6 must be 1 and 9
# w7 no affect on its own
# w8 must be 6 less than w9
# w10 must be 5 less than w11
# w12 = 6 does something

# num must shrink at 4, 6, 9, 11, 12, 13, 14

# find combos of 1, 2, 5, 6 that lower num

# -> 405

# num = 99911993949684 LARGEST
# num = 62911941716111 LOWEST

# 7 z / 26 
# 
# 14 z * y

# first y is 26
# second y is 26
# third y is 26
# z = num * 26 + last input + val
# z after 1 input % 26 = -1 impossible
# z after 2 inputs % 26 = -4
# z after 3 inputs % 26 = 11     	z = ((((w1 + 6) * 26) + w2 + 6) * 26 + w3 + 3), true if w3 + 3 - 11 = w4
# z after 4 inputs % 26 = -4		z = ((((w1 + 6) * 26) + w2 + 6) * 26 + w3 + 3) / 26 
# z after 5 inputs % 26 = 1 		z = (z / 26 + w5 + 9 % 26 = w6 - 1,   z after 5 inps, ((((w1 + 6) * 26) + w2 + 6) * 26 + w3 + 3) / 26 + w5 + 9) = w6 - 1
# z after 6 inputs % 26 = -1
# z after 7 inputs % 26 = -2
# z after 8 inputs % 26 = 0         w8 + 6 = w9
# z after 9 inputs % 26 = -1
# z after 10 inputs % 26 = 5 		w10 + 10 - 5 = w11
# z after 11 inputs % 26 = 16 		w11 + 12 = w12 + 16
# z after 12 inputs % 26 = 7 		w
# z after 13 inputs % 26 = 11
# z after 14 inputs  = z / 26 % 26


alu = ALU(num, copy.deepcopy(instructions))
alu.run()
print(alu.result())
# compare_val = alu.result()

# num_to_comp = '1191191'
a = '9119'
b = '1716111'
lower = []

for i in range(111, 1000):
	print(i)
	x = str(i)
	if '0' in x:
		continue
	y = x[:2] + a + x[2] + b
# 	y = x[:2] + '91' + x[2:] + num_to_comp
	alu = ALU(int(y), copy.deepcopy(instructions))
	alu.run()
	lower.append((alu.result(), y))

# last2 = ['16', '27', '38', '49']
# last22 = ['17', '28', '39']
# # for l in range(1, 10):
# for j in last2:
# 	for k in last22:
# 		for i in range(111, 1000):
# 			print(i)
# 			x = str(i)
# 			if '0' in x:
# 				continue
# 			y = num_to_comp + k + j + str(i)
# 		# 	y = x[:2] + '91' + x[2:] + num_to_comp
# 			alu = ALU(int(y), copy.deepcopy(instructions))
# 			alu.run()
# 			lower.append((alu.result(), k, j, i))

print(sorted(lower))
