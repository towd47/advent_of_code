from enum import IntEnum
import functools

class Order(IntEnum):
	UNORDERED = 1
	UNKNOWN = 0
	ORDERED = -1

def toList(lstring):
	lstring = lstring[1:len(lstring)-1]
	li = []
	pos = 0
	while pos < len(lstring):
		if lstring[pos] == '[':
			depth = 1
			startpos = pos
			while lstring[pos] != ']' or depth != 0:
				pos += 1
				if lstring[pos] == '[':
					depth += 1
				elif lstring[pos] == ']':
					depth -= 1
			li.append(toList(lstring[startpos:pos+1]))
		elif lstring[pos] != ',':
			num = ""
			num = num + lstring[pos]
			while pos + 1 < len(lstring) and lstring[pos + 1] != ',':
				pos += 1
				num = num + lstring[pos]
			li.append(int(num))
		pos += 1

	return li

def isOrdered(l1, l2):
	pos = 0

	status = Order.UNKNOWN
	end = False

	while status == Order.UNKNOWN and not end:
		if pos >= len(l1):
			if pos >= len(l2):
				status = Order.UNKNOWN
				end = True
			else:
				status = Order.ORDERED
		elif pos >= len(l2):
			status = Order.UNORDERED
		else:
			if type(l1[pos]) is list:
				if type(l2[pos]) is list:
					status = isOrdered(l1[pos], l2[pos])
				else:
					status = isOrdered(l1[pos], [l2[pos]])
			elif type(l2[pos]) is list:
				status = isOrdered([l1[pos]], l2[pos]) # status can come back unknown if the two lists are the same
			elif l1[pos] < l2[pos]:
				status = Order.ORDERED
			elif l1[pos] > l2[pos]:
				status = Order.UNORDERED
			# Status does not change if l1[pos] == l2[pos]
		pos += 1
	return status

def p1(data):
	pairs = []

	for i in range(0, len(data), 3):
		l1 = toList(data[i].strip())
		l2 = toList(data[i+1].strip())

		pairs.append((l1, l2))

	pairIndexSum = 0
	for i in range(len(pairs)):
		status = isOrdered(pairs[i][0], pairs[i][1])
		if status == Order.ORDERED:
			pairIndexSum += i + 1

	print(pairIndexSum)

def p2(data):
	i = 0
	while i < len(data):
		data[i] = data[i].strip()
		if data[i] == "":
			data.pop(i)
		else:
			data[i] = toList(data[i])
			i += 1

	data.append(toList("[[2]]"))
	data.append(toList("[[6]]"))

	data.sort(key=functools.cmp_to_key(isOrdered))
	decoderKey = 1
	for i in range(len(data)):
		if data[i] == [[2]] or data[i] == [[6]]:
			decoderKey *= i + 1

	print(decoderKey)

f = open("input/13")

data = f.readlines()

p1(data)
p2(data)




