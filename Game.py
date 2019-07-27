# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
#Game.py
# This file defines the Engine of the game

from Player import *
from Room import *
import textwrap
import pickle

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
        for room in self.rooms:
            self.verbs += room.get_verbs()

        # Remove duplicate verbs
        dups_removed = []
        for verb in self.verbs:
            if verb not in dups_removed:
                dups_removed.append(verb)

        self.verbs = dups_removed

    @staticmethod
    def help():
        """Required action/verb
        Prints the help screen for game
        """
        print("---------------------------------------- HELP ---------------------------------------")
        print("help                         Lists verbs used throughout the game.")
        print("go <direction>               Moves player to the Room in the specified direction.")
        print("move <direction>             Moves player to the Room in the specified direction.")
        print("take <object>                Acquires object by putting it in player's inventory.")
        print("look                         States description of the current Room")
        print("look at <object/feature>     Gives explanation of object or feature")
        print("fill                         If 'Water Bottle' is in player's inventory, fill to be able to "
              "                             drink from.")
        print("drink                        If 'Water Bottle' is in player's inventory and it has been filled,"
              "                             drink to increase players hydration levels.")
        print("turn on <object>             If 'Flashlight' is in player's inventory, turns flashlight on to be used.")
        print("put on <object>              Puts on object if in player's inventory.")
        print("ride                         Rides bike if in player's inventory")
        print("inventory                    Lists the contents of players inventory")
        print("secure <object>              If 'Rope' is in player's inventory, secures Rope to cross glacier")
        print("health                       Displays the player's current energy and hydration levels")
        print("exit                         Displays the possible exits from a room.")
        print("savegame                     Saves the current state of the game.")
        print("loadgame                     Loads the previously saved game into play.")
        print("quit                         Exits the game without saving the game state.")
        print("-------------------------------------------------------------------------------------")

    def save_game(self, player):
        """
        Saves the state of the game.
        Args:
            player (Player): The player object in the last saved state.
            game (Game): The game object in the last saved state.
        """
        # write data to a file
        pickle.dump(player, open("saved_player.txt", "wb"))
        pickle.dump(self, open("saved_game.txt", "wb"))

    def quit_game(self):
        """Quits the game without saving the state"""

        self.game_over = True


    def health_status(self, player1):
        """Prints the player's current hunger and thrist levels"""
        data_printer.print_health_levels(player1)


    def list_exit(self,room):
        """Prints all the possible exit names"""
        print("Possible exits from", room.name, ":")
        for exit in room.east_exits:
            print(exit)
        for exit in room.west_exits:
            print(exit)
        for exit in room.north_exits:
            print(exit)
        for exit in room.south_exits:
            print(exit)


    def get_room_restrictions(self):
        """Returns list of rooms that have restrictions to enter thme"""
        restricted_rooms = []
        for room in self.rooms:
            if room.restricted is True:
                restricted_rooms.append(room)

        return restricted_rooms