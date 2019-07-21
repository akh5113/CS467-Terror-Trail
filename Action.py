# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Action.py
# This file defines the Action class, subclass of the Player class


#################################################################
# To be refined when we have decided on our verbs
#################################################################
from Room import *

def move_room(go_to, current_room):
    """Move from current room to the user entered room"""
#Short exit list checking currently not function, room files missing the info
#Needs updates to be returning room objects not string 

    # Check all possible exit names in north exits
    if go_to in current_room.north_exits or go_to == current_room.north:
        # if match found return room name
        return current_room.north

    elif go_to in current_room.south_exits or go_to == current_room.south:
        return current_room.south

    elif go_to in current_room.east_exits or go_to == current_room.east:
        return current_room.east

    elif go_to in current_room.west or go_to == current_room.west:
        return current_room.west
    
    else:
        # if no matching room then return none
        return None

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