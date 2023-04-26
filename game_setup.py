"""importing the pygame module"""
import pygame as pg
from pygame.locals import *
from game_rules import GameRules

#Initializing the pygame module
pg.init()

#Setting the window caption
pg.display.set_caption("Chinese checkers")


class GameSetUp(GameRules):
    """This class will be responsible for setting together
    the whole game"""

    def __init__(self):
        super().__init__()
        self.processing = False
        self.run = True
        self.font = pg.font.SysFont("Georgia", 30)
        self.play = False
        self.players_nr = None

    def draw_text(self, text, color, x_pos, y_pos):
        """This function will draw text"""
        # Creating a text object
        textobj = self.font.render(text, 1, color)
        textrect = textobj.get_rect()
        # Adding the coordinates of where the text will be written
        textrect.topleft = (x_pos, y_pos)

        # Drawing the text on the window
        self.window.blit(textobj, textrect)


    def button(self, text, pos_y, pos_x=None):
        """This function will be responsible for creating a menu button"""
        # Defining the hight and width of the button
        # The position on the x coordinate will be solid
        if pos_x is None:
            pos_x = self.center_of_x_coordinates

        button_width = 200
        button_height = 60
        button_pos_y = pos_y - (button_height//2)
        button_pos_x = pos_x - (button_width // 2)



        # Creating the button
        button = pg.Rect(button_pos_x, button_pos_y,
                            button_width, button_height)

        # Drawing the text and the button
        pg.draw.rect(self.window, (138, 138, 138), button)
        self.draw_text(text,
                           (255, 255, 255), (pos_x - 45), (pos_y - 25))

        # We return the button in order to check if the user click it
        return button


    def start_menu(self):
        """This function will create a little start menu for the game"""

        while True:
            self.window.fill((252, 207, 121, 255))
            # We need to get the position of the mouse
            mx,my = pg.mouse.get_pos()
            start_button = None
            game_options = [[None, 2], [None, 4], [None, 6]]

            # First we will create the start game button
            # We will centerialize the button in the middle of the page
            if not self.play:
                pos_y = self.center_of_y_coordinates
                start_button = self.button("Play", pos_y)

            if self.play and self.players_nr is None:
                # Here we check if the player started the game but did not
                # yet choose the number of the players
                pos_y = (self.center_of_y_coordinates * 2) // 3 // 2
                game_options_text = ["2 players", "4 players", "6 players"]

                # Looping through the options and creating a button for each option
                for option_nr in range(3):
                    option_text = game_options_text[option_nr]
                    button_pos_y = pos_y * (option_nr + 1)

                    # Creating the button and saving it to the game options list
                    button = self.button(option_text, button_pos_y)
                    game_options[option_nr][0] = button
            
            elif self.play and self.players_nr:
                self.run_game()




            # Creating a simple game run to check if the player made any clicks
            for event in pg.event.get():
                if event.type == QUIT:
                        pg.quit()
                        
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pg.quit()

                if event.type == MOUSEBUTTONDOWN:

                    # Here we check if the player did not start the game
                    if start_button:
                        # Here we check if the player did click the start game button
                        if event.button == 1 and start_button.collidepoint(mx,my):
                            self.play = True
                            self.window.fill((252, 207, 121, 255))
                    else:
                        # Getting each option alone and check if it has been clicked
                        for option in game_options:
                            if event.button == 1 and option[0].collidepoint(mx, my):
                                self.players_nr = option[1]
                                



            pg.display.update()
            



    def set_up(self):
        """This function will setup the game board
        and the basic game stuff"""

    def run_game(self):
        self.window.fill((252, 207, 121, 255))
        self.game_board_hexagon()
        if self.players_nr == 2:
            self.two_players()
        elif self.players_nr == 4:
            self.four_players()
        else:
            self.sex_players()


        # The game loop will be running until the status of the run variable become false
        while self.run:

            # Getting the mouse position
            mouse_pos = pg.mouse.get_pos()
            for event in pg.event.get():

                if event.type == QUIT:
                    self.run = False

                if not self.play and self.players_nr is None:
                    self.start_menu()
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
    set_up = GameSetUp()
    set_up.start_menu()
