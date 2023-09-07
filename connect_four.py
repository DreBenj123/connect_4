import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, peice):
    # check hoizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if (
                board[r][c] == peice
                and board[r][c + 1] == peice
                and board[r][c + 2] == peice
                and board[r][c + 3] == peice
            ):
                return True
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if (
                board[r][c] == peice
                and board[r + 1][c] == peice
                and board[r + 2][c] == peice
                and board[r + 3][c] == peice
            ):
                board = create_board()
                print_board(board)


game_over = False
turn = 0

# Player 1 input
while not game_over:
    if turn == 0:
        col = int(input("Player 1 Make Your Selection (0-6):"))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

            if winning_move(board, 1):
                print("Player 1 Wins!")
                game_over = True

    # Player 2 input
    else:
        col = int(input("Player 2 Make Your Selection (0-6):"))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            if winning_move(board, 2):
                print("Player 2 Wins!")
                game_over = True
    print_board(board)
    turn += 1
    turn = turn % 2
