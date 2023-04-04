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

        # if pos_x > 558 and pos_y > 260:
        #     cell = [558, 260, 'hexagon']

        # Iterating through the dictonary of positions
        for list in self.game_positions.values():

            # Gripping the coordinates from each positions list
            for coordinates in list:


                coord_x = coordinates[0]
                coord_y = coordinates[1]
                x_range = False


                # Checking if the range of the givin positions is in the range of any chess piece
                #We will do that by checking if the positions are in the range of the piece diameter
                x_range = (pos_x >= (coord_x - self.radius)) and (pos_x <= (coord_x + self.radius))
                y_range = (pos_y >= (coord_y - self.radius)) and (pos_y <= (coord_y + self.radius))

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

            except Exception as e:
                print(e)

        # Returning the cells
        return [[left_behind_cell, right_behind_cell], [left_cell, right_cell], [left_front_cell, right_front_cell]]



    def detect_possible_moves(self, pos):
        """This function will detect possible moves"""

        # Getting the current cell
        current_cell = self.detect_cell(pos)
        front_right_cell = self.detect_possible_cells(current_cell)[2][1]
        front_left_cell = self.detect_possible_cells(current_cell)[2][0]

        print(self.detect_possible_cells(current_cell))
        current_right_cell = front_right_cell
        current_left_cell = front_left_cell


        possible_moves = []


        #This while loop will be responsible for finding the path
        #from the right side of the cell
        while True:
            try:

                # Checking if the player can only move on step
                if current_right_cell[2] == "hexagon":
                    possible_cells = self.detect_possible_cells(current_right_cell)

                    front_right_cell = possible_cells[2][1]

                    # Here we check if this is a closed end where the player can not jump
                    # over the left and right cells after moving to the current position
                    if front_right_cell[2] != "hexagon":

                        possible_moves.append(current_right_cell)
                        break

                    if front_right_cell[2] == "hexagon":
                        possible_moves.append(current_right_cell)

                        break

                # Checking if the right infron cell is not empty
                elif current_right_cell[2] != "hexagon":
                    # If it is not empty we check if we can jump over it
                    possible_cells = self.detect_possible_cells(current_right_cell)

                    front_right_cell = possible_cells[2][1]
                    # print(next_two_cells[1][2] == "hexagon")
                    # break

                    if front_right_cell[2] == "hexagon":
                        current_right_cell = front_right_cell

                    # Here we check if it is a closed end
                    elif front_right_cell[2] != "hexagon":
                        break

            #Here we accept TypeError in case right_cell or left_cell are equal to None
            except TypeError as err:

                print(err)
                break



        #This while loop will be responsible for finding the path
        #from the left side of the cell

        while True:
            try:

                # Checking if the player can only move on step
                if current_left_cell[2] == "hexagon":
                    possible_cells = self.detect_possible_cells(current_left_cell)

                    front_left_cell = possible_cells[2][0]

                    # Here we check if this is a closed end where the player can not jump
                    # over the left and left cells after moving to the current position
                    if front_left_cell[2] != "hexagon":

                        possible_moves.append(current_left_cell)
                        break

                    if front_left_cell[2] == "hexagon":
                        possible_moves.append(current_left_cell)

                        break

                # Checking if the left infron cell is not empty
                elif current_left_cell[2] != "hexagon":
                    # If it is not empty we check if we can jump over it
                    possible_cells = self.detect_possible_cells(current_left_cell)

                    front_left_cell = possible_cells[2][0]
                    # print(next_two_cells[1][2] == "hexagon")
                    # break

                    if front_left_cell[2] == "hexagon":
                        current_left_cell = front_left_cell

                    # Here we check if it is a closed end
                    elif front_left_cell[2] != "hexagon":
                        break

            #Here we accept TypeError in case left_cell or left_cell are equal to None
            except TypeError as err:

                print(err)
                break


        print(possible_moves)










    def run_game(self):
        self.window.fill((252, 207, 121, 255))

        self.game_board_hexagon()
        self.sex_players()
        self.update_game_board()
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

                    if not self.processing:
                        self.detect_possible_moves(mouse_pos)




            pg.display.update()

        # Closing the playing window
        pg.quit()

if __name__ == "__main__":
    set_up = GameRules()
    set_up.run_game()

