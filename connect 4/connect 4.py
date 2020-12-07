import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0 :
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    #check horizontal locations
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True

    # vertical locations 
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True
    # positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True

    #negatively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True
board = create_board() 
# print (board) 
game_over = False
turn = 0
while not game_over:
    #ask player 1 move
    if turn == 0:
        col = int(input("player 1 move"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board,row, col, 1)

        if winning_move(board, 1):
            print("PLAYER 1 WINS")
            game_over = True


        # print (board)  
        print_board(board)   

    #ask player 2 move
    else:
        col = int(input("player 2 move"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board,row, col, 2)
        
        if winning_move(board, 2):
            print("PLAYER 2 WINS")
            game_over = True

        # print (board)   
        print_board(board)  

    turn += 1
    turn = turn % 2