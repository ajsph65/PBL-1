import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QLabel, QComboBox, QSlider
from PyQt5.QtCore import Qt, QTimer
import math


# Constants (game symbols)
IA = "O"
PLAYER = "X"
EMPTY = " "


# Game logic
def possible_moves(board):
    # Return a list of all empty positions on the board
    moves = []
    for i in range(len(board)):
        if board[i] == EMPTY:
            moves.append(i)
    return moves

# Check if a player has 3 symbols in a line
def win(board, player):
    # All possible winning combinations
    lines = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    # Check if one line contains the same player symbol
    for l in lines:
        if board[l[0]] == board[l[1]] == board[l[2]] == player:
            return True
    return False

# Check if the board is full (no empty cells)
def draw(board):
    return EMPTY not in board


# Evaluate the board for the AI : positive score = good for AI, negative score = good for player
def evaluation(board):
    if win(board, IA): 
        return 1000
    if win(board, PLAYER): 
        return -1000
    score = 0
    lines = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for line in lines:
        line_values = [board[i] for i in line]
        if IA in line_values and PLAYER in line_values: 
            continue
        if line_values.count(IA) == 2: 
            score += 30
        elif line_values.count(IA) == 1: 
            score += 10
        elif line_values.count(PLAYER) == 2: 
            score -= 30
        elif line_values.count(PLAYER) == 1: 
            score -= 10
    return score


# Recursive algorithm that explores possible future moves
def minimax(board, depth, is_max):

    # stop condition, if depth reached or game finished
    if depth == 0 or win(board, IA) or win(board, PLAYER) or draw(board):
        return evaluation(board)
    if is_max:
        best = -math.inf
        for move in possible_moves(board):
            board[move] = IA
            best = max(best, minimax(board, depth-1, False))
            board[move] = EMPTY
        return best
    
    else:
        worst = math.inf
        for move in possible_moves(board):
            board[move] = PLAYER
            worst = min(worst, minimax(board, depth-1, True))
            board[move] = EMPTY
        return worst

# Find the best move with minimax
def best_move(board, depth, current_player=IA):
    if current_player == IA:
        best_score = -math.inf
    else:
        best_score = math.inf

    move = -1

# test every possible move
    for m in possible_moves(board):
        board[m] = current_player
        score = minimax(board, depth - 1, current_player == PLAYER)
        board[m] = EMPTY

        if current_player == IA:
            if score > best_score:
                best_score = score
                move = m
        else:
            if score < best_score:
                best_score = score
                move = m

    return move


# Interface PYQT5

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Morpion IA - Stylish GUI")
        self.setFixedSize(350,450)

        self.board = [EMPTY]*9
        self.buttons = []
        self.mode = "Player vs AI"
        self.depth = 3
        self.current_player = PLAYER
        self.timer = None

        self.init_ui()

# Create the interface
    def init_ui(self):
        layout = QVBoxLayout()

        self.status = QLabel("Choose a mode")
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setStyleSheet("font-size:16px; margin-bottom:10px")
        layout.addWidget(self.status)

    # Dropdown menu to select mode
        self.mode_box = QComboBox()
        self.mode_box.addItems(["Player vs Player","Player vs AI","AI vs AI"])
        self.mode_box.currentTextChanged.connect(self.change_mode)
        layout.addWidget(self.mode_box)

#label showing ai depth
        self.slider_label = QLabel(f"AI Depth: {self.depth}")
        layout.addWidget(self.slider_label)

#slider to change ai difficulty
        self.depth_slider = QSlider(Qt.Horizontal)
        self.depth_slider.setMinimum(1)
        self.depth_slider.setMaximum(9)
        self.depth_slider.setValue(self.depth)
        self.depth_slider.valueChanged.connect(self.change_depth)
        layout.addWidget(self.depth_slider)

#grid for the tic tac toe board
        grid = QGridLayout()
        for i in range(9):
            btn = QPushButton("")
            btn.setFixedSize(90,90)
            btn.setStyleSheet("font-size:28px")

            #when clicked, play in this cell
            btn.clicked.connect(lambda _, x=i: self.play(x))
            self.buttons.append(btn)
            grid.addWidget(btn, i//3, i%3)
        layout.addLayout(grid)

# reset button
        reset_btn = QPushButton("Reset")
        reset_btn.clicked.connect(self.reset)
        layout.addWidget(reset_btn)

        self.setLayout(layout)

# change game mode
    def change_mode(self, text):
        self.mode = text
        self.reset()


#change ai difficulty
    def change_depth(self, val):
        self.depth = val
        self.slider_label.setText(f"AI Depth: {val}")

    def play(self, pos):
        # ignore click if cell alreagy used
        if self.board[pos] != EMPTY: 
            return

#player vs player
        if self.mode == "Player vs Player":
            self.board[pos] = self.current_player
            self.buttons[pos].setText(self.current_player)
            if win(self.board, self.current_player):
                self.status.setText(f"{self.current_player} wins!")
                return
            if draw(self.board):
                self.status.setText("Draw !")
                return
            self.current_player = IA if self.current_player==PLAYER else PLAYER

#player vs ia

        elif self.mode == "Player vs AI":
            #player move
            self.board[pos] = PLAYER
            self.buttons[pos].setText(PLAYER)
            if win(self.board, PLAYER):
                self.status.setText("You win !")
                return
            if draw(self.board):
                self.status.setText("Draw !")
                return
            
            # ai move
            ai = best_move(self.board, self.depth, IA)
            if ai!=-1:
                self.board[ai] = IA
                self.buttons[ai].setText(IA)
            if win(self.board, IA):
                self.status.setText("AI wins !")
                return
            if draw(self.board):
                self.status.setText("Draw !")

        elif self.mode == "AI vs AI":
            self.run_ai_vs_ai()

  
    # AI VS AI
   
    def run_ai_vs_ai(self):
        # Prepare the grid and the timer
        if self.timer: 
            self.timer.stop()
            #reset board
        self.board = [EMPTY]*9
        for b in self.buttons: 
            b.setText("")
        self.status.setText("AI vs AI running...")
        self.current_player = PLAYER
        # timer makes the ai play every 300ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.ai_turn)
        self.timer.start(300)

# AI plays automatically
    def ai_turn(self):
        move = best_move(self.board, self.depth, self.current_player)
        if move == -1:
            self.timer.stop()
            self.status.setText("Draw !")
            return
        self.board[move] = self.current_player
        self.buttons[move].setText(self.current_player)

        if win(self.board, self.current_player):
            self.timer.stop()
            self.status.setText(f"{self.current_player} wins !")
            return
        if draw(self.board):
            self.timer.stop()
            self.status.setText("Draw !")
            return

        # Alternate IA
        self.current_player = IA if self.current_player==PLAYER else PLAYER

    # Reset
   
    def reset(self):
        if self.timer: 
            self.timer.stop()
        self.board = [EMPTY]*9
        self.current_player = PLAYER
        for b in self.buttons: 
            b.setText("")
        self.status.setText("New game")


# Start

app = QApplication(sys.argv)
game = TicTacToe()
game.show()
sys.exit(app.exec_())
