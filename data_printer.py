# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# main_driver.py
# This file drives the game

from Room import *
from Player import *
from Feature import *
import textwrap

SCREEN_WIDTH = 90

################################################################
# helper printing methods for Rooms
################################################################

def print_room_intro(room):
    """
    Print long/short intro based on if room has been visited
    args:
        room (Room): structure that contains all room data
    """
    if room.visited is False:
        word_wrap(room.long_intro)

    else:
        word_wrap(room.short_intro)

    print('\n')
    
def print_room_long(room):
    """
    Prints the long form explanation of the room
    args:
        room (Room): structure that contains all room data
    """
    word_wrap(room.long_intro)
    print('\n')    

def print_room_exit(room):
    """
    Print long exit for room
    args:
        room (Room): structure that contains all room data
    """
    word_wrap(room.long_exit)
    print("\n")

# this method is primarily intended for testing
def print_all_room_details(rooms):
    """
    Print all room details
    args:
        rooms (dict): dict structure that contains all rooms
    """  
    for room in rooms:
        print_single_room_details(room)

# this method is primarily intended for testing
def print_single_room_details(room):
    """
    Print details for a single room
    args:
        room (dict): structure that contains all room data
    """  
    print("Room Name: ", room.name)
    print("\n")
    
    print("Long Intro: ", room.long_intro)
    print("\n")

    print("Short Intro: ", room.short_intro)
    print("\n")

    print("Long Exit: ", room.long_exit)
    print("\n")

    print("North: ", room.north)
    print("South: ", room.south)
    print("East: ", room.east)
    print("West: ", room.west)
    print("\n")

    print("Features:")
    for f in room.features:
        print("Name: ", f.feature_name)
        if len(f.actions) > 0:
            for a in f.actions:
                print("-", a)
        if len(f.aliases) > 0:
            for a in f.aliases:
                print("-", a)
        print("Desc with Objects: ", f.description_with_objects)
        print("Desc no Objects: ", f.description_no_objects)
        print("\n")

    print("Objects:")
    for o in room.objects:
        print(o.name)
        print(o.description)
        for a in o.actions:
            print("-", a)
    print("\n")
    
    print("North Exits:")
    for exit_name in room.north_exits:
        print("-", exit_name)

    print("South Exits:")
    for exit_name in room.south_exits:
        print("-", exit_name)

    print("East Exits:")
    for exit_name in room.east_exits:
        print("-", exit_name)

    print("West Exits:")
    for exit_name in room.west_exits:
        print("-", exit_name)

    print(room.room_type)
    print('---------------------------------------------------')

################################################################
# helper printing methods for Player
################################################################

def print_health_levels(player):
    """
    Print hunger and thirst status for player
    args:
        player (Player): data for current player
    """
    print('\n')
    print("+-----------------+")
    print("|Energy %s/100   |" % player.energy)
    print("|Hydration %s/100|" % player.hydration)
    print("+-----------------+")
    print('\n')

################################################################
# helper printing methods for Feature
################################################################

def print_feature_description(feature):
    """
    Print description of feature
    args:
        feature (Feature): name of the feature
    """
    if feature.objects_found() is True:
        word_wrap(feature.description_with_objects)
    else:
        word_wrap(feature.description_no_objects)

################################################################
# helper printing methods for Game introduction
################################################################
def print_intro():
    """Prints the welcome statement for the game."""
    intro = "\nWelcome to the Terror Trail! You've tumbled and lost your way, now you need to make it back " \
            "to the ranger station before it's too late. You're hungry, you're thirsty, and you don't know " \
            "where you are. But if you look closely you might just find some items to help you find your " \
            "way back to the ranger station.\n\n"
    prompt1 = "Do you dare see if you can make it out?\n"
    prompt2 = "Console width must be between 85 and 100 characters. Default width is %d."
    prompt3 = "Console height must be a minimum of 30 characters.\n"
    prompt4 = "You can start a new game, load game, set width, or quit.\n"

    word_wrap(intro)

    print(prompt1)
    print(prompt2 % SCREEN_WIDTH)
    print(prompt3)
    print(prompt4)


