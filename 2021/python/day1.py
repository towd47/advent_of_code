day1_input = open("../day_1_input.txt")
data = day1_input.readlines()

lines = [int(line) for line in data]

single_increases = 0
three_sum_increases = 0

for i in range(1, len(lines)):
	if lines[i] > lines[i-1]:
		single_increases += 1
	if i > 2:
		sum1 = sum(lines[i-4:i-1])
		sum2 = sum(lines[i-3:i])
		if sum2 > sum1:
			three_sum_increases += 1

print("Day 1 Part 1: ", single_increases)
print("Day 1 Part 2: ", three_sum_increases)