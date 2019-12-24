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
	steps_all = [0, 0, 0, 0]

	apply_gravity(moons)
	for moon in moons:
		moon.step()

	while prod(steps_all) == 0:
		for i in range(0, len(moons)):
			if steps_all[i] == 0 and moons[i].vel == moons_base[i].vel:
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
advent_12b()







