# CS467 - Capstone Project 
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Action.py
# This file defines the Action class, subclass of the Player class


#################################################################
# To be refined when we have decided on our verbs
#################################################################
import data_printer
import time
from Room import *
from Player import *

BIKE_MOVE_CMDS = ["ride", "bike"]
RAFT_MOVE_CMDS = ["launch", "paddle"]

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
    #   Includes Riding bike
    #######################################################################################################
    # Move Commands
    basic_move_cmds = ["go", "move", "walk", "exit", "travel", "cross"]
    if command.lower() in basic_move_cmds or command.lower() in BIKE_MOVE_CMDS or command.lower() in RAFT_MOVE_CMDS:
        # call move room action function to get next room
        next_room = move_room(command, use_on, current_room, rooms, player1)
        
        # call moved_locations to check if it was possible to move to the next room
        return moved_locations(next_room,player1)

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
    elif (command.lower() == "look" and use_on != "") or command.lower() in \
            ["observe", "read", "view", "search", "examine", "check"]:
        # call function to explain feature or object
        if not look_at(use_on, player1, current_room, rooms):
            print("What you're trying to look at isn't here. Try looking at something else")
        return False

    #######################################################################################################
    # ACTION = TAKE
    #######################################################################################################
    elif command.lower() in ["take", "add", "pick", "grab"]:
        # Call function to add object to inventory
        success = take(rooms, current_room, player1, use_on)
        return False

    #######################################################################################################
    # ACTION = INVENTORY
    #######################################################################################################
    elif command.lower() == "inventory":
        inventory(player1)
        return False

    #######################################################################################################
    # ACTION = FILL
    #######################################################################################################
    elif command.lower() in ["fill"]:
        fill(player1, current_room)
        return False

    #######################################################################################################
    # ACTION = DRINK
    #######################################################################################################
    elif command.lower() in ["drink"]:
        drink(player1)
        return False

    #######################################################################################################
    # ACTION = PUT IN
    #######################################################################################################
    elif command.lower() in ["wear", "put"] and preposition in ["in", "on", "up"]:
        put(player1, use_on, preposition)
        return False

    #######################################################################################################
    # ACTION = TURN ON
    #######################################################################################################
    elif command.lower() in ["turn"] and preposition in ["on"]:
        turn_on(player1, use_on, current_room)
        return False

    #######################################################################################################
    # ACTION = SECURE
    #######################################################################################################
    elif command.lower() in ["secure", "attach"]:
        secure(player1, use_on)
        return False

    #######################################################################################################
    # ACTION = EAT
    #######################################################################################################
    elif command.lower() in ["eat"]:
        eat(player1, use_on)
        return False

    #######################################################################################################
    # ACTION = UNLOCK
    #######################################################################################################
    elif command.lower() in ["unlock"]:
        unlock(player1, current_room)
        return False

    #######################################################################################################
    # ACTION = DROP
    #######################################################################################################
    elif command.lower() in ["drop", "leave", "abandon"]:
        drop(player1, current_room, use_on)
        return False

    #######################################################################################################
    # ACTION = CALL
    #######################################################################################################
    elif command.lower() in ["call", "radio"]:
        call(player1, use_on, current_room)
        return False

    else:
        return False #TODO change to error message

def move_room(command, go_to, current_room, rooms, player1):
    """
    Get next room object to move to from current room to the user entered room
    args:
        go_to(string): name of room user wants to move to
        current_room(Room): room player is currently in
        rooms(dict): dictionary object containing all rooms
        player1(Player): current player(used to access inventory)
    """
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

    # check if command is a specality movement
    if command.lower() in BIKE_MOVE_CMDS:
        valid_speciality_movement = check_move_device(current_room, next_room, 1)
    elif command.lower() in RAFT_MOVE_CMDS:
        valid_speciality_movement = check_move_device(current_room, next_room, 2)
    else:
        valid_speciality_movement = True
    if valid_speciality_movement is False:
        return None

    # Check if the next_room is a restricted room
    if next_room.restricted is True:
        next_room = current_room.check_room_restriction(next_room, player1)

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
        return True

