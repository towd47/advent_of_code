f = open("input/10")

data = f.readlines()

cyclenum = 0
regval = 1
strengthSum = 0
spritepos = [1, 2, 3]
crtstr = ""

for x in data:
	x = x.strip().split()
	cyclenum += 1
	if (cyclenum - 20) % 40 == 0:
		strengthSum += cyclenum * regval

	testnum = cyclenum % 40
	if testnum == 0:
		testnum = 40
	if testnum in spritepos:
		crtstr += "#"
	else:
		crtstr += "."

	if x[0] == "addx":
		cyclenum += 1
		if (cyclenum - 20) % 40 == 0:
			strengthSum += cyclenum * regval

		testnum = cyclenum % 40
		if testnum == 0:
			testnum = 40
		if testnum in spritepos:
			crtstr += "#"
		else:
			crtstr += "."

		regval += int(x[1])
		spritepos = [regval, regval + 1, regval + 2]
print(strengthSum)
crt = ""
for i in range(40, len(crtstr) + 1, 40):
	crt += crtstr[i - 40:i] + "\n"

print(crt)
