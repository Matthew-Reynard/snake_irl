'''
Simple SnakeAI Game with basic Q Learning

INFO:
@author: Matthew Reynard
@year: 2018

DESCRIPTION:
QLearn.py is a a simple implementation of a Q learning algorithm with a lookup table of Q values
You can change the code in the main() function to either train(), run(), or play() 
- with the latter being just for fun and to explore the world and see whats happening and
what the computer is learning to do

TO DO LIST:
- Comment all the code
- Make a more user friendly method to change between the train, run and play methods
- Add a score
-

'''

import numpy as np 
import pandas as pd
import csv
import sys
import time
from SnakeGame import Environment


# dimensions: (states, actions)
def Qmatrix(x, env):
	if x == 0:
		Q = np.zeros((env.number_of_states(), env.number_of_actions()))
	elif x == 1:
		np.random.seed(0) # To ensure the results can be recreated
		Q = np.random.rand(env.number_of_states(), env.number_of_actions()) 
	elif x == 2:
		Q = np.loadtxt(Q_textfile_path_load, dtype='float', delimiter=" ")
	return Q


# Play the game yourself :)
def play():

	env = Environment(wrap = False, grid_size = 10, rate = 150, tail = True, obstacles = False)

	env.play()


# Inverse RL
def watch():

	csv_file_path = "./Data/Logs/log_file11.csv"

	RENDER_TO_SCREEN = True

	# rate should be 0 when not rendering, else it will lengthen training time unnecessarily
	env = Environment(wrap = False, grid_size = 10, rate = 80, tail = True, obstacles = False)

	if RENDER_TO_SCREEN:
		env.prerender()
	
	avg_time = 0
	avg_score = 0

	episode = 0

	df = pd.read_csv(csv_file_path)
	print(df)

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
		last_action = 3

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
					env.display.blit(text,(180,180))
					env.pg.display.update()
					time.sleep(0.5)
					t =  t - 1
					if t == 0:
						t = 3
						env.countdown = False
				else:
					# print(action)
					new_state, reward, GAME_OVER, info = env.step(action, action_space = 4)
					# print(reward)

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
				print("Total Episodes: ", episode)
				env.end()
			else:
				GAME_OVER = False
				episode = episode + 1
				avg_time = 0
				avg_score = 0

	print("Total Episodes: ", episode)
	env.end()


if __name__ == '__main__':

	play()

	# watch()
