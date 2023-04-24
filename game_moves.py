"""importing the pygame module"""
import pygame as pg
from pygame.locals import *
from game_board import GameBoard
import traceback



class GameMoves(GameBoard):
    """This function will contain all the ways about how
    a player can move"""

    def __init__(self):
        # Passing arguments to the child class
        super().__init__()

        self.possible_cells = []
        self.current_cell = None

    def back_right_cells(self, current_cell):
        """This function will detect the back possible right cells to move to"""

        back_right_cell = self.detect_possible_cells(current_cell)[0][1]
        current_back_right_cell = back_right_cell


        while current_back_right_cell:
            try:
                if current_back_right_cell[2] == "hexagon":
                    possible_cells = self.detect_possible_cells(current_back_right_cell)

                    back_right_cell = possible_cells[0][1]

                    # Here we check if this is a closed end where the player can not jump
                    # over the left and right cells after moving to the current position
                    # We also check that the type is not None

                    if back_right_cell:
                        if back_right_cell[2] != "hexagon":

                            self.possible_cells.append(current_back_right_cell)
                            break

                        if back_right_cell[2] == "hexagon":
                            self.possible_cells.append(current_back_right_cell)

                            break
                    else:
                        # If the type is none then that means that you just can make one move
                        self.possible_cells.append(current_back_right_cell)
                        break

                if current_back_right_cell[2] != "hexagon":
                    possible_cells = self.detect_possible_cells(current_back_right_cell)

                    back_right_cell = possible_cells[0][1]

                    # Checking that we do not get None as type
                    if back_right_cell:

                        if back_right_cell[2] == "hexagon":
                            current_back_right_cell = back_right_cell

                        elif back_right_cell[2] != "hexagon":
                            break


                    else:
                        break

            except TypeError:
                print(traceback.format_exc())
                break

    def back_left_cells(self, current_cell):
        """This function will detect the possible moves on the back left side of the current cell"""
        back_left_cell = self.detect_possible_cells(current_cell)[0][0]
        current_back_left_cell = back_left_cell


        while current_back_left_cell:
            try:
                if current_back_left_cell[2] == "hexagon":
                    possible_cells = self.detect_possible_cells(current_back_left_cell)

                    back_left_cell = possible_cells[0][0]

                    # Here we check if this is a closed end where the player can not jump
                    # over the left and right cells after moving to the current position
                    # We also check that the type is not None

                    if back_left_cell:
                        if back_left_cell[2] != "hexagon":

                            self.possible_cells.append(current_back_left_cell)
                            break

                        if back_left_cell[2] == "hexagon":
                            self.possible_cells.append(current_back_left_cell)

                            break
                    else:
                        # If the type is none then that means that you just can make one move
                        self.possible_cells.append(current_back_left_cell)
                        break

                if current_back_left_cell[2] != "hexagon":
                    possible_cells = self.detect_possible_cells(current_back_left_cell)

                    back_left_cell = possible_cells[0][0]

                    # Checking that we do not get None as type
                    if back_left_cell:

                        if back_left_cell[2] == "hexagon":
                            current_back_left_cell = back_left_cell

                        elif back_left_cell[2] != "hexagon":
                            break


                    else:
                        break

            except TypeError:
                print(traceback.format_exc())
                break

    def right_cells(self, current_cell):
        """This function will detect the cells right to the current cell"""

        # Getting the nearst cell on the right of the current cell
        right_cell = self.detect_possible_cells(current_cell)[1][1]
        current_right_cell = right_cell

        while current_right_cell:
            try:
                if current_right_cell[2] == "hexagon":
                    possible_cells = self.detect_possible_cells(current_right_cell)

                    right_cell = possible_cells[1][1]

                    # Here we check if this is a closed end where the player can not jump
                    # over the left and right cells after moving to the current position
                    # We also check that the type is not None

                    if right_cell:
                        if right_cell[2] != "hexagon":

                            self.possible_cells.append(current_right_cell)
                            break

                        if right_cell[2] == "hexagon":
                            self.possible_cells.append(current_right_cell)

                            break
                    else:
                        # If the type is none then that means that you just can make one move
                        self.possible_cells.append(current_right_cell)
                        break

                if current_right_cell[2] != "hexagon":
                    possible_cells = self.detect_possible_cells(current_right_cell)

                    right_cell = possible_cells[1][1]

                    # Checking that we do not get None as type
                    if right_cell:

                        if right_cell[2] == "hexagon":
                            current_right_cell = right_cell

                        elif right_cell[2] != "hexagon":
                            break

                    else:
                        break

            except TypeError:
                print(traceback.format_exc())
                break

    def left_cells(self, current_cell):
        """This function will detect the possible cells to move to 
        on the left of the current cell
        """

        #Getting the nearst cell on the left of the current cell
        left_cell = self.detect_possible_cells(current_cell)[1][0]
        current_left_cell = left_cell

        while current_left_cell:
            try:
                if current_left_cell[2] == "hexagon":
                    possible_cells = self.detect_possible_cells(current_left_cell)

                    left_cell = possible_cells[1][0]

                    # Here we check if this is a closed end where the player can not jump
                    # over the left and right cells after moving to the current position
                    # We also check that the type is not None

                    if left_cell:
                        if left_cell[2] != "hexagon":

                            self.possible_cells.append(current_left_cell)
                            break

                        if left_cell[2] == "hexagon":
                            self.possible_cells.append(current_left_cell)

                            break
                    else:
                        # If the type is none then that means that you just can make one move
                        self.possible_cells.append(current_left_cell)
                        break

                if current_left_cell[2] != "hexagon":
                    possible_cells = self.detect_possible_cells(current_left_cell)

                    left_cell = possible_cells[1][0]

                    # Checking that we do not get None as type
                    if left_cell:

                        if left_cell[2] == "hexagon":
                            current_left_cell = left_cell

                        elif left_cell[2] != "hexagon":
                            break

                    else:
                        break

            except TypeError:
                print(traceback.format_exc())
                break





    def detect_right_wing_moves(self, current_cell):
        """This function will detect the possible moves on the right side
        both behind and in front of the current cell
        """
        # Getting the front right cell
        front_right_cell = self.detect_possible_cells(current_cell)[2][1]

        current_front_right_cell = front_right_cell


        #This while loop will be responsible for finding the path
        #from the right side of the cell
        while current_front_right_cell:
            try:


                # Checking if the player can only move on step
                if current_front_right_cell[2] == "hexagon":
                    possible_cells = self.detect_possible_cells(current_front_right_cell)

                    front_right_cell = possible_cells[2][1]

                    # Here we check if this is a closed end where the player can not jump
                    # over the left and right cells after moving to the current position
                    # Checking so that the type is not None

                    if front_right_cell:
                        if front_right_cell[2] == "hexagon":
                            self.possible_cells.append(current_front_right_cell)

                            break

                        if front_right_cell[2] != "hexagon":

                            self.possible_cells.append(current_front_right_cell)
                            break
                    else:
                        self.possible_cells.append(current_front_right_cell)
                        break

                # Checking if the right infron cell is not empty
                elif current_front_right_cell[2] != "hexagon":
                    # If it is not empty we check if we can jump over it
                    possible_cells = self.detect_possible_cells(current_front_right_cell)

                    front_right_cell = possible_cells[2][1]

                   # Making sure that the type is not None
                    if front_right_cell:
                        if front_right_cell[2] == "hexagon":
                            current_front_right_cell = front_right_cell

                        # Here we check if it is a closed end
                        elif front_right_cell[2] != "hexagon":
                            break

                    else:
                        break


            #Here we accept TypeError in case right_cell or left_cell are equal to None
            except TypeError:

                print(traceback.format_exc())
                break

        self.back_right_cells(current_cell)
        self.right_cells(current_cell)

    def detect_left_wing_moves(self, current_cell):
        """This function will detect the possible moves on the left side
        both behind and in front of the current cell
        """
        # Getting the fron left cell
        front_left_cell = self.detect_possible_cells(current_cell)[2][0]
        current_front_left_cell = front_left_cell




        #This while loop will be responsible for finding the path
        #from the left side of the cell

        while True:
            try:

                # Checking if the player can only move on step
                if current_front_left_cell[2] == "hexagon":
                    possible_cells = self.detect_possible_cells(current_front_left_cell)

                    front_left_cell = possible_cells[2][0]

                    # Here we check if this is a closed end where the player can not jump
                    # over the left and left cells after moving to the current position
                    if front_left_cell:
                        if front_left_cell[2] != "hexagon":

                            self.possible_cells.append(current_front_left_cell)
                            break

                        if front_left_cell[2] == "hexagon":
                            self.possible_cells.append(current_front_left_cell)

                            break
                    else:
                        self.possible_cells.append(current_front_left_cell)
                        break

                # Checking if the left infron cell is not empty
                elif current_front_left_cell[2] != "hexagon":
                    # If it is not empty we check if we can jump over it
                    possible_cells = self.detect_possible_cells(current_front_left_cell)

                    front_left_cell = possible_cells[2][0]
                    # print(next_two_cells[1][2] == "hexagon")
                    # break
                    if front_left_cell:
                        if front_left_cell[2] == "hexagon":
                            current_front_left_cell = front_left_cell

                        # Here we check if it is a closed end
                        elif front_left_cell[2] != "hexagon":
                            break
                    else:
                        break

            #Here we accept TypeError in case left_cell or left_cell are equal to None
            except TypeError:

                print(traceback.format_exc())
                break

        self.back_left_cells(current_cell)
        self.left_cells(current_cell)
