# importing the required libraries
import pygame as pg
import sys
import time
from pygame.locals import *

# creating all needed variables
XO = 'x'
winner = None
draw = None
width = 400
height = 400
white = (255, 255, 255)

# color of the straightlines on that white game board, dividing board into 9 parts
line_color = (0, 0, 0)

# using 3*3 board in canvas
board = [[None]*3, [None]*3, [None]*3]
pg.init()#initialize all imported pygame modules
fps = 30 #manual fps for faster gameplay used

# used to track time
CLOCK = pg.time.Clock()

# used to build the infra
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("Tic Tac Toe")

# loading the images as python object
starting_screen = pg.image.load("cover_page.png")
x_img = pg.image.load("image_'X'.png")
y_img = pg.image.load("image_'O'.png")
starting_screen = pg.transform.scale(starting_screen, (width, height + 100))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(y_img, (80, 80))

#button class for play again and quit buttons
class button:
    def __init__(self, x, y, width, height, text, color, text_color):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color
    
    def draw(self, surface):
        pg.draw.rect(surface, self.color, self.rect)
        pg.draw.rect(surface, (0, 0, 0), self.rect, 2)
        font = pg.font.Font(None, 24)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

#maikng custom modules to call on later
def game_starting_screen():
    
    screen.blit(starting_screen, (0, 0))
    
    pg.display.update()
    time.sleep(3)					
    screen.fill(white)

    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2), ( width, height / 3 * 2), 7)
    draw_status()

def draw_status():
    
    global draw
    
    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " won !"
    if draw:
        message = "Game Draw !"

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))
    
    # block at bottom of the main display
    screen.fill ((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center =(width / 2, 420))
    screen.blit(text, text_rect)
    pg.display.update()

def draw_game_over_buttons():
    play_again_btn = button(50, 450, 120, 40, "Play Again", (0, 200, 0), (255, 255, 255))
    quit_btn = button(230, 450, 120, 40, "Quit", (200, 0, 0), (255, 255, 255))
    
    play_again_btn.draw(screen)
    quit_btn.draw(screen)
    pg.display.update()
    
    return play_again_btn, quit_btn

#main game algo for checking wins
def check_win():
    global board, winner, draw

    # checking for wins
    for row in range(0, 3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board [row][0] is not None)):
            winner = board[row][0]
            pg.draw.line(screen, (250, 0, 0),
                                                (0, (row + 1)*height / 3 -height / 6),
                        (width, (row + 1)*height / 3 - height / 6 ),
                        4)
            break
    for col in range(0, 3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pg.draw.line (screen, (250, 0, 0), ((col + 1)* width / 3 - width / 6, 0), \
                        ((col + 1)* width / 3 - width / 6, height), 4)
            break

    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        
        winner = board[0][0]
        pg.draw.line (screen, (250, 70, 70), (50, 50), (350, 350), 4)
        
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        
        winner = board[0][2]
        pg.draw.line (screen, (250, 70, 70), (350, 50), (50, 350), 4)

    if(all([all(row) for row in board]) and winner is None ):
        draw = True

    draw_status()

def drawXO(row, col):
    global board, XO

        # for setting up image placement	 
    if row == 1:
        posx = 30
        
    if row == 2:
        posx = width / 3 + 30
        
    if row == 3:
        posx = width / 3 * 2 + 30

    if col == 1:
        posy = 30
        
    if col == 2:
        posy = height / 3 + 30
    
    if col == 3:
        posy = height / 3 * 2 + 30
        
    # value for display
    board[row-1][col-1] = XO
    
    if(XO == 'x'):
        screen.blit(x_img, (posy, posx))
        XO = 'o'
    
    else:
        screen.blit(o_img, (posy, posx))
        XO = 'x'
    pg.display.update()

def user_click():
    # get coordinates of mouse click
    x, y = pg.mouse.get_pos()

    if(x<width / 3):
        col = 1
    
    elif (x<width / 3 * 2):
        col = 2
    
    elif(x<width):
        col = 3
    
    else:
        col = None

    if(y<height / 3):
        row = 1
    
    elif (y<height / 3 * 2):
        row = 2
    
    elif(y<height):
        row = 3
    
    else:
        row = None

    # the desired positions
    if(row and col and board[row-1][col-1] is None):
        global XO

        drawXO(row, col)
        check_win()

#resetting game to play again 
def reset_game():
    global board, winner, XO, draw
    XO = 'x'
    draw = False
    game_starting_screen()
    winner = None
    board = [[None]*3, [None]*3, [None]*3]

game_starting_screen()

#main game loop
while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # Only detect left mouse button (1 = left, 2 = middle, 3 = right, 4 = scroll up, 5 = scroll down)
                if(winner or draw):
                    play_again_btn, quit_btn = draw_game_over_buttons()
                    if play_again_btn.is_clicked(event.pos):
                        reset_game()
                    elif quit_btn.is_clicked(event.pos):
                        pg.quit()
                        sys.exit()
                else:
                    user_click()

    if(winner or draw):
        draw_game_over_buttons()

    pg.display.update()
    CLOCK.tick(fps)