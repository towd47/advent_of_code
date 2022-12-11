import copy

# #############
# #...........#
# ###D#A#B#C###
#   #B#A#D#C#
#   #########

# #############
# #AA.........#
# ###D#.#B#C###
#   #B#.#D#C#
#   #########

# #############
# #AA...C...C.#
# ###D#.#.#.###
#   #B#B#D#.#
#   #########

# #############
# #AA.........#
# ###D#.#C#.###
#   #B#B#C#D#
#   #########

# PART 1 SOLUTION
# a
# 5, 5, 3, 3 - 	16 -    16
# b
# 5, 5			10 -   100
# c
# 7, 7			14 -  1400
# d
# 6, 8			14 - 14000
# 					 15516

# PART 2
class Point:
	row = 0
	col = 0
	value = ''
	moved = False
	finished = False

	def __str__(self):
		return self.value

class State:
	letters = ['A', 'B', 'C', 'D']
	not_allowed = [2, 4, 6, 8]
	value_col = {'A':2, 'B':4, 'C':6, 'D':8}
	score_map = {'A':1, 'B':10, 'C':100, 'D':1000}
	points = []

	def __init__(text_board):
		self.make_pts(text_board)
		self.board = []
		for x in range(5):
			self.board.append([None] * 5)
		for point in self.points:
			self.board[point.row][point.col] = point
		for key in value_col:
			for i in range(4, 0, -1):
				if self.board[i][value_col[key]].value == key:
					self.board[i][value_col[key]].moved = True
					self.board[i][value_col[key]].finished = True
				else:
					break

	def make_pts(self, text_board):
		for x in range(text_board):
			for y in range(text_board[0]):
				if text_board[x][y] in self.letters:
					point = Point()
					point.row = x
					point.col = y
					point.value = text_board[x][y]
					self.points.append(point)

	def est_cost_to_finish():
		total = 0
		for point in self.points:
			moves = 0
			if not point.moved:
				moves += point.row
			side_dist = abs(point.col - value_col[point.value])
			if side_dist == 0 and not point.moved:
				side_dist = 2
			moves += side_dist
			if not point.moved:
				moves += 4
			else:
				moves += 4 - point.row
			total += moves * score_map[point.value]


	# Board Representationn
	# Current Cost to reach
	# Estimated best cost to finish from here
	# Generate possible states from here

# #############
# #...........#
# ###D#A#B#C###
#	#D#C#B#A#
#	#D#B#A#C#
#   #B#A#D#C#
#   #########

# 45244 WRONG - added my numbers wrong
# 45324 WRONG - starting with C col
# 45330 ????? - starting with B col
# 45776 ????? - starting with D col
# 45304 WRONG - started with C
# 45298 ????? - started with C col - WRONG MATH


diagram = '........... ##D#A#B#C## ##B#A#D#C#'.split()
# diagram = '........... ##D#A#B#C## ##D#C#B#A# ##D#B#A#C# ##B#A#D#C#'.split()
for i in range(len(diagram)):
	diagram[i] = list(diagram[i])

points = []
for i in range(len(diagram) - 1):
	p = Point()
	p.row = i + 1
	p.col = 2
	p.value = diagram[p.row][p.col]
	points.append(p)

for i in range(len(diagram) - 1):
	p = Point()
	p.row = i + 1
	p.col = 4
	p.value = diagram[p.row][p.col]
	points.append(p)

for i in range(len(diagram) - 1):
	p = Point()
	p.row = i + 1
	p.col = 6
	p.value = diagram[p.row][p.col]
	points.append(p)

for i in range(len(diagram) - 1):
	p = Point()
	p.row = i + 1
	p.col = 8
	p.value = diagram[p.row][p.col]
	points.append(p)

not_allowed = [2, 4, 6, 8]
value_col = {'A':2, 'B':4, 'C':6, 'D':8}
score_map = {'A':1, 'B':10, 'C':100, 'D':1000}

def can_move(point, diagram):
	points = []
	if point.row > 0:
		if point.moved:
			return[]
		for i in range(0, point.row):
			if diagram[i][point.col] != '.':
				return []
		for i in range(point.col + 1, len(diagram[0])):
			if diagram[0][i] != '.':
				break
			if i not in not_allowed:
				p = Point()
				p.row = 0
				p.col = i
				p.value = point.value
				p.moved = True
				points.append(p)
		for i in range(point.col-1, -1, -1):
			if diagram[0][i] != '.':
				break
			if i not in not_allowed:
				p = Point()
				p.row = 0
				p.col = i
				p.value = point.value
				p.moved = True
				points.append(p)
	else:
		deepest = 1
		for i in range(1, 5):
			if diagram[i][value_col[point.value]] != point.value:
				return []
			elif diagram[i][value_col[point.value]] == '.':
				deepest = i
		p = Point()
		p.row = deepest
		p.col = value_col[point.value]
		p.value = point.value
		p.moved = True

	return points

def dist_between_pts(p1, p2):
	return abs(p1.row - p2.row) + abs(p1.col - p2.col)

def solved(diagram):
	for i in range(1, 5):
		for x in value_col:
			if diagram[i][value_col[x]] != x:
				return False
	return True


def solve(points, diagram, score):
	min_score = 100000
	scores = []
	popped_points = []
	for x in diagram:
		print(x)
	input()
	while points:
		point_to_move = points.pop()
		available_pts = can_move(point_to_move, diagram)
		if available_pts:
			for point in available_pts:
				points2 = copy.deepcopy(points)
				points2.append(point)
				points2.extend(copy.deepcopy(popped_points))
				diagram2 = copy.deepcopy(diagram)
				diagram2[point_to_move.row][point_to_move.col] = '.'
				diagram2[point.row][point.col] = point.value
				score2 = (score + dist_between_pts(point_to_move, point)) * score_map[point.value]
				if score2 < min_score:
					s = solve(points2, diagram2, score2)
					if s:
						scores.extend(s)
		popped_points.append(point_to_move)
	if not scores:
		if solved(diagram):
			min_score = min(min_score, score)
			return [score]
	return scores
	
scores = solve(points, diagram, 0)
print(scores)













