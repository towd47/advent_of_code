import readInput

def getRGBCounts(s):
	s = s.split(":")[1]
	a = s.split(";")

	b = 0
	r = 0
	g = 0

	for x in a:
		l = x.split(",")
		for y in l:
			y = y.strip()
			num, char = y.split(" ")
			num = int(num)
			char = char[0]

			if char == 'b' and num > b:
				b = num
			elif char == 'r' and num > r:
				r = num
			elif char == 'g' and num > g:
				g = num

	return (r, g, b)

def validForPart1(r, g, b):
	if r > 12 or g > 13 or b > 14:
		return False
	return True

tot = 0
tot2 = 0
for line in readInput.yieldLines("2"):
	r, g, b = getRGBCounts(line)
	if validForPart1(r, g, b):
		l = line.split(":")[0]
		n = int("".join([x for x in l if x.isdigit()]))
		tot += n
	tot2 += r * g * b

print(tot)
print(tot2)