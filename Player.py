# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Player.py
# This file defines the Player class


class Player:
    """Class to define the player."""

    def __init__(self, starting_location):
        """Constructor."""
        self.hunger = 100
        self.thirst = 100
        self.inventory = []
        self.alive = True
        self.location = starting_location   # Current location of the player

    def player_status(self):
        """Gives the hunger and thirst levels of a player as a list

        Prints
            self.hunger (int): Integer representing players hunger levels
            self.thirst (int): Integer representing players thirst levels
        """
        # Hunger levels will change by 1 for every move
        self.hunger -= 1

        # Thirst levels will change by 2 for every move
        self.thirst -= 2

        # Add any other factors that impact health

        # Determine if player is still alive
        if self.hunger > 0 and self.thirst > 0:
            self.alive = True
        else:
            self.alive = False

    def add_obj_to_inventory(self, obj):
        """Add an object to the players inventory
        Args:
            obj (Object): object to be added to the players inventory list
        """
        self.inventory.append(obj)

    def remove_obj_from_inventory(self, obj):
        """Remove object from players inventory
        Args:
            obj (Object): object to be removed from the players inventory list
        """
        self.inventory.remove(obj)
