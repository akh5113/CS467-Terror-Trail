# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# main_driver.py
# This file drives the game

from Room import *
from Player import *
from Feature import *

################################################################
# helper printing methods for Rooms
################################################################

def print_room_intro(room):
    """
    Print long/short intro based on if room has been visited
    args:
        room (Room): structure that contains all room data
    """
    if room.visited == False:
        print(room.long_intro)
    else:
        print(room.short_intro)
    print('\n')

def print_room_exit(room):
    """
    Print long exit for room
    args:
        room (Room): structure that contains all room data
    """
    print(room.long_exit)

################################################################
# helper printing methods for Player
################################################################

def print_health_levels(player):
    """
    Print hunger and thirst status for player
    args:
        player (Player): data for current player
    """
    print("Hunger %s/100" % player.hunger)
    print("Thirst %s/100" % player.thirst)
    print('\n')

def print_inventory(player):
    """
    Print hunger and thirst status for player
    args:
        player (Player): data for current player
    """
    for obj in player.inventory:
        print(obj)
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
        print(feature.description_with_objects)
    else:
        print(feature.description_no_objects)