day2_input = open("../day_2_input.txt")
data = day2_input.readlines()

horiz = 0
depth = 0
aim = 0
depth2 = 0

for line in data:
	[direction, value] = line.split()
	if direction == "forward":
		horiz += int(value)
		depth2 += aim * int(value)
	elif direction == "up":
		depth -= int(value)
		aim -= int(value)
	else:
		depth += int(value)
		aim += int(value)

print("Day 2 part 1: ", horiz * depth)
print("Day 2 part 2: ", horiz * depth2)