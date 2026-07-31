import numpy as np
import pygame
import sys
import math
import random
# from tkinter import *


pygame.init()

icon=pygame.image.load("/Users/maxnguyen/Downloads/logo.png")
pygame.display.set_icon(icon)
time=1800
PLAYER_1= (255,0,0)
PLAYER_2 = (50,205,50)
grey=(128,128,128)
d_grey=(169,169,169)
white=(220,220,220)
black=(0,0,0)
green=(124,252,0)
d_green=(0,200,0)
red=(255,0,0)
d_red=(200,0,0)
orange=(255,99,71)
purple=(139,0,139)
PIECE = (255,255,255)
BG = (0,0,205)

ROW_COUNT = 6
COLUMN_COUNT = 7

SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)

width = COLUMN_COUNT*SQUARESIZE
height = (ROW_COUNT+1)*SQUARESIZE
btnw=width/3
btnh=height/12
size = (width, height)
screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont("monospace",75)
btnfont = pygame.font.SysFont("monospace",30)

PLAYER = 0
AI = 1

EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2
WINDOW_LENGTH = 4

def quit():
    pygame.quit()
    sys.exit()

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

board=create_board()

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0 :
            return r

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

def text(msg,w,h,s,color):
    font=pygame.font.SysFont("monospace",s)
    label = font.render(msg,True,color)
    textRect = label.get_rect()
    textRect.center=(w,h)
    screen.blit(label,textRect)

def btn(msg,x,y,w,h,ic,ac,color,action=None):
    btn = btnfont.render(msg,True,color)
    btnRect = btn.get_rect()
    btnRect.center=((x+(w/2)),(y+(h/2)))
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(screen,ac,(x,y,w,h))
            if click[0]==1 and action != None :
                action()
    else:
            pygame.draw.rect(screen,ic,(x,y,w,h))
            
    screen.blit(btn,btnRect)

def btnai(msg,x,y,w,h,ic,ac,color,i,action=None):
    btn = btnfont.render(msg,True,color)
    btnRect = btn.get_rect()
    btnRect.center=((x+(w/2)),(y+(h/2)))
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(screen,ac,(x,y,w,h))
            if click[0]==1 and action != None :
                action(i)
    else:
            pygame.draw.rect(screen,ic,(x,y,w,h))
            
    screen.blit(btn,btnRect)

def intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.fill(white)
        pygame.display.set_caption("Connect 4")
        text("Connect 4",width/2,height/5,80,black)
        btn("VS Player",230,250,btnw,btnh,d_grey,grey,black,game)
        btn("VS AI",230,400,btnw,btnh,d_grey,grey,black,intro_ai)
        btn("Quit",230,550,btnw,btnh,d_red,red,white,quit)

        pygame.display.update()

def intro_ai():
    introai=True
    
    while introai:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.fill(white)
        text("Connect 4",width/2,height/5,80,black)
        btnai("Easy",230,250,btnw,btnh,d_grey,grey,black,1,AI_game)
        btnai("Normal",230,350,btnw,btnh,d_grey,grey,black,2,AI_game)
        btnai("Hard",230,450,btnw,btnh,d_grey,grey,black,4,AI_game)
        btnai("Very hard",230,550,btnw,btnh,d_grey,grey,black,5,AI_game)
        btn("Back",10,550,btnw/2,btnh/2,d_red,red,white,intro)
        pygame.display.update()

def win_screen(win_text,color):
    endscreen=True
    while endscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.fill(white)
        text(win_text,width/2,height/4,70,color)
        btn("Play Again",100,280,btnw,btnh,d_grey,grey,black,game)
        btn("Main Menu",365,280,btnw,btnh,d_red,red,white,intro)
        pygame.display.update()

def win_screen_ai(win_text,color,x):
    endscreen=True
    while endscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.fill(white)
        text(win_text,width/2,height/4,70,color)
        btnai("Play Again",100,280,btnw,btnh,d_grey,grey,black,x,AI_game)
        btn("Difficulty",365,280,btnw,btnh,d_grey,grey,black,intro_ai)
        btn("Main Menu",230,480,btnw,btnh,d_red,red,white,intro)
        pygame.display.update()

# def popup():
#     popup = Tk()
#     popup.title("Over!!!")
#     label=Label(popup,text="Game over!!!",font=norm_font)
#     label.pack(fill="both")
#     b1 = Button(popup,text="OK",command=popup.destroy)
#     b1.pack()
#     popup.mainloop()


# def cr():
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 quit()
#         screen.fill(white)
#         text("Connect 4",width/2,height/5,80)
        
#         pygame.display.update()

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen,BG, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen,PIECE, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS )
            
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):    
            if board[r][c] == 1 :
                pygame.draw.circle(screen,PLAYER_1, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS )
            elif board[r][c] == 2: 
                pygame.draw.circle(screen,PLAYER_2, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS )
    pygame.display.update()

def evaluate_window(window, piece):
	score = 0
	opp_piece = PLAYER_PIECE
	if piece == PLAYER_PIECE:
		opp_piece = AI_PIECE

	if window.count(piece) == 4:
		score += 100
	elif window.count(piece) == 3 and window.count(EMPTY) == 1:
		score += 5
	elif window.count(piece) == 2 and window.count(EMPTY) == 2:
		score += 2

	if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
		score -= 4

	return score

