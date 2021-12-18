VERSION_SIZE = 3
TYPE_SIZE = 3
LENGTH_TYPE_SIZE = 1


def literal(bits, index):
	num = ''
	while bits[index] == '1':
		index += 1
		num = num + bits[index:index + 4]
		index += 4
	index += 1
	num = num + bits[index:index + 4]
	index += 4
	return num, index

def get_next_bits(num, bits, index):
	# print(index)
	# print(num)
	# print(bits)
	# val = int(bits[index:index+num], 2)
	# print(val)
	# print()
	return int(bits[index:index+num], 2), index + num

def process_packet(bits, index):
	v, index = get_next_bits(VERSION_SIZE, bits, index)
	t, index = get_next_bits(TYPE_SIZE, bits, index)
	num = None

	if t == 4:
		num, index = literal(bits, index)
	else:
		length_type, index = get_next_bits(LENGTH_TYPE_SIZE, bits, index)
		if length_type == 0:
			sublength, index = get_next_bits(15, bits, index)
			start_index = index
			while index < start_index + sublength:
				vp, nump, index = process_packet(bits, index)
				v += vp
		else:
			num_sub_packets, index = get_next_bits(11, bits, index)
			for i in range(num_sub_packets):
				vp, nump, index = process_packet(bits, index)
				v += vp
	return v, num, index


day16_input = open("../day_16_input.txt")
outer_packet = day16_input.readline().strip()

bits = str(bin(int(outer_packet, 16))[2:])
while len(bits) % 4 != 0:
	bits = '0' + bits

index = 0
v, num, index = process_packet(bits, index)
print(v)



