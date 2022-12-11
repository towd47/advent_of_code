def contains(e1, e2):
	if e1[0] <= e2[0] and e1[1] >= e2[1]:
		return True
	return False

def overlap(e1, e2):
	if e1[0] <= e2[0] and e1[1] >= e2[0]:
		return True
	if e1[0] <= e2[1] and e1[1] >= e2[1]:
		return True
	if e2[0] <= e1[1] and e2[1] >= e1[1]:
		return True
	if e2[0] <= e1[1] and e2[1] >= e1[1]:
		return True
	return False


f = open("input/04")

data = f.readlines()

totalcont = 0
totalover = 0
for x in data:
	x = x.strip()
	e1, e2 = x.split(',')

	e1 = list(map(int, e1.split('-')))
	e2 = list(map(int, e2.split('-')))

	if contains(e1, e2) or contains(e2, e1):
		totalcont += 1
	if overlap(e1, e2):
		totalover += 1

print(totalcont)
print(totalover)