# Description of Tic-Tac-Toe Game

The game of Tic-Tac-Toe is a simple, two-player strategy game where players take turns placing their mark (either 'X' or 'O') on a 3x3 grid. The objective is to place three of their marks in a horizontal, vertical, or diagonal row before the opponent does. If all spaces are filled and no player has achieved this goal, the game results in a draw.

In this implementation, the player competes against an AI, where the player takes the first move with 'X' and the AI plays with 'O'. The game continues until a player wins or the game ends in a draw. The graphical interface for the game is created using the Tkinter library in Python.
Technologies and Algorithms Used

# Technologies:
  Python: The core programming language used for game logic and AI implementation.
    Tkinter: A Python library used to create the graphical user interface (GUI) of the game. It allows users to interact with buttons representing the Tic-Tac-Toe board.
# Algorithms:

Minimax Algorithm with Alpha-Beta Pruning:
        The AI player uses the Minimax algorithm to determine its optimal move. This algorithm evaluates all possible moves and their outcomes to maximize its own chances of winning while minimizing the player's chances.
        Alpha-Beta Pruning is employed to optimize the performance of the Minimax algorithm by cutting off branches in the game tree that cannot result in a better outcome. This helps reduce the number of nodes evaluated, making the AI faster and more efficient.

# Explanation of the code :
The provided code implements a Tic-Tac-Toe game where the user plays against an AI. The game uses the Tkinter library to create a graphical interface, allowing players to interact with a 3x3 grid of buttons representing the game board. The game alternates between the player (who plays as 'X') and the AI (who plays as 'O').

The **AI's logic** is based on the **Minimax algorithm with Alpha-Beta pruning**. The AI evaluates all possible moves and selects the best one by simulating future game states, ensuring it maximizes its chances of winning while minimizing the player's chances.

Key components:
- Player Moves: When the player clicks a button, their move is placed, and the game checks for a win or draw.
- AI Moves: The AI uses Minimax to compute the optimal move and places its mark ('O').
- Win Conditions: The game checks rows, columns, and diagonals to determine if either player has won or if the game is a draw.
- GUI: The game is visually represented with buttons in a window, and the game state is updated after each move.

The game continues until one player wins or all moves are exhausted, resulting in a draw.
