"""importing the pygame module"""
import pygame as pg
from pygame.locals import *
from game_board import GameBoard

#Initializing the pygame module
pg.init()

#Setting the window caption
pg.display.set_caption("Chinese checkers")

class GameRules(GameBoard):

    """This class will determine the game rules"""
    def __init__(self, width, length):
        # Passing arguments to the child class
        super().__init__(width, length)

        self.processing = False
        self.run = True

    def detect_cell(self, pos):
        """
        The purpose of this function is to detect which cell 
        the player wants to move according to the given positions
        """

        print(pos)




    def run_game(self):
        self.window.fill((252, 207, 121, 255))

        self.game_board_hexagon()
        self.sex_players()

        # The game loop will be running until the status of the run variable become false
        while self.run:

            # Getting the mouse position 
            mouse_pos = pg.mouse.get_pos()
            for event in pg.event.get():

                if event.type == QUIT:
                    self.run = False
                
                # Checking if the game board has been clicked
                if event.type == pg.MOUSEBUTTONDOWN:

                    if not self.processing: 
                        self.detect_cell(mouse_pos)




            pg.display.update()

        # Closing the playing window
        pg.quit()

if __name__ == "__main__":
    set_up = GameRules(1180, 800)
    set_up.run_game()
