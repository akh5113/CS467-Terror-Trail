# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Player.py
# This file defines the Player class

import data_printer

class Player:
    """Class to define the player."""

    def __init__(self, starting_location):
        """Constructor."""
        self.energy = 10000000 # previously hunger
        self.hydration  = 1000000
        self.inventory = []
        self.alive = True
        self.location = starting_location   # Current location of the player

    def player_status(self, moved_rooms):
        """Gives the hunger and thirst levels of a player as a list

        Prints
            self.energy (int): Integer representing players hunger levels
            self.hydration (int): Integer representing players thirst levels
        """
        if moved_rooms:
            # Energy levels will change by 10 for every move
            self.energy -= 4

            # Thirst levels will change by 5 for every move
            self.hydration -= 3

        else:
            # Energy levels will change by 10 for non-moving actions
            self.energy -= 2

            # Thirst levels will change by 5 for non-moving actions
            self.hydration -= 1


        # Determine if player is still alive
        if self.energy > 0 and self.hydration > 0:
            self.alive = True
        else:
            self.alive = False

        if self.energy <= 25 or self.hydration <= 25:
            data_printer.print_health_levels(self)
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
        Returns:
            tuple:
                Boolean: if the object is in the
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