def set_width():
    """
    Allow the user to set the console window width for playing the game.
    """
    global SCREEN_WIDTH 
    error = "Please enter a valid width."

    print("Set a window width between 85 and 100 characters. Default width is %d." % SCREEN_WIDTH)
    valid = False
    while True:
        screen_width_input = input(">>>")
        if screen_width_input.lower() == "default":
            break
        try:
            width = int(screen_width_input)
            if width >= 85 and width <= 100:
                SCREEN_WIDTH = int(width)
                break
            else:
                print(error)
        except ValueError:
            print(error)

    print("\n")
    print("Game width set to width of %d, please adjust window size!" % SCREEN_WIDTH)
    print("You can start a new game, load game, set width, or quit.")

def print_map(rooms):
    """
    When called, this method constructs a map of the game only showing the room
    names when the room has been visited.
    """
    # blank text for if the room has not been visited
    blank_room = "\t\t"

    # we know terror trail is first room, so will always be visited
    terror_trail = "Terror trail\t"

    # set all other rooms to simply tabs
    animal_habitat = blank_room
    bike_trail = blank_room
    campsite = blank_room
    cave = blank_room
    forest = blank_room
    geyser = blank_room
    glacier = blank_room
    hot_spring = blank_room
    lake = blank_room 
    mountain = blank_room 
    open_field = blank_room  
    ranger_station = blank_room + " "
    river = blank_room
    waterfall = blank_room

    # if a room has been visited, set the text for the room to the room name
    for room in rooms:

        if room.name == "Animal habitat":
            if room.visited == True:
                animal_habitat = room.name + ""

        if room.name == "Bike trail":
            if room.visited == True:
                bike_trail = room.name + "\t"

        if room.name == "Campsite":
            if room.visited == True:
                campsite = room.name + "\t"
        
        if room.name == "Cave":
            if room.visited == True:
                cave = room.name + "\t\t"

        if room.name == "Forest":
            if room.visited == True:
                forest = room.name + "\t"

        if room.name == "Geyser":
            if room.visited == True:
                geyser = room.name + "\t"

        if room.name == "Glacier":
            if room.visited == True:
                glacier = room.name + "\t"

        if room.name == "Hot spring":
            if room.visited == True:
                hot_spring = room.name + "\t"

        if room.name == "Lake":
            if room.visited == True:
                lake = room.name + "\t\t"

        if room.name == "Mountain":
            if room.visited == True:
                mountain = room.name + "\t"

        if room.name == "Open field":
            if room.visited == True:
                open_field = room.name + "\t"

        if room.name == "Ranger station":
            if room.visited == True:
                ranger_station = room.name + ""

        if room.name == "River":
            if room.visited == True:
                river = room.name + "\t"

        if room.name == "Waterfall":
            if room.visited == True:
                waterfall = room.name  + "\t"

    print("Terror Trail Map:")
    print("|----------------|---------------|---------------|")
    print("|", terror_trail, "|", mountain, "|", waterfall, "|")
    print("|----------------|---------------|---------------|")
    print("|", glacier, "|", cave, "|", river, "|")
    print("|----------------|---------------|---------------|")
    print("|", forest, "|", bike_trail, "|")
    print("|----------------|---------------|---------------|---------------|----------------|")
    print("|", animal_habitat, "|", campsite, "|", hot_spring, "|", geyser, "|",ranger_station, "|")
    print("|----------------|---------------|---------------|---------------|----------------|")
    print(" ", blank_room, "|", lake, "|",open_field, "|")
    print(" \t\t |---------------|---------------|")


def word_wrap(text_to_print):
    """
    Print text using a text wrapper 
    args:
        text_to_print (string): text to be printed using the text wrapper
    source for text wrapper: https://www.geeksforgeeks.org/textwrap-text-wrapping-filling-python/
    """
    wrapper = textwrap.TextWrapper(width=SCREEN_WIDTH, break_long_words=False, replace_whitespace=False)
    words = wrapper.wrap(text=text_to_print)
    for w in words:
        print(w)