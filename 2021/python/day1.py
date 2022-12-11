INPUT_PATH = "../inputs/day_1_input.txt"

day1_input = open(INPUT_PATH)
data = day1_input.readlines()

depths = [int(line) for line in data]

single_increases = 0
three_sum_increases = 0

for i in range(1, len(depths)):
	if depths[i] > depths[i-1]:
		single_increases += 1
	if i > 2:
		sum1 = sum(depths[i-4:i-1])
		sum2 = sum(depths[i-3:i])
		if sum2 > sum1:
			three_sum_increases += 1

print("Day 1 Part 1: ", single_increases)
print("Day 1 Part 2: ", three_sum_increases)