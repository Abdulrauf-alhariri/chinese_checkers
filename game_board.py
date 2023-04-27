"""importing the pygame module"""
# pylint: disable=no-member, undefined-variable, wildcard-import, unused-wildcard-import
import pygame as pg
from pygame.locals import *
#Initializing the pygame module




# pylint: disable=no-member,undefined-variable,wildcard-import
class GameBoard:

    """This class will be respobsible for the game settings"""
    def __init__(self, window_width=1180, window_heigt=800):
        self.radius = 15
        self.space_between_pieces = 5
        self.game_positions = {
            'hexagon': [],
            'red': [],
            'green': [],
            'blue': [],
            'orange': [],
            'white': [],
            'black': []
        }
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
        self.center_of_x_coordinates = (window_width// 2)
        self.center_of_y_coordinates = (window_heigt//2)


    def game_board_hexagon(self):
        """"This function will draw the base of the game board without the players """
        # Specifying the max number of columns that can be in a row
        nr_of_columns = 9
        player_type = "hexagon"
        coords = []

        # This variable will tell in which list of the different
        # types our cell is currently in
        list_type = player_type

        # The hexagon consists of nine rows where it follows the pattern 5-9-5 for the columnes
        #It means the first row starts with 5 columns
        # and it increase with 1 column for each next row
        # and when we hit row 5 with 9 columns it will reverse
        # with a 1 column decrease for each row
        for row in range(5):

            # Getting the coordinates of each cell
            for col in range(nr_of_columns):
                start_pos_x = ((self.center_of_x_coordinates -
                ((((self.radius*2+self.space_between_pieces) * nr_of_columns)//2) + self.radius))
                + (self.radius*2+self.space_between_pieces)*col)

                # Checking if we are in the middle row or not
                # in order to start the forward and backward iteration
                if row != 0:
                    # Y cords for rows > 5
                    start_pos_y_forward = (self.center_of_y_coordinates
                    + (self.radius*2+self.space_between_pieces)*row)

                    # Y cords for rows < 5
                    start_pos_y_backward = (self.center_of_y_coordinates
                    - (self.radius*2+self.space_between_pieces)*row)

                    # Adding the column coordinates to the lists
                    coords.append([start_pos_x, start_pos_y_backward,
                                   player_type, False, list_type])
                    coords.append([start_pos_x, start_pos_y_forward,
                                    player_type, False, list_type])



                else:
                    coords.append([start_pos_x, self.center_of_y_coordinates,
                                   player_type, False, list_type])



            # Decreasing the number if columns by each row
            nr_of_columns -= 1

        # Checking if the lists are not empty before adding them to the global coordinate list
        if len(coords) > 0:
            for coord in coords:
                self.game_positions[player_type].append(coord)

    def two_players(self):
        """This function will draw two players"""
        two_players_colors = ["red", "green"]


        for index in range(2):
            # Here is the type of the player and in wich list he is in
            player_type = two_players_colors[index]
            list_type = player_type

            nr_of_columns = 4
            for row in range(5, 9):
                # Getting the y coordinates
                if index == 0:
                    # Y cords for rows > 5
                    start_pos_y = (self.center_of_y_coordinates
                    + (self.radius*2+self.space_between_pieces)*row)
                else:
                    # Y cords for rows < 5
                    start_pos_y = (self.center_of_y_coordinates
                    - (self.radius*2+self.space_between_pieces)*row)

                for col in range(nr_of_columns):
                    # Getting the x coordinates
                    start_pos_x = ((self.center_of_x_coordinates -
                    ((((self.radius*2+self.space_between_pieces) * nr_of_columns)//2)
                    + self.radius)) + (self.radius*2+self.space_between_pieces)*col)


                    # Adding the coordinates to the object
                    self.game_positions[player_type].append([start_pos_x,
                    start_pos_y,player_type, False, list_type])

                nr_of_columns -= 1

    def four_players(self):
        """This function will be responsible for drawing 4 players"""

        # Drawing the first and second player
        self.two_players()
        four_players_colors = ["red", "green", "blue", "orange"]
        # Drawing the third and fourth player
        for index in range(2, 4):
            player_type = four_players_colors[index]
            list_type = player_type

            # Initializing the original columns on the second row of the hexagon
            nr_of_columns = 1
            hexagon_nr_of_columns = 8

            for row in range(1, 5):
                total_nr_of_columns = hexagon_nr_of_columns + (nr_of_columns*2)
                # Getting the y coordinates
                if index == 2:
                    # Y cords for rows > 5
                    start_pos_y = (self.center_of_y_coordinates
                    - (self.radius*2+self.space_between_pieces)*row)
                else:
                    # Y cords for rows < 5
                    start_pos_y = (self.center_of_y_coordinates
                    + (self.radius*2+self.space_between_pieces)*row)

                for col in range(nr_of_columns):

                    if index == 2:

                        # Getting the x coordinates
                        start_pos_x = (self.center_of_x_coordinates - (
                        (((self.radius*2+self.space_between_pieces) * total_nr_of_columns)//2)
                        + self.radius) + (self.radius*2+self.space_between_pieces)*col)



                        # Adding the coordinates to the object
                        self.game_positions[player_type].append([start_pos_x,
                        start_pos_y,player_type, False, list_type])

                    else:

                        start_pos_x = ((self.center_of_x_coordinates +
                        ((((self.radius*2+self.space_between_pieces) * total_nr_of_columns)//2)
                        + self.radius) - (self.radius*2+self.space_between_pieces)*col) - 65)





                        self.game_positions[player_type].append([start_pos_x,
                        start_pos_y,player_type, False, list_type])

                nr_of_columns += 1
                hexagon_nr_of_columns -= 1

    def sex_players(self):
        """This function will draw 6 players"""
        # Drawing the first 4 players
        self.four_players()
        sex_players_colors = ["red", "green", "blue", "orange", "white", "black"]
        # Drawing the fifth and sexth player
        for index in range(4, 6):
            player_type = sex_players_colors[index]
            list_type = player_type


            nr_of_columns = 1
            hexagon_nr_of_columns = 8

            for row in range(1, 5):
                total_nr_of_columns = hexagon_nr_of_columns + (nr_of_columns*2)

                if index == 4:
                    # Y cords for rows < 5
                    start_pos_y = (self.center_of_y_coordinates
                    - (self.radius*2+self.space_between_pieces)*row)
                else:
                    # Y cords for rows > 5
                    start_pos_y = (self.center_of_y_coordinates
                    + (self.radius*2+self.space_between_pieces)*row)

                for col in range(nr_of_columns):

                    if index == 4:

                        # Getting the x coordinates
                        start_pos_x = ((self.center_of_x_coordinates
                        + ((((self.radius*2+self.space_between_pieces) * total_nr_of_columns)//2)
                        + self.radius) - (self.radius*2+self.space_between_pieces)*col) -65)



                        # Adding the coordinates to the object
                        self.game_positions[player_type].append([start_pos_x,
                        start_pos_y, player_type, False, list_type])

                    else:

                        start_pos_x = (self.center_of_x_coordinates -
                        ((((self.radius*2+self.space_between_pieces) * total_nr_of_columns)//2)
                        + self.radius) + (self.radius*2+self.space_between_pieces)*col)


                        self.game_positions[player_type].append([start_pos_x,
                        start_pos_y, player_type, False, list_type])

                nr_of_columns += 1
                hexagon_nr_of_columns -= 1

    def update_game_board(self):
        """This function will update the game board after every move"""

        # Iterating through the coordinates dictionary, getting key and value
        for coord_list in self.game_positions.values():

            # Looping through the coordinates list
            for coordinates in coord_list:

                # Gets the positions and the color of the chess piece
                x_position = coordinates[0]
                y_position = coordinates[1]
                color = coordinates[2]

                # Checking if cell is active
                active = coordinates[3]


                # Getting the color as rgb
                if active:
                    color_rgb = (45, 177, 252)

                else:
                    color_rgb = self.colors[color]


                # Drawing the chess piece on its new position
                pg.draw.circle(self.window, color_rgb,
                [x_position, y_position], self.radius, 0)
