from math import gcd

def advent_12a(steps):
	f = open("12.txt", "r")
	lines = f.readlines()

	moons = []
	for line in lines:
		positions = line.split()
		pos = []
		for val in positions:
			chars = "<x=, yz>"
			val = val.strip(chars)
			pos.append(int(val))
		moons.append(Moon(pos))

	for _ in range(0, steps):
		apply_gravity(moons)
		for moon in moons:
			moon.step()

	total_energy = 0
	for moon in moons:
		total_energy += moon.total_energy()

	return total_energy

def advent_12C():
	lines = read_file()
	x, y, z = lines_to_pos(lines)
	x_vel = [0, 0, 0, 0]
	y_vel = [0, 0, 0, 0]
	z_vel = [0, 0, 0, 0]
	x_period = steps_till_repeat(x, x_vel)
	y_period = steps_till_repeat(y, y_vel)
	z_period = steps_till_repeat(z, z_vel)

	print(lcm([x_period, y_period, z_period]))


def lcm(vals):
	lcm = vals[0]
	for i in vals[1:]:
		lcm = int(lcm * i / gcd(lcm, i))

	return lcm



def steps_till_repeat(pos, vel):
	pos_update = pos.copy()
	vel_update = vel.copy()

	steps = 1
	step(pos_update, vel_update)

	while pos_update != pos or vel_update != vel:
		steps += 1
		step(pos_update, vel_update)

	return steps

def step(pos, vel):
	for i in range(0, len(pos)):
		pos_copy = pos.copy()
		pos_copy.pop(i)
		for j in pos_copy:
			if j > pos[i]:
				vel[i] += 1
			elif j < pos[i]:
				vel[i] -= 1

	for i in range(0, len(pos)):
		pos[i] += vel[i]



def lines_to_pos(lines):
	x = []
	y = []
	z = []
	for line in lines:
		positions = line.split()
		pos = []
		for val in positions:
			chars = "<x=, yz>"
			val = val.strip(chars)
			pos.append(int(val))

		x.append(pos[0])
		y.append(pos[1])
		z.append(pos[2])
	return x, y, z

def read_file():
	f = open("12.txt", "r")
	lines = f.readlines()
	return lines

def advent_12b():
	f = open("12.txt", "r")
	lines = f.readlines()

	moons = []
	moons_base = []
	for line in lines:
		positions = line.split()
		pos = []
		for val in positions:
			chars = "<x=, yz>"
			val = val.strip(chars)
			pos.append(int(val))
		moons.append(Moon(pos))
		moons_base.append(Moon(pos))

	steps = 1
	steps_all = [0, 0, 0]

	apply_gravity(moons)
	for moon in moons:
		moon.step()

	while prod(steps_all) == 0:
		for i in range(0, 3):
			if steps_all[i] == 0:
				match = True
				for j in range(0, len(moons)):
					if moons[j].pos[i] != moons_base[j].pos[i] or moons[j].vel[i] != moons_base[j].vel[i]:
						match = False
				if match:
					steps_all[i] = steps
					

		apply_gravity(moons)
		for moon in moons:
			moon.step()
		steps += 1

	print(steps_all)
	lcm = steps_all[0]
	for i in steps_all[1:]:
		lcm = int(lcm * i / gcd(lcm, i))

	print(lcm)

def prod(list):
	result = 1
	for x in list:
		result = result * x

	return result



def apply_gravity(moons):
	for i in range(0, len(moons) - 1):
		for j in range(i + 1, len(moons)):
			moon1 = moons[i]
			moon2 = moons[j]
			for k in range(0, len(moon1.pos)):
				if moon1.pos[k] > moon2.pos[k]:
					moon1.add_change(k, -1)
					moon2.add_change(k, 1)
				elif moon1.pos[k] < moon2.pos[k]:
					moon1.add_change(k, 1)
					moon2.add_change(k, -1)


class Moon:
	def __init__(self, pos):
		self.pos = pos
		self.vel = [0, 0, 0]
		self.change = [0, 0, 0]

	def __repr__(self):
		return repr(self.pos)

	def potential_energy(self):
		return sum(abs(pos) for pos in self.pos)
	def kinetic_energy(self):
		return sum(abs(vel) for vel in self.vel)

	def total_energy(self):
		return self.potential_energy() * self.kinetic_energy()

	def update_pos(self):
		for i in range(0, len(self.pos)):
			self.pos[i] += self.vel[i]

	def update_vel(self):
		for i in range(0, len(self.vel)):
			self.vel[i] += self.change[i]

	def step(self):
		self.update_vel()
		self.update_pos()
		self.change = [0, 0, 0]

	def add_change(self, pos_to_change, change):
		self.change[pos_to_change] += change

#print("12a ", advent_12a(1000))
#advent_12b()
advent_12C()






