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
    """Required verb/action"""

# class move_south(Action):
    """Required verb/action"""

# class move_east(Action):
    """Required verb/action"""

# class move_west(Action):
    """Required verb/action"""

# class take(Action):
    """Required verb/action
    Acquire an object and put it into your inventory
    """

# class look(Action):
    """Required verb/action
    Repeats the long form explination of the room
    """

# class look_at(Action):
    """Requried verb/action
    Look at feature or object, gives a interesting explination of the feature or object.
    
    Allows player to look at objects in their inventory
    """
