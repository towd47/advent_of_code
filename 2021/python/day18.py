def adjust_form(snail_num):
	nums = []
	depths = []
	num = []
	depth = 0
	for i in range(len(snail_num)):
		cur_depth = depth
		char = snail_num[i]
		if char == '[':
			if num:
				num.append('x')
			depth += 1
			
		elif char == ']':
			depth -= 1
		elif char != ',':
			if snail_num[i - 1] == ',' and snail_num[i - 2] == ']':
				num.append('z')
			non_nums = ['[', ']', ',']
			if snail_num[i-1] in non_nums:
				while snail_num[i + 1] not in non_nums:
					char = char + snail_num[i+1]
					i += 1
				num.append(int(char))
		if len(num) == 2:
			nums.append(num)
			num = []
			depths.append(cur_depth)
	return nums, depths


def reduce(snail_num, depths):
	changed = True
	# step = 0
	while changed:
		# print("STEP", step)
		# print(snail_num)
		# print(depths)
		# step += 1
		# print()
		changed = False
		for i in range(len(depths)):
			# EXPLODE
			if depths[i] == 5:
				should_pop = True
				if i == 0:
					if snail_num[i+1][0] == 'z':
						snail_num[i+1][0] = 0
						snail_num[i+1][1] = snail_num[i+1][1] + snail_num[i][1]
					else:
						snail_num[i+1][0] = snail_num[i+1][0] + snail_num[i][1]
						snail_num[i][0] = 0
						snail_num[i][1] = 'x'
						depths[i] = depths[i] - 1
						should_pop = False
				elif i == len(depths) - 1:
					if snail_num[i-1][1] == 'x':
						snail_num[i-1][1] = 0
						snail_num[i-1][0] = snail_num[i-1][0] + snail_num[i][0]
					else:
						snail_num[i-1][1] = snail_num[i-1][1] + snail_num[i][0]
				elif depths[i-1] == 4 and snail_num[i-1][1] == 'x':
					snail_num[i-1][0] = snail_num[i-1][0] + snail_num[i][0]
					snail_num[i-1][1] = 0
					if snail_num[i+1][0] != 'z':
						snail_num[i+1][0] = snail_num[i+1][0] + snail_num[i][1]
					else:
						snail_num[i+1][1] = snail_num[i+1][1] + snail_num[i][1]
				elif depths[i+1] == 4 and snail_num[i+1][0] == 'z':
					snail_num[i+1][1] = snail_num[i+1][1] + snail_num[i][1]
					snail_num[i+1][0] = 0
					if snail_num[i-1][1] != 'x':
						snail_num[i-1][1] = snail_num[i-1][1] + snail_num[i][0]
					else:
						snail_num[i-1][0] = snail_num[i-1][0] + snail_num[i][0]
				else:
					if snail_num[i+1][0] != 'z':
						snail_num[i+1][0] = snail_num[i+1][0] + snail_num[i][1]
					else:
						snail_num[i+1][1] = snail_num[i+1][1] + snail_num[i][1]
					if snail_num[i-1][1] != 'x':
						snail_num[i-1][1] = snail_num[i-1][1] + snail_num[i][0]
					else:
						snail_num[i-1][0] = snail_num[i-1][0] + snail_num[i][0]
					snail_num[i][1] = 'x'
					snail_num[i][0] = 0
					depths[i] -= 1
					should_pop = False
				
				if should_pop:
					snail_num.pop(i)
					depths.pop(i)
				changed = True
				break

		if changed:
			continue
		#SPLIT
		for i in range(len(snail_num)):
			x, y = snail_num[i]
			if x != 'z' and x > 9:
				snail_num[i][0] = 'z'
				new_num = [int(x/2), int(round(x/2 + .3))] # ROUND(6.5) ROUNDS TO 6?? BUT OTHER NUMBERS WORK NORMALLY??
				snail_num.insert(i, new_num)
				depths.insert(i, depths[i] + 1)
				changed = True
				if snail_num[i+1][1] == 'x':
					snail_num.pop(i+1)
					depths.pop(i+1)
				break
			elif y != 'x' and y > 9:
				snail_num[i][1] = 'x'
				new_num = [int(y/2), int(round(y/2 + .3))]
				snail_num.insert(i+1, new_num)
				depths.insert(i+1, depths[i] + 1)
				changed = True
				if snail_num[i][0] == 'z':
					snail_num.pop(i)
					depths.pop(i)
				break
	return snail_num, depths
	
def total_magnitude(snail_num, depths):
	pos = 0
	while len(snail_num) > 1:
		# print(pos)
		# print(snail_num)
		# print(depths)
		# print()
		if snail_num[pos][0] != 'z' and snail_num[pos][1] != 'x':
			if pos > 0 and snail_num[pos - 1][1] == 'x' and depths[pos - 1] == depths[pos] - 1:
				snail_num[pos - 1][1] = magnitude(snail_num[pos])
				snail_num.pop(pos)
				depths.pop(pos)
				pos = pos - 1
			elif pos < len(snail_num) - 1 and snail_num[pos + 1][0] == 'z'and depths[pos + 1] == depths[pos] - 1:
				snail_num[pos + 1][0] = magnitude(snail_num[pos])
				snail_num.pop(pos)
				depths.pop(pos)
			else:
				snail_num[pos][0] = magnitude(snail_num[pos])
				snail_num[pos][1] = 'x'
				depths[pos] -= 1
				pos += 1
		else:
			pos += 1

	return magnitude(snail_num[0])


def magnitude(num):
	return num[0] * 3 + num[1] * 2

day18_input = open("../day_18_input.txt")
data = day18_input.readlines()
added_nums = []
added_depths = []
# step = 1
for line in data:
	line = line.strip()
	nums, depths = adjust_form(line)
	nums, depths = reduce(nums, depths)
	if added_nums:
		added_nums.extend(nums)
		added_depths.extend(depths)
		added_depths = [x+1 for x in added_depths]
		added_nums, added_depths = reduce(added_nums, added_depths)
	else:
		added_nums = nums
		added_depths = depths
	# print(added_nums)
	# print(added_depths)
	# print('step', step)
	# print()
	# step += 1

print(added_nums)
print(added_depths)

print(total_magnitude(added_nums, added_depths))





# TESTING

# a = '[[[[3,0],[5,3]],[4,4]],[5,5]]'
# nums, depths = adjust_form(a)
# print(total_magnitude(nums, depths))

# a = '[[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]'
# nums, depths = adjust_form(a)
# print('ADJUSTED')
# print(nums)
# print(depths)

# nums, depths = reduce(nums, depths)
# print('REDUCED')
# print(nums)
# print(depths)