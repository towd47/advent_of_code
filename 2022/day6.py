f = open("input/06")

data = f.readline()

data = list(data.strip())

buff = data[:4]

pos = 4

foundMarker = False
while not foundMarker:
	if len(set(buff)) == 4:
		foundMarker = True
	else:
		buff.pop(0)
		buff.append(data[pos])
		pos += 1

print(pos)

buff = data[:14]

pos = 14

foundMarker = False
while not foundMarker:
	if len(set(buff)) == 14:
		foundMarker = True
	else:
		buff.pop(0)
		buff.append(data[pos])
		pos += 1

print(pos)

