INPUT_PATH = "../inputs/day_14_input.txt"

def apply_rules(current_pairs, rules):
	new_pairs = {}

	for pair in current_pairs:
		resulting_pairs = rules[pair]
		for rp in resulting_pairs:
			if rp in new_pairs:
				new_pairs[rp] += current_pairs[pair]
			else:
				new_pairs[rp] = current_pairs[pair]

	return new_pairs

def apply_rules_x_times(current_pairs, rules, x):
	for i in range(x):
		current_pairs = apply_rules(current_pairs, rules)
	return current_pairs

def score_pairs(current_pairs):
	starting_letters = {}

	for pair in current_pairs:
		s = pair[0]
		num = current_pairs[pair]
		if s in starting_letters:
			starting_letters[s] += num
		else:
			starting_letters[s] = num

	starting_letters[ending_letter] += 1

	return max(starting_letters.values()) - min(starting_letters.values())

# READ INPUT INTO EXISTING PAIRS AND RULES
day14_input = open(INPUT_PATH)
data = day14_input.readlines()

template = data[0].strip()
ending_letter = template[-1]

current_pairs = {}

for i in range(len(template) - 1):
	key = template[i:i+2]
	if key in current_pairs:
		current_pairs[key] += 1
	else:
		current_pairs[key] = 1

pair_insertion_rules = data[2:]

rules = {}

for pair in pair_insertion_rules:
	[key, val] = pair.split(' -> ')
	vals = (key[0] + val.strip(), val.strip() + key[1])
	rules[key] = vals


# Compute soln
current_pairs = apply_rules_x_times(current_pairs, rules, 10)
print(score_pairs(current_pairs))
current_pairs = apply_rules_x_times(current_pairs, rules, 30)
print(score_pairs(current_pairs))


# IDEA -> Rules lead to new pairs, count number of each pair cumulatively
# CH -> CB, BH
# CB -> CH, BH
# BH -> BH, HH
# HH -> HN, NH
# HN -> HC, CN
# NH -> NC, CH
# NN -> NC, CN
# CN -> CC, CN
# Pairs = NNCB : NN - 1, NC - 1, CB - 1
# Length 4
# Do 1 step: NNCB -> NCNBCHB : NC - 1, CN - 1, NB - 1, BC - 1, CH - 1, HB - 1