def check_move_device(current_room, next_room, command):
    # Check to see if the user is trying to use raft/paddle in non water room
    water_rooms = ["Waterfall", "River", "Cave"]
    non_bike_rooms = ["Waterfall", "River", "Glacier"]
    # RAFT
    if command == 2:
        if current_room.name not in water_rooms or next_room.name not in water_rooms:
            print("You need to be near water to use a raft.")
            return False
    # BIKE
    elif command == 1:
        if next_room.name in non_bike_rooms:
            print("You can't ride your bike through this.")
            return False
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

def take(rooms, room, player, object_name):
    """Required verb/action
    Acquire an object and put it into your inventory

    Args:
        room (Room): current room of the game
        player (Player): player who's inventory the object will be added to
        object_name (str): The name of the object to be added
    Returns:
        Boolean: true if the object was found in the room, False if not
    """
    # Check for max number of objects
    if len(player.inventory) >= 8:
        print("Woah woah you can't carry that much! You must pick something to drop before adding anything else.")
        return False
    # Check if object is unable to be picked up
    stationary_objects = ["cave art", "water"]
    if object_name.lower() in stationary_objects:
        print("You can't take {}, try another action".format(object_name))
        return False
    # If they don't have a full inventory
    for obj in room.objects:
        if obj.name.lower() == object_name.lower():
            # Get the original feature the object was seen in
            og_feature_str = obj.original_feature
            # if there is no feature needed to add the object, add to inventory
            if og_feature_str == "":
                # add object to inventory
                player.add_obj_to_inventory(obj)
                # remove object from room
                room.remove_object(obj.name)
                print("{} has been added to your inventory".format(object_name.capitalize()))
                return True
            # If there is a feature associated with the object
            else:
                # Get the feature object
                for room_feat in get_all_features(rooms):
                    if room_feat.feature_name == og_feature_str:
                        og_feature = room_feat
                        # If original feature has been viewed, it can be added to their inventory
                        if og_feature.viewed is True:
                            #add object to inventory
                            player.add_obj_to_inventory(obj)
                            #remove object from room
                            room.remove_object(obj.name)
                            print("{} has been added to your inventory".format(object_name.capitalize()))
                            return True
                        else:
                            print("You're getting close to the {}, but you need to look at {} first.".format(obj.name.lower(),
                                                                                                             og_feature.feature_name.lower()))
                            return False

    print("{} is not here.".format(object_name))
    return False


def get_all_features(rooms):
    """ Helper function
    Returns list of all features in the game"""
    all_features = []
    for room in rooms:
        all_features.append(room.get_feature(1))
        all_features.append(room.get_feature(2))

    return all_features


def look(current_room):
    """Required verb/action
    Repeats the long form explination of the room
    args:
        current_room(Room): current player location
    Returns:
        if user moved rooms
    """
    data_printer.print_room_long(current_room)

def look_at(item,player1,room,rooms):

    """Requried verb/action
    Look at feature or object or inventory, gives a interesting explination of the feature or object.
    args:
        item(string): what the user wants to look at
        player1(Player): player used to access inventory
        room(Room): player's current location
    Return:
        bool: if item was succewssfully viewed
    """

    # if player wants to view inventory
    if item.lower() == "inventory":
        # Show player their current inventory
        print("Items in current inventory:")
        for i in player1.inventory:
            print(i.name)
        return True

    elif item.lower() == "map":
        # Check to see if player has map in inventory
        if player1.check_inventory(item.capitalize()):
            data_printer.print_map(rooms)
            return True
        else:
            print("You need to take the map before reading!")
            return False
            
    # if player wants to view an object or feature
    else:
        # Check if a feature of room
        for feature in room.features:
            if item.capitalize() == feature.feature_name or item.lower() in feature.aliases:
                if feature.feature_name == "Informational sign":
                    if player1.check_inventory("Flashlight"):
                        flashlight = player1.get_object("Flashlight")
                        if flashlight.used:
                            print(feature.description_no_objects)
                            feature.viewed = True
                        else:
                            print("Turn on your flashlight to be able to read this.")
                    else:
                        print(feature.description_with_objects)
                else:
                    # if feature is part of the current room
                    feature.print_description(rooms)
                    # mark the item as viewed
                    feature.viewed = True
                    # Check for beaver den - decrease energy
                    if feature.feature_name == "Beaver den":
                        # Decrease health
                        data_printer.word_wrap("The beaver ended up keeping it to itself, but it really spooked you and took a lot out of you!")
                        player1.energy -= 10
                        data_printer.print_health_levels(player1)
                # call function to check if room has been completed
                room.check_room_completion()

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

