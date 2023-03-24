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

        # Getting the x and y coordinates from the givin position
        pos_x = pos[0]
        pos_y = pos[1]
        cell = None

        # Iterating through the dictonary of positions
        for list in self.game_positions.values():

            # Gripping the coordinates from each positions list
            for coordinates in list:
                
                coord_x = coordinates[0]
                coord_y = coordinates[1]
            
                # Checking if the range of the givin positions is in the range of any chess piece
                # We will do that by checking if the positions are in the range of the piece diameter
                x_range = (pos_x >= (coord_x - self.radius)) and (pos_x <= (coord_x + self.radius))
                y_range = (pos_y >= (coord_y - self.radius)) and (pos_y <= (coord_y + self.radius))

                if x_range and y_range:
                    cell = coordinates

        return cell


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
