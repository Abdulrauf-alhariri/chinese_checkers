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
        self.hexagon_cords = []
        self.radius = 15
        self.players_positions = {
            'red': [],
            'green': [],
            'blue': [],
            'yellow': [],
            'white': [],
            'black': []
        }

        #Setting the size of the pygame window
        self.window_width = window_width
        self.window_heigt = window_heigt
        self.window = pg.display.set_mode((self.window_width, self.window_heigt))

        # Specifying the center coordinates of the window, in order to centralize the game board
        self.start_x = (self.window_width// 2)
        self.start_y = (self.window_heigt//2)


    def game_board_hexagon(self):
        """"This function will draw the base of the game board without the players """
        # Specifying the max number of columns that can be in a row
        nr_of_columns = 9

        # The hexagon consists of nine rows where it follows the pattern 5-9-5 for the columnes
        #It means the first row starts with 5 columns
        # and it increase with 1 column for each next row
        # and when we hit row 5 with 9 columns it will reverse
        # with a 1 column decrease for each row
        for row in range(5):
            backward_cords = []
            forward_cords = []
            middle_cords = []

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
                    backward_cords.append([start_pos_x, start_pos_y_backward])
                    forward_cords.append([start_pos_x, start_pos_y_forward])


                    pg.draw.circle(self.window, (255, 255, 255),
                    [start_pos_x, start_pos_y_backward], self.radius, 0)
                    pg.draw.circle(self.window, (255, 255, 255),
                    [start_pos_x, start_pos_y_forward], self.radius, 0)

                else:
                    middle_cords.append([start_pos_x, self.start_y])
                    pg.draw.circle(self.window, (255, 255,255),
                    [start_pos_x, self.start_y], self.radius, 0)

            # Checking if the lists are not empty before adding them to the global coordinate list
            if len(middle_cords) > 0:
                self.hexagon_cords.append(middle_cords)

            else:
                # If the middle cords list is empty so that means
                # that we are not in the middle row anymore
                # so the backward and forward lists should be full
                self.hexagon_cords.append(backward_cords)
                self.hexagon_cords.append(forward_cords)

            # Decreasing the number if columns by each row
            nr_of_columns -= 1

    def game_players(self, nr_of_players):
        """"This function will be responsible for drawing the players corners of the game board """

        players_colors = [['red', (235, 14, 14)], ['green', (38, 189, 53)], 
        ['blue', (66, 78, 245)], ['yellow', (227, 223, 14)], ['white', (255, 255, 255)], ['black', (0,0,0)]]
        # Drawing the players positions according to the number of players

        if nr_of_players >= 2:
            for index in range(2):
                player_color = players_colors[index]
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
                        pg.draw.circle(self.window, player_color[1],
                        [start_pos_x, start_pos_y], self.radius, 0)

                        # Adding the coordinates to the object
                        self.players_positions[player_color[0]].append([start_pos_x, start_pos_y, player_color[0]])

                    nr_of_columns -= 1
     
        elif nr_of_players == (3, 4):
            pass
        else:
            pass

        print(self.players_positions)



    def run_game(self):
        """ This function will be respobsible for the game loop"""

        self.window.fill((252, 207, 121, 255))
        self.game_board_hexagon()
        self.game_players(2)

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
