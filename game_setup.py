"""importing the pygame module"""
# pylint: disable=no-member, undefined-variable, wildcard-import, unused-wildcard-import
import time
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
        self.run = False
        self.font = pg.font.SysFont("Georgia", 30)
        self.play = False
        self.players_nr = None
        self.player_turn = 0
        self.window_backgroung_color = (252, 207, 121, 255)

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

    def start_game_page(self):
        """This function will be called when the game just got started and waiting
        for the player to click start"""

        # First we will create the start game button
        # We will centerialize the button in the middle of the page
        if not self.play:
            self.window.fill(self.window_backgroung_color)
            start_button = None
            pos_y = self.center_of_y_coordinates
            start_button = self.button("Play", pos_y)

            return start_button

        return None

    def game_play_options(self):
        """This function will be called after the player clicked on start
        and here the player will get to choose the play mode"""


        if self.play and self.players_nr is None:
            self.window.fill(self.window_backgroung_color)
            game_options = [[None, 2], [None, 4], [None, 6]]
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

            return game_options

        return None

    def button_event_checker(self, event, start_button, game_play_options):
        """This function will be responsible for checking the game events"""
        # Getting the mouse positions
        mouse_x,mouse_y = pg.mouse.get_pos()

        # Checking if the game board has been clicked
        # pylint: disable=no-member
        if event.type == pg.MOUSEBUTTONDOWN:
            # Here we check if the player did not start the game
            if start_button:
                # Here we check if the player did click the start game button
                if event.button == 1 and start_button.collidepoint(mouse_x,mouse_y):
                    self.play = True
                    self.window.fill((252, 207, 121, 255))
            elif game_play_options:
                # Getting each option alone and check if it has been clicked
                for option in game_play_options:
                    if event.button == 1 and option[0].collidepoint(mouse_x,mouse_y):
                        self.players_nr = option[1]
                        self.run = True

    def set_up(self):
        """This function will setup the game board
        and the basic game stuff"""

        self.window.fill(self.window_backgroung_color)
        # This first bit of code will be respobsinble for running the start
        # menu until the player choose the play mode
        while True:

            # Here we check if the player has choosen the play mode or not yet
            # If yes we break this while loop and move forward
            if self.run:
                break

            start_button = self.start_game_page()
            game_play_options = self.game_play_options()

            for event in pg.event.get():
                # pylint: disable=no-member, undefined-variable
                if event.type == QUIT:
                    pg.quit()

                # This function will check if the player still in the start page
                # or in the choose game mode page and it will check if the player
                # clicks on the options and excute an order then
                self.button_event_checker(event, start_button, game_play_options)

            pg.display.update()

        # Here according to the givin play mode we create the cells
        # of the game board
        self.game_board_hexagon()
        if self.players_nr == 2:
            self.two_players()
        elif self.players_nr == 4:
            self.four_players()
        else:
            self.sex_players()

        # After that we created the cells then we will run the game
        self.run_game()

    def game_over(self, winner):
        """This function will be called when it is game over"""

        self.window.fill(self.window_backgroung_color)

        # We will display the winner on the screen
        # This piece of code will tell whos turn is now
        winner_statement = f"The winner is {winner}"
        statement_posx = self.center_of_x_coordinates
        statement_posy = 100
        statement_color = (255, 255, 255)
        self.draw_text(winner_statement, statement_color, statement_posx, statement_posy)

        pg.display.update()

        time.sleep(2)

        # Closing the game
        self.run = False



    def run_game(self):
        """This function will be responsible for running the game"""



        # The game loop will be running until the status of the run variable become false
        while self.run:
            self.window.fill(self.window_backgroung_color)

            # This piece of code will tell whos turn is now
            players_turn_statement = f"Now it's {self.players[self.player_turn]} turn"
            statement_posx = (self.center_of_x_coordinates * 2) - 300
            statement_posy = 100
            statement_color = (255, 255, 255)
            self.draw_text(players_turn_statement, statement_color, statement_posx, statement_posy)


            # Checking if any player did win the game
            winner = self.game_status(self.players[0: self.players_nr])
            if winner:
                self.game_over(winner)

            # Getting the mouse position
            mouse_pos = pg.mouse.get_pos()

            for event in pg.event.get():
                if event.type == QUIT:
                    self.run = False

                # Checking if the game board has been clicked
                # pylint: disable=no-member
                if event.type == pg.MOUSEBUTTONDOWN:

                    # Checking if the player do not have any possible cells to move to yet
                    if not self.processing:

                        self.detect_possible_moves(mouse_pos, self.player_turn)

                    else:
                        move = self.move_cell(mouse_pos)

                        if move and self.player_turn == (self.players_nr -1) :
                            self.player_turn = 0

                        elif move:
                            self.player_turn += 1



            self.update_game_board()
            pg.display.update()

        # Closing the playing window
        # pylint: disable=no-member
        pg.quit()

if __name__ == "__main__":
    set_up = GameSetUp()
    set_up.set_up()