#######################################################################################################
# OBJECT ACTIONS
#######################################################################################################

def fill(player, room):
    """Fills players water bottle if it's in their inventory"""
    #Check if room has water
    if room.get_object("Water"):
        if player.check_inventory("Water bottle"):
            wb = player.get_object("Water bottle")
            if wb.used is False:
                wb.used = True
                print("Filled! This will help keep you hydrated as you find your way, don't forget to drink!")
            else:
                print("You're bottle is already full!")
        else:
            print("Uh Oh! You don't have your water bottle!")
    else:
        print("There's no water in {}".format(room.name))

def drink(player):
    """Player drinks from water bottle. Increases "thirst" health by 10 pts"""
    if player.check_inventory("Water bottle"):
        wb = player.get_object("Water bottle")
        if wb.used is True:
            data_printer.word_wrap("Refreshing! That will help you go the extra mile. Just don't"
                  " forget to fill it back up!")
            player.hydration += 10
            data_printer.print_health_levels(player)
        else:
            print("Oh no! You forgot to fill your bottle! Looks like you need to find water.")
    else:
        print("Uh Oh! You don't have your water bottle!")

def put(player, obj, preposition):
    """For player to put on shoe if they exist in inventory"""
    if player.check_inventory(obj.capitalize()):
        inv_obj = player.get_object(obj.capitalize())
        # Check to see if object is able to be put on
        if ("put on" in inv_obj.actions) or ("put in" in inv_obj.actions):
            if inv_obj.used is True:
                print("You've already put {} {}!".format(preposition, obj))
            else:
                print("Good decision to put {} {}".format(preposition, obj))
                inv_obj.used = True
        else:
            print("You can't put {} {}".format(preposition, obj))

    else:
        print("You don't have any {} to put {}!".format(obj, preposition))

def turn_on(player, obj, room):
    """Turn on object"""
    if player.check_inventory(obj.capitalize()):
        inv_obj = player.get_object(obj.capitalize())
        if "turn on" in inv_obj.actions:
            inv_obj.used = True
            print("{} is on! This extra help gave you a boost!".format(inv_obj.name))
            player.energy += 5
            data_printer.print_health_levels(player)
        else:
            print("You can't turn on {}".format(obj))
    elif not player.check_inventory(obj.capitalize()):
        # check for feature to turn on
        for feature in room.features:
            for action in feature.actions:
                if action == "turn on":
                    print("{} is on! This extra help gave you a boost!".format(feature.feature_name))
                    player.energy += 5
                    data_printer.print_health_levels(player)
    else:
        print("You can't turn on {}".format(obj))

def ride(player):
    """Allows player to ride bike
    Args:
        player (Player): player in the game
    Returns:
        bool: if the player can successfully ride a bike
    """
    # Check for bike in inventory
    if player.check_inventory("Bike"):
        bike = player.get_object("Bike")
        # Check for tire in inventory
        if player.check_inventory("Tire"):
            tire = player.get_object("Tire")
            if tire.used is True:
                print("You're really movin' now! This is saving you some energy!")
                bike.used = True
                player.energy += 2
                data_printer.print_health_levels(player)
                return True
            else:
                print("You have a tire, you just need to put it on!")
                return False
        else:
            print("You need to find a tire and put it on before you can ride!")
            return False
    else:
        print("You need to find a bike before you can ride it!")
        return False


