# CS467 - Capstone Project 
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Action.py
# This file defines the Action class, subclass of the Player class


#################################################################
# To be refined when we have decided on our verbs
#################################################################
import data_printer
from Room import *

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
    # Waterfall next room
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
    # River next room
    elif next_room.name == "River":
        # Check if current room is Waterfall
        if current_room.name == "Waterfall":
            # if yes, check inventory for raft
            if check_inventory(player1,"Raft"):
                # if player has raft, ask if they want to use
                print("Would you like to use your raft to travel to the River?")
                use_raft = input(">>>")
                yes_raft = ["yes","Yes","YES","Y","y"]
                # if they want to use the raft
                if use_raft in yes_raft:
                    print("You have decided to use your raft to travel from the Waterfall to the River.")
                    # return River
                    return next_room
                #if they don't want to use the raft, then no movement
                print("You have decided not to use your raft right now.")
                return None
            # if they don't have a raft in inventory
            else:
               # can't travel this way
               print("It looks like you need something to travel from the Waterfall to the River. You should do some more exploring")
               return No
        # If current room isn't the waterfall
        else:
            # they can travel to river without raft
            return next_room
    # Cave next room    
    elif next_room.name == "Cave":
        # Check if current room is River
        if current_room.name == "River":
            # if yes, check inventory for raft and oar
            if check_inventory(player1,"Raft") and check_inventory(player1,"Oar"):
                # if player has raft and oar, ask if they want to use
                print("Would you like to use your raft and oar to travel to the Cave?")
                use_raft_oar = input(">>>")
                yes_raft_oar = ["yes","Yes","YES","Y","y"]
                # if they want to use the raft and oar
                if use_raft_oar in yes_raft_oar:
                    print("You have decided to use your raft and to travel from the River to the Cave.")
                    # return cave
                    return next_room
                #if they don't want to use the raft, then no movement
                print("You have decided not to use your raft and oar right now.")
                return None
            # if they don't have a raft in inventory
            else:
               # can't travel this way
               print("It looks like you need some things to travel from the River to the Cave. You should do some more exploring")
               return None        
        # Check if current room is Glacier
        elif current_room.name == "Glacier":
            # if yes, check inventory for shoes and rope
            if check_inventory(player1,"Shoes") and check_inventory(player1,"Rope"):
                # if player has shoes and rope, ask if they want to use
                print("Would you like to put on your shoes and use  the rope to travel to the Cave?")
                use_shoes_rope = input(">>>")
                yes_shoes_rope = ["yes","Yes","YES","Y","y"]
                # if they want to use the raft
                if use_shoes_rope in yes_shoes_rope:
                    print("You have decided to put on your shoes and use the rope to cross the Glacier to the Cave.")
                    # return cave
                    return next_room
                #if they don't want to use the shoes and rope, then no movement
                print("You have decided not to use your shoes and rope right now.")
                return None
            # if they don't have a raft in inventory
            else:
               # can't travel this way
               print("It looks like you need some things to travel from the Glacier to the Cave. You should do some more exploring")
               return None 
        # If current isn't Glacier or River
        else:
            # they can travel to the Cave without extra equipment
            return next_room
    # Forest next room
    elif next_room.name == "Forest":
        # Check if current room is Glacier
        if current_room.name == "Glacier":
            # if yes, check inventory for shoes and rope
            if check_inventory(player1,"Shoes") and check_inventory(player1,"Rope"):
                # if player has shoes and rope, ask if they want to use
                print("Would you like to put on your shoes and use  the rope to travel to the Forest?")
                use_shoes_rope = input(">>>")
                yes_shoes_rope = ["yes","Yes","YES","Y","y"]
                # if they want to use the raft
                if use_shoes_rope in yes_shoes_rope:
                    print("You have decided to put on your shoes and use the rope to cross the Glacier to the Forest.")
                    # return Forest
                    return next_room
                #if they don't want to use the shoes and rope, then no movement
                print("You have decided not to use your shoes and rope right now.")
                return None
            # if they don't have a raft in inventory
            else:
               # can't travel this way
               print("It looks like you need some things to travel from the Glacier to the Forest. You should do some more exploring")
               return None 
        # If current isn't Glacier
        else:
            # they can travel to the Forest without extra equipment
            return next_room
    # Campsite next room
    elif next_room.name == "Campsite":
        # Check if current room is Bike Trail
        if current_room.name == "Bike Trail":
            # if yes, check inventory for biek
            if check_inventory(player1,"Bike"):
                # if player has bike, ask if they want to use
                print("Would you like to bike to the Campsite?")
                use_bike = input(">>>")
                yes_bike = ["yes","Yes","YES","Y","y"]
                # if they want to use the bike
                if use_bike in yes_bike:
                    print("You have decided to ride your bike down the Bike Trail to the Campsite.")
                    # return campsite
                    return next_room
                #if they don't want to use the bike, then no movement
                print("You have decided not to use your bike right now.")
                return None
            # if they don't have a bike in inventory
            else:
               # can't travel this way
               print("It looks like you need something to travel through the Bike Trail. You should do some more exploring")
               return None 
        # Check if current room is Animal Habitat
        if current_room.name == "Animal Habitat":
            # Check if the room has not been completed
            if current_room.completed == False:
                # Animal hasn't been discovered yet
                print("You should really find out what animal lives here before going that way.")
                return None
            else:
                return next_room
        # If current isn't the Bike Trail or Animal Habitat
        else:
            # they can travel to the Campsite without extra equipment
            return next_room
    # Bike Trail next room
    elif next_room.name == "Bike Trail":
        # Check if current room is Campsite
        if current_room.name == "Campsite":
            # if yes, check inventory for biek
            if check_inventory(player1,"Bike"):
                # if player has bike, ask if they want to use
                print("Would you like to bike to the beginning of the Bike Trail?")
                use_bike = input(">>>")
                yes_bike = ["yes","Yes","YES","Y","y"]
                # if they want to use the bike
                if use_bike in yes_bike:
                    print("You have decided to ride your bike up the Bike Trail from the Campsite.")
                    # return bike trail
                    return next_room
                #if they don't want to use the bike, then no movement
                print("You have decided not to use your bike right now.")
                return None
            # if they don't have a bike in inventory
            else:
               # can't travel this way
               print("It looks like you need something to travel back up the Bike Trail. You should do some more exploring")
               return None 
        
        # If current isn't the Campsite
        else:
            # they can travel to the Bike Trail without extra equipment
            return next_room   
    # None of the above
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
                # if feautre is part of the current room
                feature.print_description(rooms)
                return True
        # Check if object in room
        for object in room.objects:
            if item.capitalize() == object.name:
                # if object is in room
                #TODO once objects have descriptions print them
                print("This will print a object in a room's description")
                return True
        # Check if object in inventory
        for obj in player1.inventory:
            if item.capitalize() == obj.name:
                # if object is in inventory
                #TODO once objects have descriptions print them
                print("This will print a object in a player's inventory description")
                return True 
        # if item is not in room or inventory
        return False
                
    
    

