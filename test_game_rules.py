"""Importing the necassary modules for the unit testing"""
import unittest
from game_rules import GameRules

test_game_rules = GameRules()

# Creating the game coordinates
test_game_rules.game_board_hexagon()
test_game_rules.sex_players()

# print(test_game_rules.game_positions)

class TestGameRules(unittest.TestCase):
    """This class will test the game rules class"""

    def test_detect_cell(self):
        """Here we test the detect_cell function"""
        # Creating a list with possible results
        possible_cells = [[558, 260, 'hexagon', False, "hexagon"], [715, 435, 'orange', False, "orange"],
        [435, 505,'black', False, "black" ], [558, 610, 'red', False, "red"], [435, 295, 'blue', False, "blue"], [767, 260, 'white', False, "white"]]


        # Creating a dynamic loop of tests
        for cell in possible_cells:
            cell_x = cell[0]
            cell_y = cell[1]

            start_r = 0
            end_r = 16

            for l in range(2):
                for r in range(start_r, end_r):
                    # Increasing the position in the circumference range
                    cell_x += r
                    cell_y += r

                    # Trying to detect if the givin position is to the current cell
                    result = test_game_rules.detect_cell([cell_x, cell_y])

                    self.assertEqual(result, cell)

                    # Here we are resetting the cell coordinates for the next loop
                    cell_x -= r
                    cell_y -= r

                # Changin the loop range to check to opposite side also
                start_r = -15
                end_r = 0

    def test_detect_possible_cells(self):
        # Here we have a list of current cells and
        # The cells that should surround them
        current_cells = [[540, 225, 'green', False, 'green'],
        [540, 575, 'red', False, 'red'], [715, 435, 'orange', False, 'orange']]

        possible_back_cells = [[[523, 190, 'green', False, 'green'], [558, 190, 'green', False, 'green']],
        [[523, 540, 'hexagon', False, 'hexagon'], [558, 540, 'hexagon', False, 'hexagon']],
        [[698, 400, 'hexagon', False, 'hexagon'], None]]

        possible_side_cells = [[[505, 225, 'green', False, 'green'], [575, 225, 'green', False, 'green']],
        [[505, 575, 'red', False, 'red'], [575, 575, 'red', False, 'red']],
        [[680, 435, 'hexagon', False, 'hexagon'], None]]

        possible_front_cells = [[[523, 260, 'hexagon', False, 'hexagon'], [558, 260, 'hexagon', False, 'hexagon']],
        [[523, 610, 'red', False, 'red'], [558, 610, 'red', False, 'red']],
        [[697, 470, 'orange', False, 'orange'], [732, 470, 'orange', False, 'orange']]]


        nr_current = 0

        # Looping through the current cells and getting each cell alone
        for current_cell in current_cells:
            # Getting the cells surrounded the current cell and then
            # comparing the results with the real results of our lists
            surrounded_cells = test_game_rules.detect_possible_cells(current_cell)

            self.assertEqual(surrounded_cells[0], possible_back_cells[nr_current])
            self.assertEqual(surrounded_cells[1], possible_side_cells[nr_current])
            self.assertEqual(surrounded_cells[2], possible_front_cells[nr_current])

            # Moving to the next current cell
            nr_current += 1

    def test_game_status(self):
        """This function will test game status in game rules class"""

        # First thing is to change the chess positions of a player
        # To make him win and take over someones territory
        # We choose the green player to make him win and take over red player territory

        players = ["green", "red", "black", "white", "blue", "orange"]

        for chess in test_game_rules.game_positions["red"]:
            # Changing the player in the territory
            chess[2] = "green"

        # Here we try the game status function
        # The function will return the winner and it will change
        # Game over to true
        resutl = test_game_rules.game_status(players)
        self.assertEqual(resutl, "green")
        self.assertEqual(test_game_rules.game_over, True)









if __name__ == "__main__":
    unittest.main()
