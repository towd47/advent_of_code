import copy
class Monkey(object):
	def __init__(self, items, opvals, test, throw1, throw2):
		self.items = items
		self.opvals = opvals
		self.test = test
		self.throw1 = throw1
		self.throw2 = throw2
		self.inspected = 0
		
def readMonkeys(data):
	monkeys = []
	while data:
		monkeyNum = int(data.pop(0).strip().strip(":").split()[-1])
		startingItems = list(map(int, data.pop(0).strip().split(":")[1].strip().split(", ")))
		op = data.pop(0).strip().split("=")[1]
		opvals = op.split()
		testval = int(data.pop(0).strip().split()[-1])
		throw1 = int(data.pop(0).strip().split()[-1])
		throw2 = int(data.pop(0).strip().split()[-1])

		monk = Monkey(startingItems, opvals, testval, throw1, throw2)
		monkeys.append(monk)

		if data:
			data.pop(0)
	return monkeys

def cycleMonkeys(monkeys):
	for monk in monkeys:
		while monk.items:
			item = monk.items.pop(0)
			item = operation(item, monk.opvals)
			item = int(item/3)
			if item % monk.test == 0:
				monkeys[monk.throw1].items.append(item)
			else:
				monkeys[monk.throw2].items.append(item)

			monk.inspected += 1

def cycleMonkeys2(monkeys, modnum):
	for monk in monkeys:
		while monk.items:
			item = monk.items.pop(0)
			item = item % modnum
			item = operation(item, monk.opvals)
			if item % monk.test == 0:
				monkeys[monk.throw1].items.append(item)
			else:
				monkeys[monk.throw2].items.append(item)

			monk.inspected += 1

def operation(item, opvals):
	v1 = opvals[0]
	v2 = opvals[2]
	if v1 == 'old':
		v1 = item
	if v2 == 'old':
		v2 = item
	v1 = int(v1)
	v2 = int(v2)
	return doOp(opvals[1], v1, v2)

def doOp(opchar, v1, v2):
	if opchar == '+':
		return v1 + v2
	if opchar == '-':
		return v1 - v2
	if opchar == '*':
		return v1 * v2
	if opchar == '/':
		return v1 / v2

f = open("input/11")

data = f.readlines()

monkeys = readMonkeys(data)
monkeys2 = copy.deepcopy(monkeys)

modnum = 1
for monk in monkeys2:
	modnum *= monk.test

for _ in range(20):
	cycleMonkeys(monkeys)

for i in range(10000):
	cycleMonkeys2(monkeys2, modnum)

inspections = []
for monk in monkeys:
	inspections.append(monk.inspected)

inspections.sort()
print(inspections[-1] * inspections[-2])

inspections = []
for monk in monkeys2:
	inspections.append(monk.inspected)

inspections.sort()
print(inspections[-1] * inspections[-2])


