"""importing the pygame module"""
# pylint: disable=no-member, undefined-variable, wildcard-import, unused-wildcard-import
import traceback
from pygame.locals import *
from game_board import GameBoard



class GameMoves(GameBoard):
    """This function will contain all the ways about how
    a player can move"""

    def __init__(self):
        # Passing arguments to the child class
        super().__init__()

        self.possible_cells = []
        self.current_cell = None

    def cell_detecter(self, func_detect_possible_cells, c_cell, dir_coords):
        """This function will detect cells that the current cell
        can move to accourding to which direction we are looking for"""

       
        list_in_possible_cells = dir_coords[0]
        cell_type = dir_coords[1]

        cell = func_detect_possible_cells(c_cell)[list_in_possible_cells][cell_type]
        current_cell = cell
        process = True

        while current_cell and process:
            try:
                if current_cell[2] == "hexagon":
                    possible_cells = func_detect_possible_cells(current_cell)

                    cell = possible_cells[list_in_possible_cells][cell_type]

                    # Here we check if this is a closed end where the player can not jump
                    # over the left and right cells after moving to the current position
                    # We also check that the type is not None
                    duration = 1
                    while cell:
                        if cell[2] == "hexagon" and duration == 1:

                            self.possible_cells.append(current_cell)
                            process = False
                            break

                        if cell[2] == "hexagon" and duration >= 1:
                            self.possible_cells.append(cell)
                            process = False
                            break

                        if cell[2] != "hexagon" and duration >=2 :
                            self.possible_cells.append(current_cell)
                            process = False
                            break


                        if cell[2] != "hexagon":
                            cell = (func_detect_possible_cells(cell)
                                    [list_in_possible_cells][cell_type])

                        duration +=1
                    else:
                        # If the type is none then that means that you just can make one move
                        self.possible_cells.append(current_cell)
                        process = False
                        break

                if current_cell[2] != "hexagon":
                    possible_cells = func_detect_possible_cells(current_cell)

                    cell = possible_cells[list_in_possible_cells][cell_type]

                    # Checking that we do not get None as type
                    if cell:

                        if cell[2] == "hexagon":
                            current_cell = cell

                        elif cell[2] != "hexagon":
                            break

                    else:
                        break

            except TypeError:
                print(traceback.format_exc())
                break

    def detect_right_wing_moves(self, current_cell,func_detect_possible_cells ):
        """This function will detect the possible moves on the right side
        both behind and in front of the current cell
        """

        self.cell_detecter(func_detect_possible_cells, current_cell, [0,1])
        self.cell_detecter(func_detect_possible_cells, current_cell, [1,1])
        self.cell_detecter(func_detect_possible_cells, current_cell, [2,1])

    def detect_left_wing_moves(self, current_cell, func_detect_possible_cells):
        """This function will detect the possible moves on the left side
        both behind and in front of the current cell
        """

        self.cell_detecter(func_detect_possible_cells, current_cell, [0,0])
        self.cell_detecter(func_detect_possible_cells, current_cell, [1,0])
        self.cell_detecter(func_detect_possible_cells, current_cell, [2,0])
