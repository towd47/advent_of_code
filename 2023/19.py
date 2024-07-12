import readInput
import re

def mapChar(c):
	if c == "x": return 0
	if c == "m": return 1
	if c == "a": return 2
	if c == "s": return 3

def applyRule(rating, rule):
	i = 0
	while True:
		if rule[i] == "A":
			return (1, None)
		if rule[i] == "R":
			return (-1, None)
		if "<" in rule[i]:
			c, n = rule[i].split("<")
			if rating[mapChar(c)] < int(n):
				i += 1
			else:
				i += 2
		elif ">" in rule[i]:
			c, n = rule[i].split(">")
			if rating[mapChar(c)] > int(n):
				i += 1
			else:
				i += 2
		else:
			return (0, rule[i])

def applyAllRules(rating, rules, ruleKey):
	rule = rules[ruleKey]
	res = applyRule(rating, rule)
	if res[0] == 1:
		return sum(rating)
	elif res[0] == -1:
		return 0
	else:
		return applyAllRules(rating, rules, res[1])

def solve():
	lines = readInput.yieldLines("19")

	rules = dict()
	while line := next(lines).strip():
		key, actions = line.split("{")
		actions = actions[:-1]
		actions = re.split(r":|,", actions)
		rules[key] = actions

	ratings = []
	for line in lines:
		line = line.strip()
		vals = [int(x) for x in re.findall(r'\d+', line)]
		ratings.append(vals)
	
	p1(ratings, rules)

def p1(ratings, rules):
	tot = 0
	for rating in ratings:
		tot += applyAllRules(rating, rules, "in")

	print(tot)

if __name__ == "__main__":
	solve()
