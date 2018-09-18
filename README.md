# snake_irl
Snake game used to gather game data for IRL

---

### LIBRARIES USED:
virtualenv (helpful, but not necessary)  
numpy  
pygame  
pandas

### ABOUT:
This is the snake game with a fixed grid size of 8x8 and the aim of this exercise is to gather game data from at least 1000 different games. After the data has been gathered, Inverse Reinforcement Learning algorithms will be applied  with the hope of the agent learning to play the game from you, the experts :)

### INSTALLATION:
*Note: This distribution requires Python 3.*
1. If you would like to use a virtual environment (which I highly recommend), and you don't have it installed, follow the instuctions in the text file labelled "Virtual_Environment.txt" in the folder Help_Files.
2. Clone or download this repo.
3. Run the following command:

   $ python setup.py install

4. If everything went well, you should have all the necessary libraries installed and you can now play the game using the following command:

   $ python play.py

### CONTROLS:
The controls are the standard WASD for movement, however you can use the arrow keys if you wish.
When you die, you can simply press the SPACE bar to restart, or Q to quit.

### INSTRUCTIONS:
Run the game using the command above, and survive for as long as you possibly can while eating as much food as possible. Try to play at least 10 games, but obviously the more you can play, the more helpful it will be. So take a break from your research, relax and play a few games of Snake.

When you're finished playing your games, email me a zipped version of the Data folder. Email: [matthewreynard24@gmail.com](mailto:matthewreynard24@gmail.com)

Thanks everyone, and happy gaming :)

### CHANGING THE DIFFICULTY
*Note: This is not a perfect game, it was thrown together very quickly with little thought of it going out to the public, just expect some bugs and some input lag as well. It is not an optimized game.*

If the snake is moving too fast or too slow for you, feel free to delve into the code and change the difficulty setting. I've tried to make it as easy as possible.

Developer tip: the input that is pressed last on each "tick" will be the action that is executed. Don't try and hold down buttons, this won't help, rather if you need to ensure a certain move is executed, spam the button as fast as you can.
