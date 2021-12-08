import statistics

day7_input = open("../day_7_input.txt")
data = day7_input.readline()

locations = []
for e in data.split(','):
	locations.append(int(e))

med = int(statistics.median(locations))

gas = 0
for e in locations:
	gas = gas + abs(e - med)

print(gas)

avg = round(sum(locations) / len(locations))

gas = 0
gas1 = 0
gas2 = 0
dist = 0
for e in locations:
	dist = abs(e - avg + 1)
	gas = gas + int((dist * (dist + 1))/2)

print(gas)