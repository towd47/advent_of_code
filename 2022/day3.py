def getPrio(a):
	p = ord(a)
	if p <= 97:
		p -= 38
	else:
		p -= 96
	return p

f = open("input/03")

sacks = f.readlines()

prio = 0

for sack in sacks:
	sack = sack.strip()
	seta = set(sack[:int(len(sack) / 2)])
	setb = set(sack[int(len(sack)/2):])

	a = seta & setb

	c, = a
	p = getPrio(c)
	prio += p

print(prio)

prio = 0
sets = []
for sack in sacks:
	sack = sack.strip()
	sets.append(set(sack))
	if len(sets) == 3:
		i = sets[0] & sets[1] & sets[2]
		p, = i
		prio += getPrio(p)
		sets = []

print(prio)
