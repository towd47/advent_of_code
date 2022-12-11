f = open("input/05")

data = f.readlines()

drawing = []
instructions = []

foundDivide = False
for x in data:
	x = x.strip("\n")
	if foundDivide:
		instructions.append(x)
	elif x == "":
		foundDivide = True
	else:
		drawing.append(x)

last = drawing.pop()
num = int(last.strip().split().pop())

cols = [[] for _ in range(num)]

for x in drawing:
	for i in range(num):
		pos = i * 4 + 1
		if x[pos] != " ":
			cols[i].insert(0, x[pos])

for x in instructions:
	inst = x.split()
	numToMove = int(inst[1])
	colfrom = int(inst[3]) - 1
	colto = int(inst[5]) - 1

	for _ in range(numToMove):
		cols[colto].append(cols[colfrom].pop())

ans = ""

for x in cols:
	ans = ans + x[-1]

print(ans)

cols = [[] for _ in range(num)]

for x in drawing:
	for i in range(num):
		pos = i * 4 + 1
		if x[pos] != " ":
			cols[i].insert(0, x[pos])

for x in instructions:
	inst = x.split()
	numToMove = int(inst[1])
	colfrom = int(inst[3]) - 1
	colto = int(inst[5]) - 1

	cols[colto].extend(cols[colfrom][len(cols[colfrom]) - numToMove:len(cols[colfrom])])
	cols[colfrom] = cols[colfrom][:len(cols[colfrom]) - numToMove]

ans = ""

for x in cols:
	ans = ans + x[-1]

print(ans)


