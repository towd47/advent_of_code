INPUT_PATH = "../inputs/day_12_input.txt"

def find_path(cave_system, path, current_location):
	paths = []
	for i in cave_system[current_location]:
		new_path = path + ',' + i
		if i == 'end':
			paths.append(new_path)
		elif i.isupper() or i not in path:
			paths.extend(find_path(cave_system, new_path, i))
	return paths

def find_path_two_visits(cave_system, path, current_location, small_repeated = False):
	paths = []
	for i in cave_system[current_location]:
		new_path = path + ',' + i
		if i == 'end':
			paths.append(new_path)
		else:
			can_add_to_path = i.isupper() or i not in path
			if can_add_to_path:
				paths.extend(find_path_two_visits(cave_system, new_path, i, small_repeated))
			elif i != 'start' and not small_repeated and path.count(i) < 2:
				paths.extend(find_path_two_visits(cave_system, new_path, i, True))

	return paths


day12_input = open(INPUT_PATH)
data = day12_input.readlines()

cave_system = {}

for line in data:
	line = line.strip()
	key, val = line.split('-')
	if key in cave_system:
		l = cave_system[key]
		l.append(val)
		cave_system[key] = l
	else:
		cave_system[key] = [val]
	if val in cave_system:
		l = cave_system[val]
		l.append(key)
		cave_system[val] = l
	else:
		cave_system[val] = [key]

path = 'start'


paths = find_path(cave_system, path, path)
print(len(paths))
paths = find_path_two_visits(cave_system, path, path)
print(len(paths))



