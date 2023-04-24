"""importing the pygame module"""
import traceback
import pygame as pg
from pygame.locals import *
from game_moves import GameMoves

#Initializing the pygame module
pg.init()

#Setting the window caption
pg.display.set_caption("Chinese checkers")

class GameRules(GameMoves):

    """This class will determine the game rules"""
    def __init__(self):
        # Passing arguments to the child class
        super().__init__()

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
        for coord_list in self.game_positions.values():

            # Gripping the coordinates from each positions list
            for coordinates in coord_list:


                coord_x = coordinates[0]
                coord_y = coordinates[1]
                x_range = False


                # Checking if the range of the givin positions is in the range of any chess piece
                #We will do that by checking if the positions are in the range of the piece diameter
                # x_range = (coord_x + self.radius) >= pos >= (coord_x - self.radius)

                # First variable checks if the position is greater then the beginning of the circle
                # Second variable checks if it is smaller than the end of the circle
                x_start = pos_x >= (coord_x - self.radius)
                x_end = pos_x <= (coord_x + self.radius)

                y_start = pos_y >= (coord_y - self.radius)
                y_end = pos_y <= (coord_y + self.radius)

                x_range = x_start and x_end
                y_range = y_start and y_end

                if x_range and y_range:
                    cell = coordinates
                    break


        return cell

    def detect_possible_cells(self, current_cell):
        """This functoin will detect the two cells in front of the current cell"""

        # Cells behind the current cell
        right_behind_cell = None
        left_behind_cell = None

        # Cells on the right and left sides of the current cell
        right_cell = None
        left_cell = None

        # Cells in front of the current cell
        right_front_cell = None
        left_front_cell = None


        # Check the two cells in front of the current cell
        for index in range(2):

            try:
                x_pos = None

                # Y-axel positions in front of the current cell and behind the current cell
                y_pos_behind = current_cell[1] - self.radius - self.space_between_pieces
                y_pos_front = current_cell[1] + self.radius + self.space_between_pieces
                y_pos_current = current_cell[1]


                # We check the next cell to the right, 0 represent the right cell
                if index == 0:
                    x_pos = current_cell[0] + self.radius + self.space_between_pieces

                    # Getting the cells on the right of the current cell
                    right_front_cell = self.detect_cell([x_pos, y_pos_front])
                    right_behind_cell = self.detect_cell([x_pos, y_pos_behind])
                    right_cell = self.detect_cell([x_pos, y_pos_current ])

                # The next cell to the left, 1 represent the left cell
                if index == 1:
                    x_pos = current_cell[0] - self.radius - self.space_between_pieces

                    # Getting the cells on the left of the current cell
                    left_front_cell = self.detect_cell([x_pos, y_pos_front])
                    left_behind_cell = self.detect_cell([x_pos, y_pos_behind])
                    left_cell = self.detect_cell([x_pos, y_pos_current])

            except TypeError:
                print(traceback.format_exc())

        # Returning the cells
        return [[left_behind_cell, right_behind_cell],
        [left_cell, right_cell], [left_front_cell, right_front_cell]]
    

    def detect_possible_moves(self, pos):
        """This function will detect possible moves"""

        # Getting the current cell
        self.current_cell = self.detect_cell(pos)
        print("current cell: ", self.current_cell)
        print("possible cells: ", self.detect_possible_cells(self.current_cell))




        # Check that the givin position belongs to a player and not hexagon
        if self.current_cell[2] != "hexagon":


            # detecting possible moves from the right
            self.detect_right_wing_moves(self.current_cell)

            # Detecting possible moves from the left
            self.detect_left_wing_moves(self.current_cell)


            # Looping through the possible cells to move to
            for possible_cell in self.possible_cells:

                # Getting the type of the cell in order to get all the cells with
                # Same type
                cell_list_type = possible_cell[4]

                # Getting the index of the possible cell in order to set it to active
                cell_index = self.game_positions[cell_list_type].index(possible_cell)


                # Setting the cell to possible move
                self.game_positions[cell_list_type][cell_index][3] = True

            if len(self.possible_cells) > 0:
                self.processing = True


    def move_cell(self, pos):
        """This function will move the current cell to the required position"""

        # Detecting the giving cell
        move_to_cell = self.detect_cell(pos)

        # Checking if the giving cell is among the possible cells
        if move_to_cell in self.possible_cells:

            # Iterating through the coordinates dictionary, getting key and value
            for coord_list in self.game_positions.values():

                # Looping through the coordinates list
                for coordinates in coord_list:

                    if coordinates == move_to_cell:


                        # Changing the positions between the current cell and the got cell
                        coordinates[3] = False
                        coordinates[2] = self.current_cell[2]

                        self.current_cell[2] = "hexagon"


                        self.possible_cells.remove(move_to_cell)


            # Resetting the possible cells to unactive
            # Looping through the possible cells to move to
            for possible_cell in self.possible_cells:

                # Getting the type of the cell in order to get all the cells with
                # Same type
                cell_list_type = possible_cell[4]

                # Getting the index of the possible cell in order to set it to active
                cell_index = self.game_positions[cell_list_type].index(possible_cell)

                # Setting the cell to possible move
                self.game_positions[cell_list_type][cell_index][3] = False

            # Resetting the posibble cells list to default
            self.possible_cells = []
            self.processing = False


    def run_game(self):
        self.window.fill((252, 207, 121, 255))

        self.game_board_hexagon()
        self.sex_players()
        self.detect_cell([559, 261])


        # The game loop will be running until the status of the run variable become false
        while self.run:

            # Getting the mouse position
            mouse_pos = pg.mouse.get_pos()
            for event in pg.event.get():

                if event.type == QUIT:
                    self.run = False

                # Checking if the game board has been clicked
                if event.type == pg.MOUSEBUTTONDOWN:

                    # Checking if the player do not have any possible cells to move to yet
                    if not self.processing:
                        self.detect_possible_moves(mouse_pos)

                    else:
                        self.move_cell(mouse_pos)





            self.update_game_board()
            pg.display.update()

        # Closing the playing window
        pg.quit()

if __name__ == "__main__":
    set_up = GameRules()
    set_up.run_game()
