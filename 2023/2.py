import readInput

def getMaxRGB(s):
	games = s.split(";")

	rmax = 0
	gmax = 0
	bmax = 0

	for game in games:
		colors = game.split(",")
		for color in colors:
			color = color.strip()
			num, char = color.split()
			num = int(num)
			char = char[0]

			if char == 'b' and num > bmax:
				bmax = num
			elif char == 'r' and num > rmax:
				rmax = num
			elif char == 'g' and num > gmax:
				gmax = num

	return (rmax, gmax, bmax)

def validForPart1(r, g, b):
	if r > 12 or g > 13 or b > 14:
		return False
	return True

def day2():
	tot = 0
	tot2 = 0
	for line in readInput.yieldLines("2"):
		lineNum, rgbs = line.split(":")
		r, g, b = getMaxRGB(rgbs)
		if validForPart1(r, g, b):
			n = int("".join([x for x in lineNum if x.isdigit()]))
			tot += n
		tot2 += r * g * b

	print(f'Part 1: {tot}')
	print(f'Part 2: {tot2}')

if __name__ == "__main__":
	day2()