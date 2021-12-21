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