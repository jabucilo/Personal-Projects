# Tetris - DYOA Advanced at TU Graz WS 2021
# Name:       YOUR_NAME
# Student ID: YOUR_STUDENT_ID

import pygame,random,sys
from framework import BaseGame

GAME_DIFFICULTY = 1 # number of simulated clicks when shuffling the gameboard

class Circle:
    def __init__(self, game, color):
        self.game = game #DONE set current game to access variables
        self.color_index = color #DONE set to color index (0 or 1) passed as method parameter
        self.color = self.game.circle_colors[self.color_index] #DONE Take correct color from circle_colors member dictionary in Basegame
        
    
    def swap_color(self):
        #DONE swap the color of the circle between the two possibilities (blue and yellow)
        if self.color_index == 0:
          self.color_index = 1
          self.color = self.game.circle_colors[self.color_index]
        else:
          self.color_index = 0
          self.color = self.game.circle_colors[self.color_index]


class Game(BaseGame):
    #starts the current level according to the correct set circle_count
    def start_level(self):
          #DONE get a new empty self.gameboard, fill it with circles and shuffle the gameboard
        self.gameboard = self.get_empty_board()
        self.fill_gameboard()
        self.shuffle_gameboard()

        #GameLoop
        while not self.check_level_solved():
            self.draw_game_board()
            # --------------------
            # BEGIN Student Logic
            
            #DONE check for mouse button press, get the correct circle and swap the colors of all necessary circles
            try:
              key_pressed = self.check_key_press()
              coords = self.select_circle(key_pressed)
              self.swap_circle_colors(coords)
            #DONE count clicks
              self.clicks += 1

            except TypeError:
              pass

            # END Student Logic
            # --------------------
            self.draw_level()
            self.draw_clicks()
            pygame.display.update()


    # fills gameboard with circles in one color of your choice
    # returns nothing, just adapts self.gameboard
    def fill_gameboard(self):
        #DONE implement logic according to comments and assignment description
        for row_indx in range(self.circle_count):
          for circle_indx in range(self.circle_count):
            self.gameboard[row_indx][circle_indx] = Circle(self, 0)


    # emulate clicks on the gameboard and swap the colors to make sure every level is solvable
    # returns nothing, just adapts self.gameboard
    def shuffle_gameboard(self):
        #DONE implement logic according to comments and assignment description
        for i in range(GAME_DIFFICULTY):
          random_pos = (random.choice(range(self.circle_count)), random.choice(range(self.circle_count)))
          self.swap_circle_colors(random_pos)


    # Logic to swap all circles in a diagonal pattern (X) from the clicked circle
    # returns nothing, just adapts self.gameboard
    def swap_circle_colors(self, pos):
        #DONE implement logic according to comments and assignment description
        x, y = pos
        
        # clicked circle, to compensate for when the left and right meet
        self.gameboard[y][x].swap_color()
        
        # swaps color for 2 circles per row
        for row_indx in range(self.circle_count):
          left = x - (row_indx - y)
          right = x + (row_indx - y)
          
          if len(self.gameboard[row_indx]) > left >= 0:
              self.gameboard[row_indx][left].swap_color()

          if len(self.gameboard[row_indx]) > right >= 0:
              self.gameboard[row_indx][right].swap_color()


    # checks if the level is solved (all circles have the same color)
    # if solved return True, False otherwise
    def check_level_solved(self):
        #DONE implement logic according to comments and assignment description
        first_circle = self.gameboard[0][0].color_index

        # compares every circle on the board with circle(0,0)
        for row in self.gameboard:
          for circle in row:
            if circle.color_index != first_circle:
              return False
        
        return True


# create main loop for up to 13 circles in a row
# reset clicks for each level and increase number of cicles before starting level
def main(game):
    #TODO implement logic according to comments and assignment description
    running = True
    while running:
      game.start_level()
      game.clicks = 0
      game.circle_count += 1
      if game.circle_count > 13:
        running = False


#-------------------------------------------------------------------------------------
# Do not modify the code below, your implementation should be done above
#-------------------------------------------------------------------------------------
def init():
    pygame.init()
    game = Game()
    game.clicks = 0
    main(game)

if __name__ == '__main__':
    init()