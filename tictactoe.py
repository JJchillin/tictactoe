import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = WIDTH // 9
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
CIRCLE_COLOR = (78, 245, 66)
CROSS_COLOR = (0, 245, 238)
BACKGROUND_COLOR = (242, 245, 66)
LINE_COLOR = (255, 0, 0)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE' )
screen.fill( BACKGROUND_COLOR )

#board
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )


def draw_lines():
	#horizontal lines
	pygame.draw.line( screen, LINE_COLOR, (0, WIDTH // 3), (HEIGHT, WIDTH // 3), LINE_WIDTH )
	pygame.draw.line( screen, LINE_COLOR, (0, 2 * WIDTH // 3), (HEIGHT, 2 * WIDTH // 3), LINE_WIDTH )
	#vertical lines
	pygame.draw.line( screen, LINE_COLOR, (HEIGHT // 3, 0), (HEIGHT // 3, WIDTH), LINE_WIDTH )
	pygame.draw.line( screen, LINE_COLOR, (2 * HEIGHT // 3, 0), (2 * HEIGHT // 3, WIDTH), LINE_WIDTH )

def draw_figures():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 1:
				pygame.draw.line( screen, CROSS_COLOR, ( col * HEIGHT // 3 + SPACE, row * WIDTH // 3 + WIDTH // 3 - SPACE), (col * HEIGHT // 3 + HEIGHT // 3 - SPACE, row * WIDTH // 3 + SPACE), CROSS_WIDTH )
				pygame.draw.line( screen, CROSS_COLOR, ( col * HEIGHT // 3 + SPACE, row * WIDTH // 3 + SPACE), (col * HEIGHT // 3 + HEIGHT // 3 - SPACE, row * WIDTH // 3 + WIDTH // 3 - SPACE), CROSS_WIDTH )
			if board[row][col] == 2:
				pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * (HEIGHT // 3) + HEIGHT // 6), int( row * (WIDTH // 3) + WIDTH // 6)), CIRCLE_RADIUS, CIRCLE_WIDTH )

def mark_square(row, col, player):
	board[row][col] = player

def available_square(row, col):
	return board[row][col] == 0

def is_board_full():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 0:
				return False
	return True

def check_win(player):
	#check columns
	for col in range(BOARD_COLS):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			draw_vertical_winning_line(col, player)
			return True

	#check rows
	for row in range(BOARD_ROWS):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_horizontal_winning_line(row, player)
			return True

	#check ascending diagonal
	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		draw_ascending_diagonal(player)
		return True

	#check descending diagonal
	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		draw_descending_diagonal(player)
		return True

	return False

def draw_vertical_winning_line(col, player):
	posX = col * HEIGHT // 3 + HEIGHT // 6
	if player == 1:
		color = CROSS_COLOR
	else:
		color = CIRCLE_COLOR

	pygame.draw.line( screen, color, (posX, LINE_WIDTH), (posX, HEIGHT - LINE_WIDTH), LINE_WIDTH )

def draw_horizontal_winning_line(row, player):
	posY = row * WIDTH // 3 + WIDTH // 6

	if player == 1:
		color = CROSS_COLOR
	else:
		color = CIRCLE_COLOR

	pygame.draw.line( screen, color, (LINE_WIDTH, posY), (WIDTH - LINE_WIDTH, posY), LINE_WIDTH )

def draw_ascending_diagonal(player):
	if player == 1:
		color = CROSS_COLOR
	else:
		color = CIRCLE_COLOR

	pygame.draw.line( screen, color, (LINE_WIDTH, HEIGHT - LINE_WIDTH), (WIDTH - LINE_WIDTH, LINE_WIDTH), LINE_WIDTH )

def draw_descending_diagonal(player):
	if player == 1:
		color = CROSS_COLOR
	else:
		color = CIRCLE_COLOR

	pygame.draw.line( screen, color, (LINE_WIDTH, LINE_WIDTH), (WIDTH - LINE_WIDTH, HEIGHT - LINE_WIDTH), LINE_WIDTH )

def restart():
	screen.fill( BACKGROUND_COLOR )
	draw_lines()
	player = 1
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			board[row][col] = 0

draw_lines()

player = 1
game_over = False
#main loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN and not game_over:


			mouseX = event.pos[0] # x
			mouseY = event.pos[1] # y

			clicked_row = int(mouseY // (WIDTH // 3))
			clicked_col = int(mouseX // (HEIGHT // 3))
			

			if available_square( clicked_row, clicked_col ):
				if player == 1:
					mark_square( clicked_row, clicked_col, 1 )
					if check_win(player):
						game_over = True;
					player = 2
				else:
					mark_square( clicked_row, clicked_col, 2 )
					if check_win(player):
						game_over = True;
					player = 1

				draw_figures()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				restart()


	pygame.display.update()