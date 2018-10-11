'''
Snake Game

Controls:

W,A,S,D - Movement; 
SPACE - restart; 
Q - quit
'''

import numpy as np 
import pandas as pd
import time
import click
from SnakeGame import Environment

'''
If you want to watch your games, enter the log file number you want, and run watch() instead of play()

A new log file is created each time you start up the game to play
If you restart the game in the same session, the same log file is used
'''
# logFileNumber =  int(sys.argv[1])

@click.command(options_metavar='<options>')
@click.option("-n", "--file_number", type=int, help="Watch the games stored in this file", metavar='<int>', prompt=True)
def watch(file_number):
	"""
	Watch the games in a specific log file 

	Default file: Last log file
	"""
	number_path = "./Data/log_file_number.txt"
	log_file_number_txt = np.loadtxt(number_path, dtype='int')

	if file_number >= log_file_number_txt or file_number < 0:
		print("\nYou did not enter a valid log file number!\nReplaying last log file (file number: {})\n".format(log_file_number_txt-1))
		file_number = log_file_number_txt-1
	else:
		print("\nReplaying Log file {}\n".format(file_number))

	csv_file_path = "./Data/Logs/log_file{}.csv".format(file_number)

	RENDER_TO_SCREEN = True

	# Create environment
	env = Environment(wrap = False, grid_size = 10, rate = 90, tail = True, obstacles = False)

	if RENDER_TO_SCREEN:
		env.prerender()
	
	# No arrow on top of snakes head
	env.noArrow()

	avg_time = 0
	avg_score = 0

	episode = 0

	df = pd.read_csv(csv_file_path)
	# print(df)

	GAME_OVER = False
	GAME_ON = True

	t = 3

	time_stamps = df["TIME_STAMP"].values

	snake_Xs = df["SNAKE_X"].values
	snake_Ys = df["SNAKE_Y"].values

	food_Xs = df["FOOD_X"].values
	food_Ys = df["FOOD_Y"].values

	my_actions = df["INPUT_BUTTON"].values

	my_index = 0

	while GAME_ON:

		# needs to be changed to ignore the SCALE
		state, info = env.irl_reset(snake_Xs[my_index], snake_Ys[my_index], food_Xs[my_index], food_Ys[my_index])
		# last_action = 3
		last_action = my_actions[my_index]

		# print(state)

		my_index = my_index + 1 #BUG: TODO: FIX MY_INDEX

		if RENDER_TO_SCREEN:
			env.countdown = True
		else:
			env.countdown = False

		while not GAME_OVER:

			try:
				if RENDER_TO_SCREEN:
					env.render()

				action = last_action

				# print(self.time)
				if my_index < len(my_actions):

					# Ensuring that it takes the last action pressed during that "tick"
					last_action_pressed = False
					i = 1
					while not last_action_pressed:
						if my_index + i < len(my_actions) and time_stamps[my_index] == time_stamps[my_index + i]:
							my_index = my_index + 1
							i = i + 1
						else:
							last_action_pressed = True

					# print(time_stamps[my_index])
					if env.time == time_stamps[my_index]:
						action = my_actions[my_index]
						last_action = action
						if action != -1:
							my_index = my_index + 1

				if env.countdown:
					text = env.font.render(str(t), True, (255, 255, 255))
					env.display.blit(text,(60,30))
					env.pg.display.update()
					time.sleep(0.4)
					t =  t - 1
					if t == 0:
						t = 3
						env.countdown = False
				else:
					new_state, reward, GAME_OVER, info = env.step(action, action_space = 4)

					if reward > 0:
						env.food.irl_make(food_Xs[my_index], food_Ys[my_index], env.SCALE)
						# new_state = env.get_state()

				if GAME_OVER:
					avg_time += info["time"]
					avg_score += info["score"]
					my_index = my_index + 1

			except KeyboardInterrupt as e:
				raise e

		while GAME_OVER:

			if my_index >= len(my_actions)-1:
				# print("Total Episodes: ", episode)
				env.end()
			else:
				GAME_OVER = False
				episode = episode + 1
				avg_time = 0
				avg_score = 0

	# print("Total Episodes: ", episode+1)
	env.end()


# Just incase someone types python replay.py
if __name__ == '__main__':

	watch()
