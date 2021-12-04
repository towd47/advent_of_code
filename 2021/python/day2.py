day2_input = open("../day_2_input.txt")
data = day2_input.readlines()

horiz = 0
depth = 0
aim = 0

for line in data:
	[direction, value] = line.split()
	if direction == "forward":
		horiz += int(value)
		depth += aim * int(value)
	elif direction == "up":
		aim -= int(value)
	else:
		aim += int(value)

print("Day 2 part 1: ", horiz * aim)
print("Day 2 part 2: ", horiz * depth)