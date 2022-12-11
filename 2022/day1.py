f = open("input/01")

data = f.readlines()

top = []
curr = 0
for x in data:
	if x == "" or x == "\n":
		top.append(curr)
		curr = 0
	else:
		curr += int(x)

top.sort()
print(top[-1])
print(sum(top[len(top) - 3:len(top)]))