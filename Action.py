# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Action.py
# This file defines the Action class, subclass of the Player class


#################################################################
# To be refined when we have decided on our verbs
#################################################################


import Player

class Action(Player):
    """Defines the action of the player."""

    def __init__(self, method, name, **kwargs):
        """Constructor.

        Args:
            method:
            name (str): name of the action
            kwargs (list): additional information needed for action.
        """
        self.method = method
        self.name = name
        self.kwargs = kwargs

# class move_north(Action):

# class move_south(Action):

# class move_east(Action):

# class move_west(Action):

# class pick_up(Action):


