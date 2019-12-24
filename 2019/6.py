def advent_6a():
	f = open("6.txt", "r")
	lines = f.readlines()

	com = Node("COM")
	com.set_depth(0)

	objects = set()
	objects.add(com)

	for line in lines:
		bodies = line.split(")")

		obj1 = contains_object(bodies[0].strip(), objects)
		obj2 = contains_object(bodies[1].strip(), objects)

		if obj1 is None:
			obj1 = Node(bodies[0].strip())
			objects.add(obj1)
		
		if obj2 is None:
			obj2 = Node(bodies[1].strip())
			objects.add(obj2)

		obj1.add_child(obj2)

	objects_to_update = list()
	objects_to_update.append(com)	

	while objects_to_update:
		obj = objects_to_update.pop()

		for child in obj.get_children():
			child.set_depth(obj.depth + 1)

		objects_to_update.extend(obj.get_children())

	orbits = 0
	for obj in objects:
		orbits += obj.depth

	return orbits

def advent_6b():
	f = open("6.txt", "r")
	lines = f.readlines()

	com = Node("COM")
	com.set_depth(0)

	objects = set()
	objects.add(com)

	for line in lines:
		bodies = line.split(")")

		obj1 = contains_object(bodies[0].strip(), objects)
		obj2 = contains_object(bodies[1].strip(), objects)

		if obj1 is None:
			obj1 = Node(bodies[0].strip())
			objects.add(obj1)
		
		if obj2 is None:
			obj2 = Node(bodies[1].strip())
			objects.add(obj2)

		obj2.set_parent(obj1)
		obj1.add_child(obj2)

	objects_to_update = list()
	objects_to_update.append(com)	

	while objects_to_update:
		obj = objects_to_update.pop()

		for child in obj.get_children():
			child.set_depth(obj.depth + 1)

		objects_to_update.extend(obj.get_children())

	you_parent_list = set()
	san_parent_list = set()

	you = None
	san = None

	for obj in objects:
		if obj.name == "YOU":
			you = obj
		if obj.name == "SAN":
			san = obj


	start_node = you
	while start_node.parent:
		you_parent_list.add(start_node.parent)
		start_node = start_node.parent

	start_node = san
	while start_node.parent:
		san_parent_list.add(start_node.parent)
		start_node = start_node.parent

	overlap = you_parent_list & san_parent_list
	
	max_depth = 0
	for node in overlap :
		if node.depth > max_depth:
			max_depth = node.depth

	return you.depth - max_depth + san.depth - max_depth - 2



def contains_object(name, list):
	for obj in list:
		if obj.name == name:
			return obj
	return None

class Node(object):
	def __init__(self, name):
		self.name = name
		self.depth = 0
		self.children = list()
		self.parent = None

	def set_parent(self, parent):
		self.parent = parent

	def add_child(self, child):
		self.children.append(child)

	def get_children(self):
		return self.children

	def set_depth(self, depth):
		self.depth = depth

print("6a: ", advent_6a())
print("6b: ", advent_6b())