import statistics

INPUT_PATH = "../inputs/day_10_input.txt"

def is_open_char(c):
	open_chars = ['(', '[', '{', '<']
	return c in open_chars

def is_match(o, c):
	char_match = {'(':')', '[':']', '{':'}', '<':'>'}
	return char_match.get(o) == c

def is_corrupt(line):
	open_chars = []
	for c in line:
		if is_open_char(c):
			open_chars.append(c)
		else:
			if not open_chars:
				return 0
			if not is_match(open_chars.pop(), c):
				return c
	return 0

def complete_line(line):
	char_match = {'(':')', '[':']', '{':'}', '<':'>'}
	open_chars = []
	for c in line:
		if is_open_char(c):
			open_chars.append(c)
		else:
			open_chars.pop()
	open_chars.reverse()
	close_chars = []
	for c in open_chars:
		close_chars.append(char_match.get(c))
	return close_chars

def score_chars(chars):
	score = 0
	scoring = {')':1, ']':2, '}':3, '>':4}

	for c in chars:
		score = score * 5 + scoring.get(c)

	return score

day10_input = open(INPUT_PATH)
data = day10_input.readlines()

incomplete = []

score = 0
scoring = {')':3, ']':57, '}':1197, '>':25137}
for line in data:
	line = line.strip()
	c = is_corrupt(line)
	if c != 0:
		score = score + scoring.get(c)
	else:
		incomplete.append(line)

print(score)

scores = []
for line in incomplete:
	chars_to_complete = complete_line(line)
	scores.append(score_chars(chars_to_complete))

print(statistics.median(scores))
