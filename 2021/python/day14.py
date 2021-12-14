from collections import Counter

def add_to_template(template, rules):
	i = 0
	while i < len(template) - 1:
		key = template[i:i+2]
		if key in rules:
			val = rules[key]
			template = template[:i+1] + val + template[i+1:]
			i += 1
		i += 1

	return template

day14_input = open("../day_14_input.txt")
data = day14_input.readlines()

template = data[0].strip()

pair_insertion_rules = data[2:]

rules = {}

for pair in pair_insertion_rules:
	[key, val] = pair.split(' -> ')
	rules[key.strip()] = val.strip()

for i in range(10):
	template = add_to_template(template, rules)

x = Counter(template)

most_common = x.most_common(1)[0]
least_common = x.most_common()[:-2:-1][0]

print(most_common[1] - least_common[1])
