class Dir(object):
	def __init__(self, name):
		self.name = name
		self.children = dict()
		self.docs = []
		self.parent = None
		self.size = None

	def addChild(self, childName, childDir):
		self.children[childName] = childDir

	def addDoc(self, doc):
		self.docs.append(doc)

	def addParent(self, parent):
		self.parent = parent

	def calcsize(self):
		totSize = 0
		sizeOfAllUnder100000 = 0
		for child in self.children:
			child = self.children[child]
			chisize = child.calcsize()
			totSize += chisize[0]
			sizeOfAllUnder100000 += chisize[1]
		for doc in self.docs:
			totSize += doc.size
		self.size = totSize
		if totSize <= 100000:
			sizeOfAllUnder100000 += totSize
		return totSize, sizeOfAllUnder100000

class Doc(object):
	"""docstring for Doc"""
	def __init__(self, name, size):
		self.name = name
		self.size = size
		

f = open("input/07")

data = f.readlines()

currDir = None
startDir = None
for x in data:
	if x[0] == '$':
		x = x.strip().split()
		if x[1] == "cd":
			dirname = x[2]
			if dirname == "..":
				currDir = currDir.parent
			else:
				if currDir == None:
					currDir = Dir(dirname)
					startDir = currDir
				else:
					currDir = currDir.children[dirname]
		#elif x[1] == "ls":
	else:
		x = x.strip().split()
		if x[0] == "dir":
			dirname = x[1]
			if dirname not in currDir.children:
				newDir = Dir(dirname)
				newDir.addParent(currDir)
				currDir.addChild(dirname, newDir)
		else:
			size = int(x[0])
			name = x[1]
			newDoc = Doc(name, size)
			currDir.addDoc(newDoc)

totsize, sizeunder100000 = startDir.calcsize()

print(sizeunder100000)

unusedSpace = 70000000 - totsize
neededSpace = 30000000 - unusedSpace

def findSizeClosestToVal(dir, val, mindir, minval):
	for child in dir.children:
		child = dir.children[child]
		if child.size >= val and child.size < minval:
			mindir = child.name
			minval = child.size
		mindir, minval = findSizeClosestToVal(child, val, mindir, minval)

	return (mindir, minval)

mindir, minval = findSizeClosestToVal(startDir, neededSpace, startDir.name, startDir.size)

print(mindir)
print(minval)




