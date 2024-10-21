import tkinter as tk
import math

# Initialize the board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Check for a win condition
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Check if there are moves left
def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

# Evaluate the board to give scores
def evaluate(board):
    if check_winner(board, 'O'):  # AI wins
        return 10
    elif check_winner(board, 'X'):  # Human wins
        return -10
    return 0  # No winner

# Minimax function with alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)

    if score == 10 or score == -10:  # AI or Human won
        return score

    if not is_moves_left(board):  # It's a draw
        return 0

    if is_maximizing:  # AI's move
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = max(best, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = ' '
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best

    else:  # Human's move
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = ' '
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

# Find the best move for AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'  # AI move
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '  # Undo move

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Create the GUI for the game
class TicTacToeGame:
    def __init__(self, root):
        self.board = initialize_board()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.resizable(False, False)  # Make window non-resizable
        self.human_turn = True
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=' ', font=('Arial', 40), height=2, width=5,
                                   bg="#f0f0f0", activebackground="#d3d3d3",
                                   command=lambda i=i, j=j: self.human_move(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

    def human_move(self, row, col):
        if self.human_turn and self.board[row][col] == ' ':
            self.board[row][col] = 'X'
            self.buttons[row][col].config(text='X', fg="blue")  # X color
            if check_winner(self.board, 'X'):
                self.end_game("You win!")
                return
            self.human_turn = False
            # Delay before AI's move
            self.root.after(1000, self.ai_move)  # Delay in milliseconds (1000 ms = 1 second)

    def ai_move(self):
        if is_moves_left(self.board):
            row, col = find_best_move(self.board)
            self.board[row][col] = 'O'
            self.buttons[row][col].config(text='O', fg="red")  # O color
            if check_winner(self.board, 'O'):
                self.end_game("AI wins!")
                return
            self.human_turn = True

        if not is_moves_left(self.board):
            self.end_game("It's a draw!")

    def end_game(self, result):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state=tk.DISABLED)
        
        # Create a new top-level window for the result
        result_window = tk.Toplevel(self.root)
        result_window.title("Game Over")
        result_window.geometry("300x200")  # Set the size of the window

# Center the window
        screen_width = result_window.winfo_screenwidth()
        screen_height = result_window.winfo_screenheight()
        x = (screen_width // 2) - (300 // 2)  # Center x
        y = (screen_height // 2) - (200 // 2)  # Center y
        result_window.geometry(f"300x200+{x}+{y}")  # Update position

        result_window.configure(bg="#f0f0f0")  # Set background color

# Display the result message
        result_label = tk.Label(result_window, text=result, font=('Arial', 20), bg="#f0f0f0")
        result_label.pack(pady=10)

# Create a rounded button using Canvas
        button_canvas = tk.Canvas(result_window, width=150, height=50, bg="white", highlightthickness=0)
        button_canvas.pack(pady=10)

# Change button rectangle color to blue
        button_canvas.create_rectangle(0, 0, 150, 50, fill="#007BFF", outline="white")  # Blue background

# Add button text
        button_canvas.create_text(75, 25, text="Restart", fill="white", font=('Arial', 15))

# Bind click event to the canvas
        button_canvas.bind("<Button-1>", lambda e: self.restart_game(result_window))


    def restart_game(self, result_window):
        self.board = initialize_board()
        self.human_turn = True
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ', state=tk.NORMAL)
        result_window.destroy()  # Close the result window

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
