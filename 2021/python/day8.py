def decode(digits):
	key_map = [""] * 10
	left_to_decode = []
	for e in digits:
		e = ''.join(sorted(e))
		if len(e) == 2:
			key_map[1] = e
		elif len(e) == 3:
			key_map[7] = e
		elif len(e) == 4:
			key_map[4] = e
		elif len(e) == 7:
			key_map[8] = e
		else:
			left_to_decode.append(e)

	still_left_to_decode = []
	for e in left_to_decode:
		if len(e) == 6 and set(key_map[4]).issubset(set(e)):
			key_map[9] = e
		elif len(e) == 5 and set(key_map[1]).issubset(set(e)):
			key_map[3] = e
		else:
			still_left_to_decode.append(e)

	for e in still_left_to_decode:
		if len(e) == 6:
	 		if set(key_map[1]).issubset(set(e)):
	 			key_map[0] = e
	 		else:
	 			key_map[6] = e
		elif len(e) == 5:
	 		overlap = ''.join(set(key_map[4]).intersection(e))
	 		if len(overlap) == 3:
	 			key_map[5] = e
	 		else:
	 			key_map[2] = e

	return key_map

day8_input = open("../day_8_input.txt")
data = day8_input.readlines()

vals = [2, 3, 4, 7]

unique_count = 0
total = 0
totalsum = 0

for line in data:
	nums = [""] * 10
	[inp, outp] = line.split('|')

	in_digits = inp.split()
	digit_map = decode(in_digits)

	out_digits = outp.split()
	num = ""
	for e in out_digits:
		e = ''.join(sorted(e))
		if len(e) in vals:
			unique_count += 1
		for i in range(len(digit_map)):
			if e == digit_map[i]:
				num = num + str(i)
				break
	totalsum = totalsum + int(num)


print(unique_count)
print(totalsum)



# Uniques:
			# 1 - 2
			# 4 - 4
			# 7 - 3
			# 8 - 7

# 1 - 2 letters
# 7 - 3 letters
# top line - difference between 1 and 7
# numbers containing 7: 0 3 9
# numbers containing 4: 9
# 0 contains 1
# 6 does not contain 1
# 3 contains 1 
# 2 and 5 do not contain 1
# 5 has 3 overlaps with 4
# 2 has 2 overlaps with 4
# lengths:
			# 0 - 6
			# 2 - 5
			# 3 - 5
			# 5 - 5
			# 6 - 6
			# 9 - 6

