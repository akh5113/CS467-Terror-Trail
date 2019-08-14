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
        self.verbs = ["inventory", "look", "look at", "go", "move", "take", "travel"]
        # Add additional
        self.get_additional_verbs()

    def check_game_status(self, current_player):
        # If the player made it to the END_ROOM room type, they have won
        # TODO this will probably change as we develop the game, keeping it simple for now
        if current_player.check_inventory("Radio"):
            radio = current_player.get_object("Radio")
            if radio.used is True and current_player.location.room_type is RoomType.END_ROOM:
                print("\nYou made it out of the terror trail!! \n\n WINNER!\n")
                self.game_over = True
        elif self.game_over is True:
            print("Game Over")
        # If the player's thirst or hunger levels have gotten to 0, they have died
        elif current_player.alive is False:
            self.game_over = True
            print("\nYou died and didn't make it out of the Terror Trail. Better luck next time.\n")
            print("\nGAME OVER\n")
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
        print("Gave saved!")

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

    def get_all_features(self):
        """Returns list of all features in the game"""
        features = []
        for room in self.rooms:
            features.append(room.get_feature(1))
            features.append(room.get_feature(2))

        return features

    def get_useable_verbs(self, current_room, player):
        """Returns list of useable verbs
        Combines actions from objects and features in teh current room as well as players inventory
        """
        useable_verbs = ["inventory", "look", "look at", "go", "move", "take"]

        # Features in Room
        for feature in current_room.features:
            for action in feature.actions:
                useable_verbs.append(action)
        # Objects in Room
        for obj in current_room.objects:
            for action in obj.actions:
                useable_verbs.append(action)
        # Objects in inventory
        for inv in player.inventory:
            for action in inv.actions:
                useable_verbs.append(action)

        verbs_dups_removed = []
        for verb in useable_verbs:
            if verb not in verbs_dups_removed:
                verbs_dups_removed.append(verb)

        return verbs_dups_removed
