import re

def shift_4(name):
	new_name = ''
	for x in name:
		x = x.lower()
		if x != ' ':
			n = ord(x) + 4
			if n > 122:
				n = n - 26
			new_name = new_name + chr(n)
		else:
			new_name = new_name + x
	return new_name

def swap_first_and_last_init(name):
	[first, last] = name.split()
	first_l = first[0]
	first = last[0] + first[1:]
	last = first_l + last[1:]
	return first + last

def remove_middle(name):
	median = int(len(name)/2)
	new_name = name[:median] + name[median + 1:]
	new_name = ''.join(new_name.split())
	return new_name

def remove_vowels(name):
	return (re.sub("[aeiouAEIOU ]","",name)) 

def remove_every_other(name):
	name = ''.join(name.split())
	first_let = ''
	second_let = ''
	for i in range(len(name)):
		if i % 2 == 0:
			first_let = first_let + name[i]
		else:
			second_let = second_let + name[i]
	return first_let + ', ' + second_let

def first_9(name):
	name = ''.join(name.split())
	return name[0:9]

done = ['Laloe Jade', 'Louisa Lemon', 'Olive Bourdeau', 
		'Gregoire Grey', 'Gretchen Periwinkle', 'Yossi Pink',
		'Violet Terlin', 'Rose Attenborough', 'Mahogany Wyndmoor',
		'Basil Copper', 'Ebony George', 'Jacques Bleu', 'Hal Black',
		'Wynn Thistle', 'Sienna Looney', 'Oliver Brown', 'Missy White', 
		'Regina Tan', 'Dona Silver', 'Suzette Gold', 'Louie Salmon']

s = [, 'Remi Green', 'Emma Grey']

for y in s:
# 	z = shift_4(y)
#	z = swap_first_and_last_init(y.lower())
#	z = remove_middle(y.lower())
#	z = remove_vowels(y.lower())
#	z = remove_every_other(y.lower())
#	z = first_9(y.lower())
	print(y, '->', z)