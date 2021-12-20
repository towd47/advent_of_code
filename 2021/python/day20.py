# 5362 TOO HIGH 
# 4942 TOO HIGH

def extend_img(image, num=1):
	char = '.'
	for i in range(len(image)):
		image[i] = char * num + image[i] + char * num
	for i in range(num):
		image.insert(0, char * len(image[0]))
		image.append(char * len(image[0]))
	return image

def enhance_img(extended_image, enhancement_algo):
	enhanced_image = ['.' * len(extended_image[0])] * len(extended_image)
	for i in range(1, len(extended_image) - 1):
		for j in range(1, len(extended_image[i]) - 1):
			binary = ''
			for x in range(i - 1, i + 2):
				for y in range(j - 1, j + 2):
					if extended_image[x][y] == '.':
						binary = binary + '0'
					else:
						binary = binary + '1'
			binary = int(binary, 2)
			char = enhancement_algo[binary]
			if char == '#':
				enhanced_image[i] = enhanced_image[i][:j] + char + enhanced_image[i][j+1:]
	enhanced_image.pop(0)
	enhanced_image.pop()
	for i in range(len(enhanced_image)):
		enhanced_image[i] = enhanced_image[i][1:-1]
	return enhanced_image

day20_input = open("../day_20_input.txt")
data = day20_input.readlines()

enhancement_algo = data[0].strip()

image = []
for i in range(2, len(data)):
	image.append(data[i].strip())

image = extend_img(image, 52)
for i in range(50):
	if i == 2:
		lit_count = 0
		for x in image:
			lit_count += x.count('#')

		print(lit_count)
	if i % 2 == 0:
		image = extend_img(image, 2)
	image = enhance_img(image, enhancement_algo)

lit_count = 0
for x in image:
	lit_count += x.count('#')

print(lit_count)