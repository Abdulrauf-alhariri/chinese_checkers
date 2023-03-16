"""importing the pygame module"""
import pygame as pg
from pygame.locals import *
#Initializing the pygame module
pg.init()

#Setting the window caption
pg.display.set_caption("Chinese checkers")




# pylint: disable=no-member,undefined-variable,wildcard-import
class GameBoard:

    """This class will be respobsible for the game settings"""
    def __init__(self, window_width, window_heigt):
        self.run = True
        self.radius = 15
        self.game_positions = {
            'hexagon': [],
            'red': [],
            'green': [],
            'blue': [],
            'orange': [],
            'white': [],
            'black': []
        }

        # self.colors = [['red', (235, 14, 14)], ['green', (38, 189, 53)],
        # ['blue', (66, 78, 245)], ['orange', (209, 103, 27)],
        # ['white', (255, 255, 255)], ['black', (0,0,0)], ['hexagon', (175, 179, 176)]]

        self.colors = {
            "red": (235, 14, 14),
            "green": (38, 189, 53),
            "blue": (66, 78, 245),
            "orange":  (209, 103, 27),
            "white": (255, 255, 255),
            "black": (0,0,0),
            "hexagon": (175, 179, 176)
        }
        self.window = pg.display.set_mode((window_width,window_heigt))

        # Specifying the center coordinates of the window, in order to centralize the game board
        self.start_x = (window_width// 2)
        self.start_y = (window_heigt//2)


    def game_board_hexagon(self):
        """"This function will draw the base of the game board without the players """
        # Specifying the max number of columns that can be in a row
        nr_of_columns = 9
        hexagon_color_rgb = self.colors['hexagon']
        hexagon_color = "hexagon"
        coords = []

        # The hexagon consists of nine rows where it follows the pattern 5-9-5 for the columnes
        #It means the first row starts with 5 columns
        # and it increase with 1 column for each next row
        # and when we hit row 5 with 9 columns it will reverse
        # with a 1 column decrease for each row
        for row in range(5):

            # Getting the coordinates of each cell
            for col in range(nr_of_columns):
                start_pos_x = (self.start_x - ((((self.radius*2+5) * nr_of_columns)//2)
                + self.radius)) + (self.radius*2+5)*col

                # Checking if we are in the middle row or not
                # in order to start the forward and backward iteration
                if row != 0:
                    start_pos_y_forward = self.start_y + (self.radius*2+5)*row
                    start_pos_y_backward = self.start_y - (self.radius*2+5)*row

                    # Adding the column coordinates to the lists
                    coords.append([start_pos_x, start_pos_y_backward,hexagon_color])
                    coords.append([start_pos_x, start_pos_y_forward,hexagon_color])


                    pg.draw.circle(self.window, hexagon_color_rgb,
                    [start_pos_x, start_pos_y_backward], self.radius, 0)
                    pg.draw.circle(self.window, hexagon_color_rgb,
                    [start_pos_x, start_pos_y_forward], self.radius, 0)

                else:
                    coords.append([start_pos_x, self.start_y,hexagon_color])
                    pg.draw.circle(self.window, hexagon_color_rgb,
                    [start_pos_x, self.start_y], self.radius, 0)


            # Decreasing the number if columns by each row
            nr_of_columns -= 1

        # Checking if the lists are not empty before adding them to the global coordinate list
        if len(coords) > 0:
            for coord in coords:
                self.game_positions["hexagon"].append(coord)

    def two_players(self):
        """This function will draw two players"""
        two_players_colors = ["red", "green"]


        for index in range(2):
            player_color = two_players_colors[index]
            player_color_rgb = self.colors[player_color]
            nr_of_columns = 4
            for row in range(5, 9):
                # Getting the y coordinates
                if index == 0:
                    start_pos_y = self.start_y + (self.radius*2+5)*row
                else:
                    start_pos_y = self.start_y - (self.radius*2+5)*row
                for col in range(nr_of_columns):
                    # Getting the x coordinates
                    start_pos_x = (self.start_x - ((((self.radius*2+5) * nr_of_columns)//2)
                    + self.radius)) + (self.radius*2+5)*col

                    # Drawing the checkers
                    pg.draw.circle(self.window, player_color_rgb,
                    [start_pos_x, start_pos_y], self.radius, 0)

                    # Adding the coordinates to the object
                    self.game_positions[player_color].append([start_pos_x,
                    start_pos_y, player_color])

                nr_of_columns -= 1

    def four_players(self):
        """This function will be responsible for drawing 4 players"""

        # Drawing the first and second player
        self.two_players()
        four_players_colors = ["red", "green", "blue", "orange"]
        # Drawing the third and fourth player
        for index in range(2, 4):
            player_color = four_players_colors[index]
            player_color_rgb = self.colors[player_color]
            # Initializing the original columns on the second row of the hexagon
            nr_of_columns = 1
            hexagon_nr_of_columns = 8

            for row in range(1, 5):
                total_nr_of_columns = hexagon_nr_of_columns + (nr_of_columns*2)
                # Getting the y coordinates
                if index == 2:
                    start_pos_y = self.start_y - (self.radius*2+5)*row
                else:
                    start_pos_y = self.start_y + (self.radius*2+5)*row

                for col in range(nr_of_columns):

                    if index == 2:

                        # Getting the x coordinates
                        start_pos_x = self.start_x - ((((self.radius*2+5) *
                        total_nr_of_columns)//2) + self.radius) + (self.radius*2+5)*col


                        # Drawing the checkers
                        pg.draw.circle(self.window, player_color_rgb,
                        [start_pos_x, start_pos_y], self.radius, 0)

                        # Adding the coordinates to the object
                        self.game_positions[player_color].append([start_pos_x,
                        start_pos_y, player_color])

                    else:

                        start_pos_x = (self.start_x + ((((self.radius*2+5) *
                        total_nr_of_columns)//2) + self.radius) - (self.radius*2+5)*col) - 65


                        pg.draw.circle(self.window, player_color_rgb,
                        [start_pos_x, start_pos_y], self.radius, 0)


                        self.game_positions[player_color].append([start_pos_x,
                        start_pos_y, player_color])

                nr_of_columns += 1
                hexagon_nr_of_columns -= 1

    def sex_players(self):
        """This function will draw 6 players"""
        # Drawing the first 4 players
        self.four_players()
        sex_players_colors = ["red", "green", "blue", "orange", "white", "black"]
        # Drawing the fifth and sexth player
        for index in range(4, 6):
            player_color = sex_players_colors[index]
            player_color_rgb = self.colors[player_color]

            nr_of_columns = 1
            hexagon_nr_of_columns = 8

            for row in range(1, 5):
                total_nr_of_columns = hexagon_nr_of_columns + (nr_of_columns*2)

                if index == 4:
                    # Backwards
                    start_pos_y = self.start_y - (self.radius*2+5)*row
                else:
                    # Forwards
                    start_pos_y = self.start_y + (self.radius*2+5)*row

                for col in range(nr_of_columns):

                    if index == 4:

                        # Getting the x coordinates
                        start_pos_x = (self.start_x + ((((self.radius*2+5)
                        * total_nr_of_columns)//2) + self.radius) - (self.radius*2+5)*col) -65


                        # Drawing the checkers
                        pg.draw.circle(self.window, player_color_rgb,
                        [start_pos_x, start_pos_y], self.radius, 0)

                        # Adding the coordinates to the object
                        self.game_positions[player_color].append([start_pos_x,
                        start_pos_y, player_color])

                    else:

                        start_pos_x = self.start_x - ((((self.radius*2+5)
                        * total_nr_of_columns)//2) + self.radius) + (self.radius*2+5)*col

                        # Drawing the checkers
                        pg.draw.circle(self.window, player_color_rgb,
                        [start_pos_x, start_pos_y], self.radius, 0)


                        self.game_positions[player_color].append([start_pos_x,
                        start_pos_y, player_color])

                nr_of_columns += 1
                hexagon_nr_of_columns -= 1

    def update_game_board(self):
        """This function will update the game board after every move"""

        # Iterating through the coordinates dictionary, getting key and value
        for coordinates in self.game_positions.values():

            # Looping through the coordinates list
            for coordinate in coordinates:

                # Gets the positions and the color of the chess piece
                x_position = coordinate[0]
                y_position = coordinate[1]
                color = coordinate[2]

                # Getting the color as rgb
                color_rgb = self.colors[color]


                # Drawing the chess piece on its new position
                pg.draw.circle(self.window, color_rgb,
                [x_position, y_position], self.radius, 0)





    def run_game(self):
        """ This function will be respobsible for the game loop"""

        self.window.fill((252, 207, 121, 255))
        self.game_board_hexagon()
        self.sex_players()
        self.update_game_board()

        # The game loop will be running until the status of the run variable become false
        while self.run:
            for event in pg.event.get():
                if event.type == QUIT:
                    self.run = False



            pg.display.update()

        # Closing the playing window
        pg.quit()

if __name__ == "__main__":
    set_up = GameBoard(1180, 800)
    set_up.run_game()
