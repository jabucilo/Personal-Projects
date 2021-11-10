import pygame,sys
from pygame.locals import *

class BaseGame:
    def __init__(self):
        self.colors = {  
                    'white'     : (255,255,255),
                    'gray'      : (185,185,185),
                    'black'     : (  0,  0,  0),
                    'blue'      : (  0,  0,255),
                    'yellow'    : (255,247,  0),
                }
        
        self.circle_colors = [self.colors['blue'], self.colors['yellow']]
        self.border_color = self.colors['white']
        self.background = self.colors['black']
        self.text_color = self.colors['white']
        self.window_width = 600
        self.window_height = 600 
        self.circle_size = 40
        self.circle_count = 4
        self.margin = int((self.window_width - self.circle_count * self.circle_size) / 2)
        self.display = 0
        self.font = pygame.font.Font('freesansbold.ttf', 18)
        self.clicks = 0
        self.gameboard = []

        self.display = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption('Diagonal')
        self.show_text('Diagonal')
    
    def get_empty_board(self):
        board = []
        for i in range(self.circle_count):
            board.append([None] * self.circle_count)
        return board

    def draw_game_board(self):
        self.display.fill(self.background)
        self.margin = int((self.window_width - self.circle_count * self.circle_size) / 2)
        pygame.draw.rect(self.display, self.border_color, (
            self.margin-1, self.margin-1, (self.circle_count * (self.circle_size))+2,
            (self.circle_count * (self.circle_size))+2), 5)
        pygame.draw.rect(self.display, self.background,
                         (self.margin, self.margin, (self.circle_size) * self.circle_count, (self.circle_size) * self.circle_count))
        for x in range(self.circle_count):
            for y in range(self.circle_count):
                self.draw_circles(x, y, self.gameboard[y][x])

    def convert_coords(self, board_x, board_y):
        return (self.margin + (board_x * self.circle_size)), (self.margin + (board_y * self.circle_size))

    def draw_circles(self, x, y, circle):
        if circle.color == ".":
            return
        x_,y_ = self.convert_coords(x,y)
        pygame.draw.circle(self.display, circle.color, (x_ + self.circle_size/2, y_ + self.circle_size/2), self.circle_size/2)

    def select_circle(self, coords):
        for x in range(self.circle_count):
            for y in range(self.circle_count):
                x_,y_ = self.convert_coords(x,y)
                if coords[0] >= x_ and coords[0] <= x_ + self.circle_size:
                    if coords[1] >= y_ and coords[1] <= y_ + self.circle_size:
                        return (x,y)

    def test_quit_game(self):
        for event in pygame.event.get(QUIT):
            pygame.quit()
            sys.exit()
        for event in pygame.event.get(KEYDOWN): # get all the KEYUP events
            if event.key == K_ESCAPE or event.key == K_q:
                pygame.quit()
                sys.exit()
            pygame.event.post(event)

    def check_key_press(self):
        self.test_quit_game()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                return event.pos
        return None

    def draw_clicks(self):
        score = self.font.render('Clicks: {}'.format(self.clicks), True, self.colors['white'])
        rect = score.get_rect()
        rect.topleft = (100, 5)
        self.display.blit(score, rect)
        
    def draw_level(self):
        text = self.font.render('Level: {}'.format(self.circle_count-4), True, self.colors['white'])
        rect = text.get_rect()
        rect.topleft = (300, 5)
        self.display.blit(text, rect)

    def show_text(self, msg):
        displ = self.font.render(msg, True, self.colors['gray'])
        rect = displ.get_rect()

        rect.center = (int(self.window_width / 2), int(self.window_height / 2))
        self.display.blit(displ, rect) 

        displ = self.font.render(msg, True, self.colors['white'])
        rect = displ.get_rect()

        rect.center = (int(self.window_width / 2) - 2, int(self.window_height / 2) - 2)
        self.display.blit(displ, rect) 

        while self.check_key_press() == None:
            self.display_update()

    def display_update(self):
        pygame.display.update()