PLAYER_1_START = 3
PLAYER_2_START = 5

i = 2
player1_score = 0
player2_score = 0

player1_pos = PLAYER_1_START
player2_pos = PLAYER_2_START

num_rolls = 0
die = list(range(1, 101))

p1_turn = True

while player1_score < 1000 and player2_score < 1000:
	if i >= 100:
		i = i % 100
		num_rolls += 100
	next_sum = sum([die[i-2], die[i-1], die[i]])
	if p1_turn:
		player1_pos = (player1_pos + next_sum) % 10
		if player1_pos == 0:
			player1_pos = 10
		player1_score += player1_pos
		p1_turn = False
	else:
		player2_pos = (player2_pos + next_sum) % 10
		if player2_pos == 0:
			player2_pos = 10
		player2_score += player2_pos
		p1_turn = True
	i += 3

num_rolls = num_rolls + i - 2
print(min(player1_score, player2_score) * num_rolls)

universes_and_moves = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}

starting_state = (0, PLAYER_1_START, PLAYER_2_START, 0, 0)

p1_states = {}
p2_states = {}

def solve(state, states, player_to_win):
	num = 0
	if player_to_win == 1:
		winning_score_pos = 3
		losing_score_pos = 4
	else:
		winning_score_pos = 4
		losing_score_pos = 3

	if state in states:
		return states[state]

	if state[winning_score_pos] >= 21 and state[losing_score_pos] < 21:
		states[state] = 1
		return 1

	elif state[losing_score_pos] >= 21:
		states[state] = 0
		return 0

	for key in universes_and_moves:
		player_turn = state[0]
		player1_pos = state[1]
		player2_pos = state[2]
		player1_score = state[3]
		player2_score = state[4]
		if player_turn == 0:
			player1_pos = (key + player1_pos) % 10
			if player1_pos == 0:
				player1_pos = 10
			player1_score += player1_pos
		else:
			player2_pos = (key + player2_pos) % 10
			if player2_pos == 0:
				player2_pos = 10
			player2_score += player2_pos
		player_turn = (player_turn + 1) % 2

		new_state = (player_turn, player1_pos, player2_pos, player1_score, player2_score)
		
		num += solve(new_state, states, player_to_win) * universes_and_moves[key]
	states[state] = num
	return num

solve(starting_state, p1_states, 1)
solve(starting_state, p2_states, 2)
print(max(p1_states[starting_state], p2_states[starting_state]))