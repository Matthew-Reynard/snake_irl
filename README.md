# snake_irl
Snake game used to gather game data for IRL

---

### LIBRARIES USED:
virtualenv (helpful, but not necessary)  
numpy  
pygame  
pandas  
click

### ABOUT:
This is the snake game with a fixed grid size of 8x8 and the aim of this exercise is to gather game data from at least 1000 different games. After the data has been gathered, Inverse Reinforcement Learning algorithms will be applied with the hope of the agent learning to play the game from you, the experts :)

![Snake Game Image](https://raw.githubusercontent.com/Matthew-Reynard/snake_irl/master/Images/snake_irl.png)

### INSTALLATION:
*Note: This distribution requires Python 3.*
1. If you would like to use a virtual environment (which I highly recommend), and you don't have virtualenv installed, follow the instructions in the text file labelled "Virtual_Environment.txt" in the Help_Files folder and after you are done, continue with step 2.
2. Clone or download this repo into your project directory.
3. Run the following command:
   ```
   $ pip install --editable .
   ```
4. If everything went well, you should have all the necessary libraries installed and you can now play the game using the following command:
   ```
   $ play
   ```
   The default difficulty of the game is set to Medium. You can change the difficulty using the option -d or --difficulty with the arguments "easy", "medium", "hard" or "insane":

   e.g.
   ```
   $ play -d insane
   ```
   The following command will provide you with more details should you need it.
   ```
   $ play --help 
   ```
5. After playing a few games, if you want to watch your games in a specific log file, run the following command with the log file number as the argument:
   ```
   $ replay -n LOG_FILE_NUMBER
   ```
   e.g.
   ```
   $ replay -n 0
   ```
   If you forget to input a file number, you will be prompted at the start of the program.

   The following command will provide you with more details should you need it.
   ```
   $ replay --help 
   ```
### CONTROLS:
The controls are the standard WASD for movement, however you can use the arrow keys if you wish.
When you die, you can simply press the SPACE bar to restart, or Q to quit.

### INSTRUCTIONS:
Run the game using the command above, and survive for as long as you possibly can while eating as much food as possible. Try to play at least 10 games, but obviously the more you can play, the more helpful it will be. So take a break from your research, relax and play a few games of Snake.

When you're finished playing your games, email me a zipped version of the Data folder.  
(email: [matthewreynard24@gmail.com](mailto:matthewreynard24@gmail.com))

Thanks everyone, and happy gaming :)

### ATTENTION:
*Note: This is not a perfect game, it was thrown together very quickly with little thought of it going out to the public, just expect some bugs and some input lag as well. It is not an optimized game.*
