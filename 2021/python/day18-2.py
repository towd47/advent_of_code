# python3 day18-2.py < ../inputs/day_18_input.txt

import sys

class Snail:
	def __init__(self, snail_str):
		self.arr = self.str_to_arr(snail_str)

	def str_to_arr(self, snail_str):
		arr = []
		num = ''
		for i in range(len(snail_str)):
			if snail_str[i] == ',':
				continue
			elif snail_str[i] == '[' or snail_str[i] == ']':
				arr.append(snail_str[i])
			else:
				arr.append(int(snail_str[i]))

		return arr

	def simplify(self):
		changed = True
		while changed:
			depth = 0
			changed = False
			for i in range(len(self.arr)):
				if self.arr[i] == '[':
					if depth == 4:
						self.explode(i)
						changed = True
						break
					depth += 1
				elif self.arr[i] == ']':
					depth -= 1

			if not changed:
				for i in range(len(self.arr)):
					if isinstance(self.arr[i], int) and self.arr[i] > 9:
						self.split(i)
						changed = True
						break

	def explode(self, pos):
		left = self.arr[pos + 1]
		right = self.arr[pos + 2]
		for i in range(pos - 1, 0, -1):
			if self.arr[i] != '[' and self.arr[i] != ']':
				self.arr[i] += left
				break
		for i in range(pos + 4, len(self.arr)):
			if self.arr[i] != '[' and self.arr[i] != ']':
				self.arr[i] += right
				break
		new_arr = self.arr[:pos]
		new_arr.append(0)
		new_arr.extend(self.arr[pos+4:])
		self.arr = new_arr

	def split(self, pos):
		val = self.arr[pos]
		left = int(val / 2)
		right = int(round(val/2 + .1))
		self.arr = self.arr[:pos] + ['[', left, right, ']'] + self.arr[pos+1:]

	def add(self, snail_str):
		self.arr = ['['] + self.arr + self.str_to_arr(snail_str) + [']']

	def magnitude(self):
		while len(self.arr) > 1:
			for i in range(len(self.arr) - 3):
				if self.arr[i] == '[' and isinstance(self.arr[i+1], int) and isinstance(self.arr[i+2], int) and self.arr[i+3] == ']':
					self.arr = self.arr[0:i] + [self.arr[i+1] * 3 + self.arr[i+2] * 2] + self.arr[i+4:]
					break
		return self.arr[0]

	def __str__(self):
		str_rep = ''
		for x in self.arr:
			if isinstance(x, int):
				str_rep += str(x) + ','
			else:
				str_rep += x
		return str_rep

lines = sys.stdin.readlines()
snail = None

for line in lines:
	line = line.strip()
	if snail:
		snail.add(line)
		snail.simplify()
	else:
		snail = Snail(line)

print(snail.magnitude())

largest = 0
for i in range(len(lines) - 1):
	for j in range(i+1, len(lines)):
		line1 = lines[i].strip()
		line2 = lines[j].strip()
		snail = Snail(line1)
		snail2 = Snail(line2)
		snail.add(line2)
		snail.simplify()
		largest = max(largest, snail.magnitude())

		snail2.add(line1)
		snail2.simplify()
		largest = max(largest, snail2.magnitude())

print(largest)
