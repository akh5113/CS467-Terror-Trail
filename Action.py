# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Action.py
# This file defines the Action class, subclass of the Player class


#################################################################
# To be refined when we have decided on our verbs
#################################################################
from Room import *

def move_room(go_to, current_room, rooms):
    """Move from current room to the user entered room"""
#Short exit list checking currently not function, room files missing the info
#Needs updates to be returning room objects not string 

    # Check all possible exit names in north exits
    # if match found return room object
    if go_to in current_room.north_exits or go_to == current_room.north:
        return get_room_object(current_room.north, rooms)

    elif go_to in current_room.south_exits or go_to == current_room.south:
        return get_room_object(current_room.south, rooms)

    elif go_to in current_room.east_exits or go_to == current_room.east:
        return get_room_object(current_room.east, rooms)

    elif go_to in current_room.west_exits or go_to == current_room.west:
        return get_room_object(current_room.west, rooms)
    
    else:
        # if no matching room then return none
        return None

def get_room_object(room_name, rooms):
    next_room = None
    for room in rooms:
        if room_name == room.name:
            next_room = room
    return next_room

def determine_action(action_name, use_on):
    if action_name == "take":
        take(use_on)
    elif action_name == "look":
        look(use_on)
    elif action_name == "look at":
        look_at()

def take(object_name):
    """Required verb/action
    Acquire an object and put it into your inventory
    """

def look(name):
    """Required verb/action
    Repeats the long form explination of the room
    """

def look_at():
    """Requried verb/action
    Look at feature or object, gives a interesting explination of the feature or object.

    Allows player to look at objects in their inventory
    """
    inventory_list = []     # ned to figure out most efficent way to get inventory list
    print("Items in current inventory:")
    for i in inventory_list:
        print(i.name)