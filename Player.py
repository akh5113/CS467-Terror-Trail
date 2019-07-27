# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Player.py
# This file defines the Player class


class Player:
    """Class to define the player."""

    def __init__(self, starting_location):
        """Constructor."""
        self.energy = 100 # previously hunger
        self.hydration  = 100
        self.inventory = []
        self.alive = True
        self.location = starting_location   # Current location of the player

    def player_status(self):
        """Gives the hunger and thirst levels of a player as a list

        Prints
            self.energy (int): Integer representing players hunger levels
            self.hydration (int): Integer representing players thirst levels
        """
        # Energy levels will change by 1 for every move
        self.energy -= 1

        # Thirst levels will change by 2 for every move
        self.hydration -= 2

        # Add any other factors that impact health

        # Determine if player is still alive
        if self.energy > 0 and self.hydration > 0:
            self.alive = True
        else:
            self.alive = False

        if self.energy <= 25 or self.hydration <= 25:
            print("You're starting to get a little lightheaded, better find some water or food.")

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

    def check_inventory(self, object_name):
        """
        Return if an object is in a player's invetory
        args:
            player1(Player): current player
            object_name(string): object to check inventory for
        """
        for i in self.inventory:
            if object_name == i.name:
                return True
        else:
            return False

    def get_object(self, object_name):
        """Returns the Object object if in the player's inventory"""
        for i in self.inventory:
            if object_name == i.name:
                return i
