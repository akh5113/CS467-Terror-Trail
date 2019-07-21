# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
#Game.py
# This file defines the Engine of the game

from Player import *

class Game:
    """Game engine that runs the game."""
    def __init__(self, rooms):
        self.game_over = False
        self.rooms = rooms

    def check_game_status(self, current_player):
        # If the player's thirst or hunger levels have gotten to 0, they have died
        if current_player.alive is False:
            self.game_over = True
        # If the player made it to the END_ROOM room type, they have won
        # Note: this will probably change as we develop the game, keeping it simple for now
        elif current_player.location.room_type is 2:
            print("YOU WON")
            self.game_over = True
        # Otherwise, game is still in play
        else:
            self.game_over = False

    @staticmethod
    def print_intro():
        """Prints the welcome statement for the game."""
        print("Welcome to the Terror Trail. ((to be expanded))")

    @staticmethod
    def help():
        """Required action/verb
        Prints the help screen for game
        """
        print("Help ((to be expanded))")
