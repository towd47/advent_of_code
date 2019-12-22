from collections import Counter

def advent_8a():
	f = open("8.txt", "r")
	image_data = f.readline()

	width = 25
	height = 6

	layers = list()

	while image_data:
		layers.append(image_data[:width * height])
		image_data = image_data[width * height:]

	min_count = width * height
	least_0_layer_counter = None

	for layer in layers:
		item_count = Counter(layer)
		if item_count['0'] < min_count:
			min_count = item_count['0']
			least_0_layer_counter = item_count

	return least_0_layer_counter['1'] * least_0_layer_counter['2']

def advent_8b():
	f = open("8.txt", "r")
	image_data = f.readline()

	width = 25
	height = 6

	layers = list()

	while image_data:
		layers.append(image_data[:width * height])
		image_data = image_data[width * height:]

	overlap_layer = layers[0]
	print(overlap_layer)

	for layer in layers:
		for pos in range(0, width * height) :
			if overlap_layer[pos] == '2' and layer[pos] != '2':
				overlap_layer = overlap_layer[:pos] + layer[pos] + overlap_layer[pos+1:]

	lines = []
	for i in range(0, len(overlap_layer), width):
		lines.append(overlap_layer[i:i+width])
	overlap_layer = '\n'.join(lines)

	return overlap_layer.replace('0', ' ')

print(advent_8b())