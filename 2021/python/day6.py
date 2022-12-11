INPUT_PATH = "../inputs/day_6_input.txt"

def total_fish(starting_fish, days):
	fish = starting_fish.copy()
	index = 0
	new_fish_buffer = [0] * 2
	for i in range(days):
		new_fish_buffer.append(fish[index])
		fish[index] += new_fish_buffer.pop(0)
		index = (index + 1) % 7

	return sum(fish) + sum(new_fish_buffer)

day6_input = open(INPUT_PATH)
data = day6_input.readline().split(',')

starting_fish = [0] * 7

for x in data:
	y = int(x)
	starting_fish[y] += 1

print(total_fish(starting_fish, 80))
print(total_fish(starting_fish, 256))