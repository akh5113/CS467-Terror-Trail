# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Action.py
# This file defines the Action class, subclass of the Player class


#################################################################
# To be refined when we have decided on our verbs
#################################################################

import Player

def determine_action(name):
    """Setup a switch type or if statements to call different functions based on action"""
    if name == "go":
        move_room()

"""If action is a movement: go ..."""
def move_room(current_location, next_location):
    """Need to figure out/correct the syntax to access"""
    """Check that """
    if current_location.is_valid(next_location) is True:
        """Get the next room"""
        next_room = current_location.get_next_room(next_location)

        return next_room

        """Also will need to add something later about the health"""
    else:
        """Some sort of error message that you can't go that way"""

def take(object_name):
    """Required verb/action
    Acquire an object and put it into your inventory
    """


def look(name):
    """Required verb/action
    Repeats the long form explination of the room
    """

def look_at(inventory_list):
    """Requried verb/action
    Look at feature or object, gives a interesting explination of the feature or object.

    Allows player to look at objects in their inventory
    """
    for i in inventory_list:
        print(i.name)
        print(i.description)