# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
#Game.py
# This file defines the Engine of the game

from Player import *
from Room import *

class Game:
    """Game engine that runs the game."""
    def __init__(self, rooms):
        self.game_over = False
        self.rooms = rooms

        # Verbs to be used within game
        self.verbs = ["inventory", "look", "look at", "go", "move", "take"]
        # Add additional
        self.get_additional_verbs()

    def check_game_status(self, current_player):
        if self.game_over is True:
            print("Game Over")
        # If the player's thirst or hunger levels have gotten to 0, they have died
        elif current_player.alive is False:
            self.game_over = True
            print("You died, game over")
        # If the player made it to the END_ROOM room type, they have won
        # Note: this will probably change as we develop the game, keeping it simple for now
        elif current_player.location.room_type is 2:
            print("YOU WON")
            self.game_over = True
        # Otherwise, game is still in play
        else:
            self.game_over = False

    def get_additional_verbs(self):
        """Takes all verbs possible for the game and adds them to a list
        Used to determine if user input is correct.
        """
        #TODO: Need to remove duplicate verbs
        for room in self.rooms:
            self.verbs += room.get_verbs()

    @staticmethod
    def print_intro():
        """Prints the welcome statement for the game."""
        print("Welcome to the Terror Trail. ((to be expanded))")
        print("\n")

    @staticmethod
    def help():
        """Required action/verb
        Prints the help screen for game
        """
        print("----------------------------------- HELP -----------------------------------")
        print("help                         Lists verbs used throughout the game.")
        print("go <direction>               Moves player to the Room in the specified direction.")
        print("move <direction>             Moves player to the Room in the specified direction.")
        print("take <object>                Acquires object by putting it in player's inventory.")
        print("look                         States description of the current Room")
        print("look at <object/feature>     Gives explanation of object or feature")
        print("inventory                    Lists the contents of players inventory")
        print("savegame                     Saves the current state of the game.")
        print("loadgame                     Loads the previously saved game into play.")
        print("quit                         Exits the game without saving the game state.")
        print("---------------------------------------------------------------------------_")

    def save_game(self):
        """Saves the state of the game"""
        # write data to a file

    def load_game(self):
        """Loads a saved state of the game"""
        # load in saved files

    def quit_game(self):
        """Quits the game without saving the state"""
        print("Quitting the game without saving the state")
        self.game_over = True
