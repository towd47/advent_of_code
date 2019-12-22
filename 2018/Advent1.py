def advent1_1():

	frequency = 0

	f = open("advent1.txt", "r")

	lines = f.readlines()

	min = 0

	for x in lines:
		frequency = frequency + int(x)
		if frequency < min:
			min = frequency

	print(min)
	return frequency

def advent1_2():
	frequency = 0
	foundFreqs = [0]

	f = open("advent1.txt", "r")
	lines = f.readlines()

	itteration = 1;
	while True:
		for x in lines:
			frequency += int(x)
			if alreadyFound(frequency, foundFreqs):
				print("found")
				return frequency
			if itteration == 1:
				foundFreqs.append(frequency)

		itteration += 1
		print(frequency)


def alreadyFound(val, list):
	for item in list:
		if item == val:
			return True
	return False

def main():
	print(advent1_2())

main()

