def advent_4a():

	count = 0
	for i in range(108457, 562041):
		if increasing_digits_only(i) and contains_adjacent_duplicate(i):
			count += 1

	return count

def advent_4b():
	count = 0
	for i in range(108457, 562041):
		if increasing_digits_only(i) and contains_exactly_two_in_a_row(i):
			count += 1

	return count


def increasing_digits_only(num):
	num_as_array = [int(i) for i in str(num)]
	for i in range(0, len(num_as_array) - 1):
		if num_as_array[i+1] < num_as_array[i]:
			return False
	return True

def contains_adjacent_duplicate(num):
	num_as_array = [int(i) for i in str(num)]
	for i in range(0, len(num_as_array) - 1):
		if num_as_array[i+1] == num_as_array[i]:
			return True
	return False

def contains_exactly_two_in_a_row(num):
	num_as_array = [int(i) for i in str(num)]
	pos = 1
	last_num = num_as_array[0]
	count = 1
	while pos < len(num_as_array):
		if num_as_array[pos] == last_num:
			count += 1
		if pos == len(num_as_array) - 1 or num_as_array[pos] != last_num :
			if count == 2:
				return True
			else:
				count = 1
				last_num = num_as_array[pos]
		pos += 1
	return False

print("4a: ", advent_4a())
print("4b: ", advent_4b())