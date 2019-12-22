def spin(x):
	global programs
	newPrograms = [None] * len(programs)
	for y in range(len(programs)):
		newPrograms[(y + x) % len(programs)] = programs[y]
	programs = newPrograms

def exchange(x, y):
	global programs
	temp = programs[x]
	programs[x] = programs[y]
	programs[y] = temp

def partner(x, y):
	global programs
	indexX = 0
	indexY = 0
	for i in range(len(programs)):
		if programs[i] == x:
			indexX = i
		if programs[i] == y:
			indexY = i
	exchange(indexX, indexY)

def dance():
	global commands
	for x in commands:
		if x[0] == "s":
			spin(int(x[1:]))
		elif x[0] == "x":
			cmd = x[1:]
			exchange(int(cmd.split("/")[0]), int(cmd.split("/")[1]))
		elif x[0] == "p":
			partner(x[1], x[3])

f = open("AdventDay16", "r")

programs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
total = 0

inputs = f.read()

commands = inputs.split(",")

dance()

timesRun = 1

while programs != ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]:
	dance()
	timesRun += 1

print timesRun
for i in range(1000000000 % timesRun):
	dance()

for x in programs:
	print x
