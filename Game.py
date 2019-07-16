# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
#Game.py
# This file defines the Engine of the game

import Room
import Player

class Game:
    """Game engine that runs the game."""
    def __init__(self):
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
