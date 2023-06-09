"""importing the pygame module"""
# pylint: disable=no-member, undefined-variable, wildcard-import, unused-wildcard-import
import traceback
import pygame as pg
from pygame.locals import *
from game_moves import GameMoves


class GameRules(GameMoves):

    """This class will determine the game rules"""
    def __init__(self):
        # Passing arguments to the child class
        super().__init__()

        self.game_over_status = False
        self.players = ["red", "green", "blue", "orange", "white", "black"]

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

    def detect_possible_moves(self, pos, turn):
        """This function will detect possible moves"""

        # Getting the current cell
        self.current_cell = self.detect_cell(pos)


        player_turn = self.players[turn]

        # Check that the givin position belongs to a player and not hexagon
        if self.current_cell and (self.current_cell[2] == player_turn):
            if self.current_cell[2] != "hexagon":


                # # detecting possible moves from the right
                self.detect_right_wing_moves(self.current_cell, self.detect_possible_cells)

                # # Detecting possible moves from the left
                self.detect_left_wing_moves(self.current_cell, self.detect_possible_cells)

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

            # This will return that the player made his move
            return True

        return None

    def game_status(self, current_players):
        """This function will be responsible on tracking the game status
        each time any player make a move this function will check if any
        player have won yet
        """

        # Getting the current player that are in the game


        # Looping through the players list and getting each player alone
        for player in current_players:

            # Getting the player territory
            territory = self.game_positions[player]
            game_over = True

            # Checking if the territory has been taken by any other player
            for chess in territory:
                player_type = chess[2]
                territory_type = chess[4]

                # Chcking if the territory is not fully taken yet
                if player_type == territory_type:
                    game_over = False

            # Checking if it is game over
            if game_over:
                self.game_over_status = True

                # Because all the positions have been colonized by the winner
                # So any random cell of them will give us the type of the winner
                winner = self.game_positions[player][0][2]

                # Returning the winer
                return winner

        return None
