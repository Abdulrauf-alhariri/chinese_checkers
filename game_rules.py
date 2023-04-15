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
        self.possible_cells = []
        self.current_cell = None

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

    def detect_right_wing_moves(self, current_cell):
        """This function will detect the possible moves on the right side
        both behind and in front of the current cell
        """
        # Getting the front right cell
        back_right_cell = self.detect_possible_cells(current_cell)[0][1]
        right_cell = self.detect_possible_cells(current_cell)[1][1]
        front_right_cell = self.detect_possible_cells(current_cell)[2][1]

        current_front_right_cell = front_right_cell
        current_back_right_cell = back_right_cell

        front_detecter = False
        back_detecter = False
        detecter = False

         #This while loop will be responsible for finding the path
        #from the right side of the cell
        while not front_detecter :
            try:

                # Checking if the player can only move on step
                if current_front_right_cell[2] == "hexagon":
                    possible_cells = self.detect_possible_cells(current_front_right_cell)

                    front_right_cell = possible_cells[2][1]

                    # Here we check if this is a closed end where the player can not jump
                    # over the left and right cells after moving to the current position
                    if front_right_cell[2] == "hexagon":
                        self.possible_cells.append(current_front_right_cell)

                        front_detecter = True
                        
                    if front_right_cell[2] != "hexagon":

                        self.possible_cells.append(current_front_right_cell)
                        front_detecter = True


                # Checking if the right infron cell is not empty
                elif current_front_right_cell[2] != "hexagon":
                    # If it is not empty we check if we can jump over it
                    possible_cells = self.detect_possible_cells(current_front_right_cell)

                    front_right_cell = possible_cells[2][1]
                   

                    if front_right_cell[2] == "hexagon":
                        current_front_right_cell = front_right_cell

                    # Here we check if it is a closed end
                    elif front_right_cell[2] != "hexagon":
                        front_detecter = True

                
            #Here we accept TypeError in case right_cell or left_cell are equal to None
            except TypeError as err:

                print(err)
                break

        while not back_detecter:
            if current_back_right_cell[2] == "hexagon":
                possible_cells = self.detect_possible_cells(current_front_right_cell)

                back_right_cell = possible_cells[0][1]

                # Here we check if this is a closed end where the player can not jump
                # over the left and right cells after moving to the current position
                if back_right_cell[2] != "hexagon":

                    self.possible_cells.append(current_back_right_cell)
                    back_detecter = True

                if back_right_cell[2] == "hexagon":
                    self.possible_cells.append(current_back_right_cell)

                    back_detecter = True

            elif current_back_right_cell[2] != "hexagon":
                possible_cells = self.detect_possible_cells(current_front_right_cell)
                back_right_cell = possible_cells[0][1]

                if back_right_cell[2] != "hexagon":
                    back_detecter = True
                
                elif back_right_cell[2] == "hexagon":
                    current_back_right_cell = back_right_cell



        

    def detect_left_wing_moves(self, current_cell):
        """This function will detect the possible moves on the left side
        both behind and in front of the current cell
        """
        # Getting the fron left cell
        front_left_cell = self.detect_possible_cells(current_cell)[2][0]
        current_left_cell = front_left_cell

        

        
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

                        self.possible_cells.append(current_left_cell)
                        break

                    if front_left_cell[2] == "hexagon":
                        self.possible_cells.append(current_left_cell)

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


    def detect_possible_moves(self, pos):
        """This function will detect possible moves"""

        # Getting the current cell
        self.current_cell = self.detect_cell(pos)

        try:

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
                    cell_type = possible_cell[2]

                    # Getting the index of the possible cell in order to set it to active
                    cell_index = self.game_positions[cell_type].index(possible_cell)

                    # Setting the cell to possible move
                    self.game_positions[cell_type][cell_index][3] = True

                if len(self.possible_cells) > 0:
                    self.processing = True

        except TypeError as err:
            pass

    def move_cell(self, pos):
        """This function will move the current cell to the required position"""

        # Detecting the giving cell
        move_to_cell = self.detect_cell(pos)

        # Checking if the giving cell is among the possible cells
        if move_to_cell in self.possible_cells:
            
            # Iterating through the coordinates dictionary, getting key and value
            for list in self.game_positions.values():

                # Looping through the coordinates list
                for coordinates in list:

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
                cell_type = possible_cell[2]

                # Getting the index of the possible cell in order to set it to active
                cell_index = self.game_positions[cell_type].index(possible_cell)

                # Setting the cell to possible move
                self.game_positions[cell_type][cell_index][3] = False

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

