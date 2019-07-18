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

        """Need to double check this syntax"""
        Player.__init__(self, location)

    def determine_action(self):
        """Setup a switch type or if statements to call different functions based on action"""
        if self.name == "go":
            move_room(self)

    """If action is a movement: go ..."""
    def move_room(self):
        """Need to figure out/correct the syntax to access"""
        """Check that """
        if self.location.is_valid == True:
            """Get the next room"""
            next_room = self.location.get_next_room()
            self.location = next_room

            """Also will need to add something later about the health"""
        else:
            """Some sort of error message that you can't go that way"""






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
