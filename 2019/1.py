import math

def advent_1a():

	f = open("1.txt", "r")
	lines = f.readlines()

	total_fuel = 0
	for line in lines:
		total_fuel = total_fuel + find_fuel(int(line))

	return total_fuel


def find_fuel(mass):
	return math.floor(mass / 3) - 2

def advent_1b():
	total_fuel = 0

	f = open("1.txt", "r")
	lines = f.readlines()

	for line in lines:
		module_fuel = 0
		remaining_fuel_to_fuel = find_fuel(int(line))

		while remaining_fuel_to_fuel > 0 :
			module_fuel += remaining_fuel_to_fuel
			remaining_fuel_to_fuel = find_fuel(remaining_fuel_to_fuel)

		total_fuel += module_fuel
		
	return total_fuel


print(advent_1a())
print(advent_1b())