day1_input = open("../day_1_input.txt")
data = day1_input.readlines()

lines = [int(line) for line in data]

single_increases = 0
three_sum_increases = 0

last_sum = lines[0] + lines[1] + lines[2]
for i in range(1, len(lines)):
	if lines[i] > lines[i-1]:
		single_increases += 1
	if i > 2:
		new_sum = last_sum - lines[i-3] + lines[i]
		if new_sum > last_sum:
			three_sum_increases += 1
		last_sum = new_sum

print("Day 1 Part 1: ", single_increases)
print("Day 1 Part 2: ", three_sum_increases)