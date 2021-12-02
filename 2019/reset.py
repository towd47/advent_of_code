import curses

def reset_curses():
	stdscr = curses.initscr()
	stdscr.keypad(True)
	stdscr.clear()
	curses.curs_set(False)

	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()

	curses.endwin()

reset_curses()