def score_position(board, piece):
	score = 0

	## Score center column
	center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
	center_count = center_array.count(piece)
	score += center_count * 3

	## Score Horizontal
	for r in range(ROW_COUNT):
		row_array = [int(i) for i in list(board[r,:])]
		for c in range(COLUMN_COUNT-3):
			window = row_array[c:c+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	## Score Vertical
	for c in range(COLUMN_COUNT):
		col_array = [int(i) for i in list(board[:,c])]
		for r in range(ROW_COUNT-3):
			window = col_array[r:r+WINDOW_LENGTH]
			score += evaluate_window(window, piece)

	## Score posiive sloped diagonal
	for r in range(ROW_COUNT-3):
		for c in range(COLUMN_COUNT-3):
			window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	for r in range(ROW_COUNT-3):
		for c in range(COLUMN_COUNT-3):
			window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
			score += evaluate_window(window, piece)

	return score

def is_terminal_node(board):
	return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0

def minimax(board, depth, alpha, beta, maximizingPlayer):
	valid_locations = get_valid_locations(board)
	is_terminal = is_terminal_node(board)
	if depth == 0 or is_terminal:
		if is_terminal:
			if winning_move(board, AI_PIECE):
				return (None, 1000000000000000)
			elif winning_move(board, PLAYER_PIECE):
				return (None, -10000000000000)
			else: # Game is over, no more valid moves
				return (None, 0)
		else: # Depth is zero
			return (None, score_position(board, AI_PIECE))
	if maximizingPlayer:
		value = -math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = get_next_open_row(board, col)
			b_copy = board.copy()
			drop_piece(b_copy, row, col, AI_PIECE)
			new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
			if new_score > value:
				value = new_score
				column = col
			alpha = max(alpha, value)
			if alpha >= beta:
				break
		return column, value

	else: # Minimizing player
		value = math.inf
		column = random.choice(valid_locations)
		for col in valid_locations:
			row = get_next_open_row(board, col)
			b_copy = board.copy()
			drop_piece(b_copy, row, col, PLAYER_PIECE)
			new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
			if new_score < value:
				value = new_score
				column = col
			beta = min(beta, value)
			if alpha >= beta:
				break
		return column, value

def get_valid_locations(board):
	valid_locations = []
	for col in range(COLUMN_COUNT):
		if is_valid_location(board, col):
			valid_locations.append(col)
	return valid_locations

def pick_best_move(board, piece):

	valid_locations = get_valid_locations(board)
	best_score = -10000
	best_col = random.choice(valid_locations)
	for col in valid_locations:
		row = get_next_open_row(board, col)
		temp_board = board.copy()
		drop_piece(temp_board, row, col, piece)
		score = score_position(temp_board, piece)
		if score > best_score:
			best_score = score
			best_col = col

	return best_col



def AI_game(x):
    board=create_board()
    game_over = False
    turn = random.randint(PLAYER, AI)
    while not game_over:
        draw_board(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, white, (0,0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == PLAYER:
                    pygame.draw.circle(screen, PLAYER_1, (posx, int(SQUARESIZE/2)), RADIUS)

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, white, (0,0, width, SQUARESIZE))
                # Ask for Player 1 Input
                if turn == PLAYER:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, PLAYER_PIECE)

                        if winning_move(board, PLAYER_PIECE):
                            win=1
                            label = myfont.render("Player 1 wins!!", 1, PLAYER_1)
                            screen.blit(label, (40,10))
                            game_over = True

                        turn += 1
                        turn = turn % 2

                        draw_board(board)


        # # Ask for Player 2 Input
        if turn == AI and not game_over:				

            col, minimax_score = minimax(board, x, -math.inf, math.inf, True)

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)

                if winning_move(board, AI_PIECE):
                    win=2
                    label = myfont.render("AI wins!!", 1, PLAYER_2)
                    screen.blit(label, (40,10))
                    game_over = True

                draw_board(board)

                turn += 1
                turn = turn % 2

        if game_over:
            pygame.time.wait(time)
            if win==1:
                win_screen_ai("PLAYER 1 WIN!!!",PLAYER_1,x)
            if win==2:
                win_screen_ai("AI WIN!!!",PLAYER_2,x)



def game():
    board=create_board()
    turn = 0
    game_over = False
    while not game_over:
        draw_board(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, white,(0,0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, PLAYER_1, (posx, int(SQUARESIZE/2)),RADIUS)  
                else:
                    pygame.draw.circle(screen, PLAYER_2, (posx, int(SQUARESIZE/2)),RADIUS)
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, white,(0,0, width, SQUARESIZE))
                #ask player 1 move
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board,row, col, 1)

                    if winning_move(board, 1):
                        win=1
                        label = myfont.render("PLAYER 1 WIN",1,PLAYER_1)
                        screen.blit(label,(40,10))
                        game_over = True

                    draw_board(board)   

                #ask player 2 move
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board,row, col, 2)
                
                    if winning_move(board, 2):
                        win=2
                        label = myfont.render("PLAYER 2 WIN",1,PLAYER_2)
                        screen.blit(label,(40,10))
                        game_over = True
                # row = get_next_open_row(board,col)
                # if is_valid_location(board, col)==False and row==None:
                #     win=3
                #     label = myfont.render("DRAW!!!",1,PLAYER_2)
                #     screen.blit(label,(40,10))
                #     game_over = True

                draw_board(board)
                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(time)
                    if win==1:
                        win_screen("PLAYER 1 WIN!!!",PLAYER_1)
                    if win==2:
                        win_screen("PLAYER 2 WIN!!!",PLAYER_2)
                    # else:
                    #     win_screen("DRAW!!!",PLAYER_1)


intro()