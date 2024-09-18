def create_board():
    return [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")
def check_winner(board, mark):
    for row in board:
        if all([cell == mark for cell in row]):
            return True
    for column in range(3):
        if all([board[row][column] == mark for row in range(3)]):
            return True
    if all([board[i][i] == mark for i in range(3)]) or all([board[i][2 - i] == mark for i in range(3)]):
        return True
    return False
def check_draw(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])
def make_move(board, moves, mark):
    for i in range(3):
        for j in range(3):
            if board[i][j] == moves:
                board[i][j] = mark
                return
def get_available_moves(board):
    return [cell for row in board for cell in row if cell not in ['X', 'O']]

import random
def X_or_O():
    board = create_board()
    player = 'X'
    opponent = 'O'
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and the opponent is 'O'.")
    while True:
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
