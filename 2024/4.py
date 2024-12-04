from readInput import linesToList
import re
import sys

def solve(filename='4'):
	lines = linesToList(filename)
	print(p1(lines))
	print(p2(lines))
	print(p2take2(lines))

def p1(lines):
	lines1 = lines.copy()
	lines1.extend([''.join(s) for s in zip(*lines)])
	lines1.extend([''.join(s) for s in diagonals(lines)])
	lines1.extend([''.join(s) for s in antidiagonals(lines)])

	fw = sum([len(re.findall(r'(XMAS)', line)) for line in lines1])
	bw = sum([len(re.findall(r'(SAMX)', line)) for line in lines1])

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
		diag_occurrences[i] = set([diagToCoord(rows, e2, i) for e2 in e])

	for i, e in enumerate(antidiag_occurrences):
		antidiag_occurrences[i] = set([antidiagToCoord(rows, e2, i) for e2 in e])

	s1 = set.union(*diag_occurrences)
	s2 = set.union(*antidiag_occurrences)
	return len(s1 & s2)

def diagonals(lines):
	rows, cols = len(lines), len(lines[0])
	return [[lines[rows - p + q - 1][q] for q in range(max(p-rows+1, 0), min(p+1, cols))] for p in range(rows + cols - 1)]

def antidiagonals(lines):
	rows, cols = len(lines), len(lines[0])
	return [[lines[p - q][q] for q in range(max(p-rows+1,0), min(p+1, cols))] for p in range(rows + cols - 1)]

def diagToCoord(rows, val, rowpos):
	return (rows - 1 - rowpos + val,val) if rowpos <= rows - 1 else (val,rowpos-rows+1+val)

def antidiagToCoord(rows, val, rowpos):
	return (rowpos - val,val) if rowpos <= rows - 1 else (rows-val-1, rowpos-rows+1+val)


def p2take2(lines):
	rows = len(lines)
	cols = len(lines[0])
	s = [sum([checkPos(lines, (row, col)) if lines[row][col] == 'A' else False for col, _ in enumerate(row_vals)]) for row, row_vals in enumerate(lines)]
	return sum(s)

def checkPos(lines, pos):
	row = pos[0]
	col = pos[1]
	if row < 1 or col < 1 or row >= len(lines) - 1 or col >= len(lines[0]) - 1:
		return False

	d1 = (lines[row-1][col-1] == 'M' and lines[row+1][col+1] == 'S') or (lines[row-1][col-1] == 'S' and lines[row+1][col+1] == 'M')
	d2 = (lines[row-1][col+1] == 'M' and lines[row+1][col-1] == 'S') or (lines[row-1][col+1] == 'S' and lines[row+1][col-1] == 'M')
	return d1 and d2


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
