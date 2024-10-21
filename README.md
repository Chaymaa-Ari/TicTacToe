# Description of Tic-Tac-Toe Game

The game of Tic-Tac-Toe is a simple, two-player strategy game where players take turns placing their mark (either 'X' or 'O') on a 3x3 grid. The objective is to place three of their marks in a horizontal, vertical, or diagonal row before the opponent does. If all spaces are filled and no player has achieved this goal, the game results in a draw.

In this implementation, the player competes against an AI, where the player takes the first move with 'X' and the AI plays with 'O'. The game continues until a player wins or the game ends in a draw. The graphical interface for the game is created using the Tkinter library in Python.
Technologies and Algorithms Used
1. Technologies:

    Python: The core programming language used for game logic and AI implementation.
    Tkinter: A Python library used to create the graphical user interface (GUI) of the game. It allows users to interact with buttons representing the Tic-Tac-Toe board.

2. Algorithms:

    Minimax Algorithm with Alpha-Beta Pruning:
        The AI player uses the Minimax algorithm to determine its optimal move. This algorithm evaluates all possible moves and their outcomes to maximize its own chances of winning while minimizing the player's chances.
        Alpha-Beta Pruning is employed to optimize the performance of the Minimax algorithm by cutting off branches in the game tree that cannot result in a better outcome. This helps reduce the number of nodes evaluated, making the AI faster and more efficient.
