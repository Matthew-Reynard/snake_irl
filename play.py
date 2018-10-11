'''
Snake Game

Controls:

W,A,S,D - Movement; 
SPACE - restart; 
Q - quit
'''

import click
from SnakeGame import Environment

'''
Difficulty (Speed)

Easy = 200
Medium = 150
Hard = 100
Insane = 80
'''
# difficulty = 150 

@click.command(options_metavar='<options>')
@click.option("-d", "--difficulty", default="medium", help="Difficulty setting: <easy>, <medium>, <hard> or <insane>", metavar='<text>')
def play(difficulty):
	"""
	Play the Snake game, feel free to change the difficulty

	Default difficulty: Medium
	"""
	d = 150

	if difficulty == "easy":
		d = 200
		print("\nDifficulty set to <easy>\n")
	elif difficulty == "medium":
		d = 150
		print("\nDifficulty set to <medium>\n")
	elif difficulty == "hard":
		d = 100
		print("\nDifficulty set to <hard>\n")
	elif difficulty == "insane":
		d = 80
		print("\nDifficulty set to <insane>\n")
	else:
		print("\nYou did not enter a valid difficulty!\nDifficulty set to <medium>\n")

	env = Environment(wrap = False, grid_size = 10, rate = d, tail = True, obstacles = False)

	env.play()

# Just in case someone types python play.py
if __name__ == '__main__':

	play()
