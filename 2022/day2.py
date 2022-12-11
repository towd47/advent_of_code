f = open("input/02")

data = f.readlines()

valmap = dict()
valmap["A"] = 1
valmap["B"] = 2
valmap["C"] = 3
valmap["X"] = 1
valmap["Y"] = 2
valmap["Z"] = 3

scoremap = dict()
scoremap[-1] = 6
scoremap[2] = 6
scoremap[-2] = 0
scoremap[1] = 0
scoremap[0] = 3 

total = 0
for x in data:
	throws = x.strip().split()
	a = valmap[throws[0]]
	b = valmap[throws[1]]

	total += scoremap[a - b]
	total += b

print(total)

total = 0
for x in data:
	throws = x.strip().split()
	a = valmap[throws[0]]
	if throws[1] == 'X':
		throwval = a - 1
		scoreval = 0
	elif throws[1] == 'Y':
		throwval = a
		scoreval = 3
	else:
		throwval = a + 1
		scoreval = 6

	if throwval == 0:
		throwval = 3
	if throwval == 4:
		throwval = 1

	total += throwval + scoreval

print(total)