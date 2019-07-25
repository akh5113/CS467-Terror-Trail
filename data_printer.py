# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# main_driver.py
# This file drives the game

from Room import *
from Player import *
from Feature import *
import textwrap

################################################################
# helper printing methods for Rooms
################################################################

def print_room_intro(room):
    """
    Print long/short intro based on if room has been visited
    args:
        room (Room): structure that contains all room data
    source for text wrapper: https://www.geeksforgeeks.org/textwrap-text-wrapping-filling-python/
    """
    wrapper = textwrap.TextWrapper(width=90, break_long_words=False,replace_whitespace=False)
    if room.visited is False:
        words = wrapper.wrap(text=room.long_intro)
        for w in words:
            print(w)
    else:
        words = wrapper.wrap(text=room.short_intro)
        for w in words:
            print(w)
    print('\n')
    
def print_room_long(room):
    """
    Prints the long form explanation of the room
    args:
        room (Room): structure that contains all room data
    source for text wrapper: https://www.geeksforgeeks.org/textwrap-text-wrapping-filling-python/
    """
    wrapper = textwrap.TextWrapper(width=90, break_long_words=False,replace_whitespace=False)

    words = wrapper.wrap(text=room.long_intro)
    for w in words:
        print(w)
    print('\n')    

def print_room_exit(room):
    """
    Print long exit for room
    args:
        room (Room): structure that contains all room data
    """
    wrapper = textwrap.TextWrapper(width=90,break_long_words=False,replace_whitespace=False)
    words = wrapper.wrap(text=room.long_exit)
    for w in words:
        print(w)
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
        rooms (dict): dict structure that contains all rooms
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
    print("|--------------|")
    print("|Hunger %s/100|" % player.hunger)
    print("|Thirst %s/100|" % player.thirst)
    print("|--------------|")
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
    wrapper = textwrap.TextWrapper(width=90,break_long_words=False,replace_whitespace=False)
    if feature.objects_found() is True:
        words = wrapper.wrap(text=feature.description_with_objects)
        for w in words:
            print(w)
    else:
        words = wrapper.wrap(text=feature.description_no_objects)
        for w in words:
            print(w)

################################################################
# helper printing methods for Game introduction
################################################################
def print_intro():
    """Prints the welcome statement for the game."""
    intro = "Welcome to the Terror Trail! You've tumbled and lost your way, now you need to make it back " \
            "to the ranger station before it's too late. You're hungry, you're thirsty, and you don't know " \
            "where you are. But if you look closely you might just find some items to help you find your " \
            "way back to the ranger station."
    prompt1 = "Do you dare see if you can make it out?"
    prompt2 = "You can start a new game, load game, or quit."
    newline = "\n"

    wrapper = textwrap.TextWrapper(width=90,break_long_words=False,replace_whitespace=False)
    words = wrapper.wrap(text=intro)
    for w in words:
        print(w)

    print(newline)
    print(prompt1)
    print(prompt2)
    print(newline)
