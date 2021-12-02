def advent_16a():
	input_str = setup()

	base_pattern = [0, 1, 0, -1]

	for i in range(100):
		input_str = phase(input_str, base_pattern)

	print(input_str[:8])
		
#67481260


def phase(input_str, base_pattern):
	new_str = ''
	pattern_repeats = 1
	pattern_pos = 0
	while len(new_str) < len(input_str):
		total_sum = 0
		repitions = 0
		for val in input_str:
			repitions += 1
			if repitions == pattern_repeats:
				repitions = 0
				pattern_pos += 1
				if pattern_pos == len(base_pattern):
					pattern_pos = 0

			total_sum += int(val) * base_pattern[pattern_pos]
		pattern_repeats += 1
		pattern_pos = 0
		
		new_str += str(int(abs(total_sum)%10))
	return new_str


def setup():
	f = open("16.txt", 'r')
	line = f.readline()
	return line


advent_16a()