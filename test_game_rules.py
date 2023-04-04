"""Importing the necassary modules for the unit testing"""
import unittest
from game_rules import GameRules

test_game_rules = GameRules()

# Creating the game coordinates
test_game_rules.game_board_hexagon()
test_game_rules.sex_players()

# print(test_game_rules.game_positions)

class TestGameRules(unittest.TestCase):
    """This function will test the game rules class"""

    def test_detect_cell(self):
        """Here we test the detect_cell function"""
        # Creating a list with possible results
        possible_cells = [[558, 260, 'hexagon'], [715, 435, 'orange'],
        [435, 505,'black' ], [558, 610, 'red'], [435, 295, 'blue'], [767, 260, 'white']]


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





if __name__ == "__main__":
    unittest.main()
