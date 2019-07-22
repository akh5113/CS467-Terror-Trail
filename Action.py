# CS467 - Capstone Project 
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Action.py
# This file defines the Action class, subclass of the Player class


#################################################################
# To be refined when we have decided on our verbs
#################################################################
from Room import *

def move_room(go_to, current_room, rooms, player1):
    """
    Get net room object to move to from current room to the user entered room
    args:
        go_to(string): name of room user wants to move to
        current_room(Room): room player is currently in
        rooms(dict): dictionary object containing all rooms
        player1(Player): current player(used to access inventory)
    """

    # Exits which require objects to move to
    restricted_rooms = ["Waterfall","River","Cave","Forest","Bike Trail","Campsite"]

    # Set next_room to None
    next_room = None
    
    # Check if the go_to room is a possible exit, if so make it the next_room
    if go_to in current_room.north_exits or go_to == current_room.north:
        next_room = get_room_object(current_room.north, rooms)

    elif go_to in current_room.south_exits or go_to == current_room.south:
        next_room = get_room_object(current_room.south, rooms)

    elif go_to in current_room.east_exits or go_to == current_room.east:
        next_room = get_room_object(current_room.east, rooms)

    elif go_to in current_room.west_exits or go_to == current_room.west:
        next_room = get_room_object(current_room.west, rooms)
    
    # Check if next room_room is None
    if next_room == None:
        return None
    
    # Check if the next_room is a restricted room
    if next_room.name in restricted_rooms:
        # Check the restriction
        next_room = check_room_restriction(current_room,next_room,player1)
    
    # Return the room. Will be None if there was an issue
    return next_room

def check_room_restriction(current_room,next_room,player1):
    """
    Verify the room can be accessed using the objects in inventory
    args:
        current_room(Room): room player is currently in
        next_room(Room): room player wants to move to
        player1(Player): current player(used to access inventory)
    """
    if next_room.name == "Waterfall":
        # Check if current_room is river
        if current_room.name == "River":
            # if yes, check inventory for raft
            if check_inventory(player1,"Raft"):
                # if player has raft, ask if they want to use
                print("Would you like to use your raft to travel to the Waterfall?")
                use_raft = input(">>>")
                yes_raft = ["yes","Yes","YES","Y","y"]
                # if they want to use the raft
                if use_raft in yes_raft:
                    print("You have decided to use your raft to travel from the River to the Waterfall.")
                    # return waterfall
                    return next_room
                #if they don't want to use the raft, then no movement
                print("You have decided not to use your raft right now.")
                return None
            # if they don't have a raft in inventory
            else:
               # can't travel this way
               print("It looks like you need something to travel from the River to the Waterfall. You should do some more exploring")
               return None
        # If current room isn't the river
        else:
            # they can travel to waterfall without raft
            return next_room    
    elif next_room.name == "River":
        #TODO
        return next_room
    
    elif next_room.name == "Cave":
        #TODO
        return next_room 
    elif next_room.name == "Forest":
        #TODO
        return next_room
    
    elif next_room.name == "Bike Trail":
        #TODO
        return next_room    
    
    elif next_room.name == "Campsite":
        #TODO
        return next_room    
    
    else:
        return None
 
def check_inventory(player1,object_name):
    """
    Return if an object is in a player's invetory
    args:
        player1(Player): current player
        object_name(string): object to check inventory for
    """
    for i in player1.inventory:
        if object_name == i.name:
            return True
    else:
        return False

def get_room_object(room_name, rooms):
    """
    Get full room object from room dictionary based on room name
    args:
        room_name (string): the name of the room to retrieve
        rooms (dict): the dictionary object containing all rooms
    """
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
