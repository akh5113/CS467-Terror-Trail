# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Player.py
# This file defines the Player class


class Player:
    """Class to define the player."""

    def __init__(self):
        """Constructor."""
        self.hunger = 100
        self.thirst = 100
        self.inventory = []
        self.alive = True
        self.location = None    # Current location of the player

    def is_alive(self):
        """Is the player still alive.

        Returns:
            self.alive (Boolean): if the player is alive or not
        """
        return self.alive

    def player_status(self):
        """Gives the hunger and thirst levels of a player as a list

        Returns:
            self.hunger (int): Integer representing players hunger levels
            self.thirst (int): Integer representing players thirst levels
        """
        return [self.hunger, self.thirst]

    def get_location(self):
        """ What room the current player is in.

        Returns:
            self.location (Room): The room object the player is currently in.
        """
        return self.location

    def get_inventory(self):
        """Required action/verb
        Retrieve invetory of player.

        Returns:
            self.inventory (List): List of objects in the players inventory.
        """
        return self.inventory

