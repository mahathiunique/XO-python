#board creation
def create_board():
    return [[str(i + 1) for i in range(j, j + 3)] for j in range(0, 9, 3)]

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

#Check for wins
def check_winner(board, mark):
    for row in board:
        if all([cell == mark for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == mark for row in range(3)]):
            return True
    if all([board[i][i] == mark for i in range(3)]) or all([board[i][2 - i] == mark for i in range(3)]):
        return True
    return False

# Check for a draw
def check_draw(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])

# Player's move
def make_move(board, moves, mark):
    for i in range(3):
        for j in range(3):
            if board[i][j] == moves:
                board[i][j] = mark
                return

# Chance left
def get_available_moves(board):
    return [cell for row in board for cell in row if cell not in ['X', 'O']]


import random

# The X or O game
def X_or_O():
    board = create_board()
    player = 'X'
    opponent = 'O'

    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and the opponent is 'O'.")
    
    while True:
# Player's move
        print("\nYour turn! moves available:")
        print_board(board)
        available_moves = get_available_moves(board)
        while True:
            move = input(f"Choose a position ({', '.join(available_moves)}): ")
            if move in available_moves:
                break
            print("Illegal move, please try again.")

        make_move(board, move, player)

        if check_winner(board, player):
            print("\n Bravo! You won!")
            print_board(board)
            break
        if check_draw(board):
            print("\nIt's a draw!")
            print_board(board)
            break

# Opponent's move
        print("\n Opponent's turn...")
        opponent_move = random.choice(get_available_moves(board))
        make_move(board, opponent_move, opponent)
        print(f"Opponent chose position {opponent_move}")

        if check_winner(board, opponent):
            print("\nOops! The opponent won.")
            print_board(board)
            break
        if check_draw(board):
            print("\nIt's a draw!")
            print_board(board)
            break

X_or_O()