def secure(player, obj):
    """Allows player to secure object
    Args:
        player (Player): player of the game
        obj (str): object to secure
    Returns:
        bool: if the player successfully secured the object
    """
    # check for object in inventory
    if player.check_inventory(obj.capitalize()):
        returned_obj = player.get_object(obj.capitalize())
        if "secure" in returned_obj.actions:
            returned_obj.used = True
            print("The {} has been secured.".format(obj))
            return True
        else:
            print("You cannot secure {}".format(obj))
    else:
        print("You don't have {} to secure.".format(obj))
        return False

def eat(player, obj):
    """Player eats object to increase energy.
    Once player has eaten object it is removed from inventory
    """
    if player.check_inventory(obj.capitalize()):
        food = player.get_object(obj.capitalize())
        if "eat" in food.actions:
            food.used = True # possibly unnecessary but keeping it right now for clarity
            # Increase players energy
            player.energy += 20     # Possibly change depending on food
            print("YUM! The {} was just what you needed to help you get the extra mile.".format(obj.capitalize()))
            # Remove food from inventory
            player.remove_obj_from_inventory(food)
        else:
            print("You cannot eat {}".format(obj))
    else:
        print("You don't have {} in your inventory! Hope you find some soon!")


def unlock(player, room):
    """Player unlocks door with key"""
    if room.name == "Ranger station":
        if player.check_inventory("Key"):
            key = player.get_object("Key")
            lock = room.get_feature(1)

            lock.viewed = True
            key.used = True
            print("It worked! You made it inside! Go find the blinking light!")
            return True
        else:
            print()
            return False
    else:
        print("There is nothing to unlock here.")
        return False

def drop(player, room, obj_name):
    """drops the object in the current room"""
    # Check if object is in Player's inventory
    if player.check_inventory(obj_name.capitalize()):
        # get Object type
        players_object = player.get_object(obj_name.capitalize())
        # add back to room object list
        room.add_object(players_object)
        # Change item used from True to False
        players_object.used = False
        # remove from players inventory
        player.remove_obj_from_inventory(players_object)
        print("{} has been dropped in the {}".format(obj_name, room.name))
    else:
        print("You don't have {} in your inventory.".format(obj_name))

def paddle(player, obj1, obj2=None):
    """Check to see if player can use raft and oar
    Must use raft to go between river and waterfall
    Must use raft and oar to go from river to cave

    Args:
        obj1 = raft
        obj2 = oar
    """
    # Check players inventory
    if player.check_inventory(obj1):
        # get raft object
        raft_obj = player.get_object(obj1.capitalize())
        if "launch" in raft_obj.actions:
            raft_obj.used = True
            if obj2 is not None:
                # check players inventory for paddle
                if player.check_inventory(obj2):
                    # get oar object
                    oar_obj = player.get_object(obj2)
                    if "paddle" in oar_obj.actions:
                        oar_obj.used = True
                        print("The oar helped you get your raft through the rapids and saved you some energy.")
                        player.energy += 2
                        data_printer.print_health_levels(player)
                        return True
                    else:
                        print("You can't paddle with {}".format(obj2))
                else:
                    print("You have a raft, but an oar will get you down the river!")
                    return False
            else:
                print("This raft will help you move a lot faster and save energy!")
                player.energy += 2
                data_printer.print_health_levels(player)
                return True
        else:
            print("You can't launch a {}".format(obj1))
    else:
        return False

def call(player, obj, current_room):
    """User calls using the radio"""
    # check player is in right room
    if current_room.name == "Ranger station":
        # Check if lock has been unlocked
        lock = current_room.get_feature(1)
        if lock.viewed:
            # Check for batteries
            if player.check_inventory("Batteries"):
                # Get batteries object
                batteries = player.get_object("Batteries")
                if batteries.used:
                    radio = current_room.get_object(obj.capitalize())
                    # get radio object
                    player.add_obj_to_inventory(radio)
                    radio.used = True
                else:
                    print("Quickly put in the batteries!")
            else:
                print("You get to the radio only to find out it's almost dead, do you have any batteries?")
        else:
            print(lock.description_with_objects)
    else:
        print("There is nothing you can use to call for help in the {}.".format(current_room.name))

def check_for_object(use_on):
    """Checks to make sure user entered an object with verb"""
    if use_on is "":
        print("You need an object for this to work.")
        return False
    else:
        return True
