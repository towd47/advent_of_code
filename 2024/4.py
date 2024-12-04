from readInput import linesToList
import re
import sys

def solve(filename='4'):
	lines = linesToList(filename)
	print(p1(lines))
	print(p2(lines))

def p1(lines):
	horiz_lines = lines.copy()
	vert_lines = [''.join(s) for s in zip(*horiz_lines)]
	diag_lines = [''.join(s) for s in diagonals(horiz_lines)]
	antidiag_lines = [''.join(s) for s in antidiagonals(horiz_lines)]

	horiz_lines.extend(vert_lines)
	horiz_lines.extend(diag_lines)
	horiz_lines.extend(antidiag_lines)

	fw = sum([len(re.findall(r'(XMAS)', line)) for line in horiz_lines])
	bw = sum([len(re.findall(r'(SAMX)', line)) for line in horiz_lines])

	return fw + bw

def p2(lines):
	rows = len(lines)
	cols = len(lines[0])
	
	diag_lines = [''.join(s) for s in diagonals(lines)]
	antidiag_lines = [''.join(s) for s in antidiagonals(lines)]

	diag_occurrences = [[match.start() + 1 for match in re.finditer(r'(MAS)', line)] for line in diag_lines]
	diag_occurrences2 = [[match.start() + 1 for match in re.finditer(r'(SAM)', line)] for line in diag_lines]
	for i, e in enumerate(diag_occurrences):
		diag_occurrences[i] = set(e) | set(diag_occurrences2[i])

	antidiag_occurrences = [[match.start() + 1 for match in re.finditer(r'(MAS)', line)] for line in antidiag_lines]
	antidiag_occurrences2 = [[match.start() + 1 for match in re.finditer(r'(SAM)', line)] for line in antidiag_lines]
	for i, e in enumerate(antidiag_occurrences):
		antidiag_occurrences[i] = set(e) | set(antidiag_occurrences2[i])

	for i, e in enumerate(diag_occurrences):
		diag_occurrences[i] = set([(rows - 1 - i + e2,e2) if i <= rows - 1 else (e2,i-rows+1+e2) for e2 in e])

	for i, e in enumerate(antidiag_occurrences):
		antidiag_occurrences[i] = set([(i - e2,e2) if i <= rows - 1 else (rows-e2-1, i-rows+1+e2) for e2 in e])

	s1 = set.union(*diag_occurrences)
	s2 = set.union(*antidiag_occurrences)
	return len(s1 & s2)

def diagonals(lines):
	rows, cols = len(lines), len(lines[0])
	return [[lines[rows - p + q - 1][q] for q in range(max(p-rows+1, 0), min(p+1, cols))] for p in range(rows + cols - 1)]

def antidiagonals(lines):
	rows, cols = len(lines), len(lines[0])
	return [[lines[p - q][q] for q in range(max(p-rows+1,0), min(p+1, cols))] for p in range(rows + cols - 1)]

if __name__ == '__main__':
	if len(sys.argv) >= 2:
		filename = sys.argv[1]
		solve(filename)
	else:
		solve()



# 0 1 2
# 3 4 5
# 6 7 8
# 9 a f
# 
# 
# ['9', '6a', '37f', '048', '15', '2']
# ['0', '31', '642', '975', 'a8', 'f']
# 
