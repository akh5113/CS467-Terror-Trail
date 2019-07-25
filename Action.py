# CS467 - Capstone Project 
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Action.py
# This file defines the Action class, subclass of the Player class


#################################################################
# To be refined when we have decided on our verbs
#################################################################
import data_printer
from Room import *
from Player import *

def determine_action(rooms, player1, current_room, command, preposition, use_on):
    """Takes user input and determines which action it will send the appropriate arguments to
    Args:
        rooms (list): List of rooms in the game
        player1 (Player): current player
        current_room (Room): current location of player
        command (str): verb to use to determine action
        preposition (str):
        use_on (str): object or feature to use the action on
    Returns:
        Boolean: If the action resulted in the player moving a room
    """
    #######################################################################################################
    # ACTION = MOVING ROOMS
    #######################################################################################################
    basic_move_cmds = ["go", "move", "walk", "exit", "travel", "cross"]
    if command.lower() in basic_move_cmds:
        # call move room action function to get next room
        next_room = move_room(use_on, current_room, rooms, player1)
        
        # call moved_locations to check if it was possible to move to the next room
        moved_locations(next_room,player1)


    #######################################################################################################
    # ACTION = LOOK
    #######################################################################################################
    elif command.lower() == "look" and preposition == "" and use_on == "":
        # call function to print long form explanation of the room
        look(current_room)
        return False

    #######################################################################################################
    # ACTION = LOOK AT
    #######################################################################################################
    elif command.lower() == "look" and use_on != "":
        # call function to explain feature or object
        if not look_at(use_on, player1, current_room, rooms):
            print("What you're trying to look at isn't here. Try looking at something else")
            return False

    #######################################################################################################
    # ACTION = TAKE
    #######################################################################################################
    elif command.lower() in ["take", "add", "pick up", "grab"]:
        # Call function to add object to inventory
        if not take(current_room, player1, use_on):
            print("That object is not in this room.")
        return False

    #######################################################################################################
    # ACTION = INVENTORY
    #######################################################################################################
    elif command.lower() == "inventory":
        inventory(player1)
        return False


    
def move_room(go_to, current_room, rooms, player1):
    """
    Get next room object to move to from current room to the user entered room
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
    if go_to.lower() in current_room.north_exits or go_to == current_room.north:
        next_room = get_room_object(current_room.north, rooms)

    elif go_to.lower() in current_room.south_exits or go_to == current_room.south:
        next_room = get_room_object(current_room.south, rooms)

    elif go_to.lower() in current_room.east_exits or go_to == current_room.east:
        next_room = get_room_object(current_room.east, rooms)

    elif go_to.lower() in current_room.west_exits or go_to == current_room.west:
        next_room = get_room_object(current_room.west, rooms)
    
    # Check if next room_room is None
    if next_room is None:
        return None
    
    # Check if the next_room is a restricted room
    if next_room.name in restricted_rooms:
        # Check the restriction
        next_room = current_room.check_room_restriction(next_room,player1)
    
    # Return the room. Will be None if there was an issue
    return next_room

def moved_locations(next_room,player1):
    """
    Determine if next room can be moved to
    args:
        next_room (Room): next room to try to move to
        player1 (Player): the current Player
    """
    
    # if no matching room found
    if next_room is None:
        # Then invalid command
        print("It doesn't look like you currently can or want to go that way. Try a different exit.")
        return False
    # if there is a matching room
    else:
        # move player to room
        player1.location = next_room
        print("Moved to", player1.location.name)
        print("\n")
        return True

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

def take(room, player, object_name):
    """Required verb/action
    Acquire an object and put it into your inventory

    Args:
        room (Room): current room of the game
        player (Player): player who's inventory the object will be added to
        object_name (str): The name of the object to be added
    Returns:
        Boolean: true if the object was found in the room, False if not
    """
    for obj in room.objects:
        if obj.name.lower() == object_name.lower():
            #add object to inventory
            player.add_obj_to_inventory(obj)
            #remove object from room
            room.remove_object(obj.name)
            print("{} has been added to your inventory".format(object_name.capitalize()))
            return True

    return False

def look(current_room):
    """Required verb/action
    Repeats the long form explination of the room
    args:
        current_room(Room): current player location
    """
    data_printer.print_room_long(current_room)

def look_at(item,player1,room,rooms):

    """Requried verb/action
    Look at feature or object or inventory, gives a interesting explination of the feature or object.
    args:
        item(string): what the user wants to look at
        player1(Player): player used to access inventory
        room(Room): player's current location
    """

    # if player wants to view inventory
    if item.lower() == "inventory":
        # Show player their current inventory
        print("Items in current inventory:")
        for i in player1.inventory:
            print(i.name)
            
    # if player wants to view an object or feature
    else:
        # Check if a feature of room
        for feature in room.features:
            if item.capitalize() == feature.feature_name:
                # if feature is part of the current room
                feature.print_description(rooms)
                return True
        # Check if object in room
        for o in room.objects:
            if item.capitalize() == o.name:
                # if object is in room
                print(o.description)
                return True
        # Check if object in inventory
        for obj in player1.inventory:
            if item.capitalize() == obj.name:
                # if object is in inventory
                print(obj.description)
                return True 
        # if item is not in room or inventory
        return False

def inventory(player):
    """Required verb
    Prints the contents of the players inventory
    """
    if len(player.inventory) == 0:
        print("There are no objects in your inventory.")
    else:
        for obj in player.inventory:
            print(obj.name)

def fill(player):
    """Fills players water bottle if it's in their inventory"""
    if "water bottle" not in player.inventory:
        print("Uh Oh! You don't have your water bottle!")
    else:
        print("This will help keep you hydrated as you find your way.")
    return False

def drink(player):
    """Player drinks from water bottle. Increases "thirst" health by 10 pts"""
    if "water bottle" not in player.inventory:
        print("Uh Oh! You don't have your water bottle!")
    #TODO implement elif for if your water bottle isn't filled
    else:
        print("Refreshing! That will help you go the extra mile. Just don't"
              "forget to fill it back up!")
        player.thirst += 10
    return False