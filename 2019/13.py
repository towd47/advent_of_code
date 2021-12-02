import intcode_computer
import curses

def advent_13a():
	comp = setup()

	grid = {}

	output = []
	while not comp.finished:
		comp.run_pause_on_input_and_output()
		output.append(comp.output)

		if len(output) == 3:
			if output[2] == 2:
				pos = (output[0], output[1])
				grid[pos] = 2
			output.clear()

	print("13a: ", len(grid))

def advent_13b():
	comp = setup()
	comp.set_memory_value(0, 2)

	grid = {}
	output = []
	input_values = []
	score = 0
	player_pos = 0
	ball_pos = 0
	while not comp.finished:
		comp.run_pause_on_input_and_output()

		if comp.sent_output:
			output.append(comp.output)

		if len(output) == 3:
			if output[0] == -1 and output[1] == 0:
				score = output[2]
			else:
				pos = (output[0], output[1])
				if output[2] == 3:
					player_pos = output[0]
				elif output[2] == 4:
					ball_pos = output[0]
				grid[pos] = output[2]
			output.clear()

		if comp.waiting_for_input:
			input_val = get_dir_to_move(player_pos, ball_pos)

			input_values.append(input_val)
			comp.input(input_val)

	print("13b: ", score)

def advent_13c(play):
	stdscr = curses.initscr()
	stdscr.keypad(True)
	stdscr.clear()
	curses.curs_set(False)

	comp = setup()
	comp.set_memory_value(0, 2)

	output = []
	input_values = []
	score = 0
	player_pos = 0
	ball_pos = 0
	while not comp.finished:
		comp.run_pause_on_input_and_output()

		if comp.sent_output:
			output.append(comp.output)

		if len(output) == 3:
			if output[0] == -1 and output[1] == 0:
				score = output[2]
			else:
				stdscr.move(output[1], output[0])
				stdscr.addch(num_to_char(output[2]))

				pos = (output[0], output[1])
				if output[2] == 3:
					player_pos = output[0]
				elif output[2] == 4:
					ball_pos = output[0]
				stdscr.refresh()
			output.clear()

		if comp.waiting_for_input:
			if play == 1:
				key_pressed = stdscr.getkey()
				input_val = key_to_val(stdscr, key_pressed)
			else:
				curses.napms(1)
				input_val = get_dir_to_move(player_pos, ball_pos)

			input_values.append(input_val)
			comp.input(input_val)

	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()

	curses.endwin()
	print(score)

def get_dir_to_move(player_pos, ball_pos):
	if ball_pos > player_pos:
		return 1
	elif ball_pos < player_pos:
		return -1
	else:
		return 0

def key_to_val(stdscr, key):
	if key == "KEY_RIGHT":
		return 1
	elif key == "KEY_LEFT":
		return -1
	else:
		return 0

def num_to_char(num):
	if num == 0:
		return " "
	elif num == 1:
		return "|"
	elif num == 2:
		return "#"
	elif num == 3:
		return "-"
	else:
		return "*"

def setup():
	f = open("13.txt", "r")
	intcode_str = f.readline()
	intcode = list(map(int, intcode_str.split(",")))

	comp = intcode_computer.Intcode_computer(intcode)
	return comp

advent_13a()
advent_13b()

# advent_13c(0)