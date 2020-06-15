README
--------------
Gordian Bruns
CS365
Lab B - Adversarial Games
--------------

I. File List
 - environmentState.py  # contains EnvironmentState-class, display_state, terminal_test
 - main.py  # contains main, initial_state, transition _function, move_generator, create_tree, minimax, play_game
 - node.py  # contains Node-class for the tree, evasive, conqueror, balanced, distance, rusher, calculate_utility

Note that all files must be in the same directory.


II. Usage

The program takes five command line arguments:

	- rows
	- columns
	- rows_of_pawns
	- utility function for the white pawns (possible options: evasive, conqueror, balanced, rusher)
	- utility function for the black pawns (possible options: evasive, conqueror, balanced, rusher)

It creates an initial state and based on that, it will play a whole game automatically.
So, for example, if you want to let an AI with the utility function balanced play against an AI with the utility function evasive on an 8 x 8 board with two rows of pawns, then you have to enter the following into the command line:
python main.py 8 8 2 balanced evasive
It will then display the board after each move and tell you in the end who won.

The general format you must have to play a game is:
python main.py [rows] [columns] [rows_of_pawns] [whites_function] [blacks_function]

Note that rows > 0, columns > 0, rows_of_pawns > 0 and <= rows // 2, and whites_function and blacks_function must be in [evasive, conqueror, balanced, rusher]
