# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# data_import.py
# This file imports room data into the room data structure

import json
import glob
from Room import *

def init_room(data):
    """
    Returns a room built with the room json data.
    args:
        data (dict): structure that contains all room data
    """
    name = data['roomName']
    long_intro = data['longIntro']
    short_intro = data['shortIntro']
    long_exit = data['longExit']
    short_exit = data['shortExit']
    north = data['north']
    south = data['south']
    east = data['east']
    west = data['west']
    features = (data['features'][0], data['features'][1])
    objects = init_room_objects(data)

    room = Room(name, long_intro, short_intro, long_exit, short_exit, north, south, east, west, features, objects)

    return room

def init_room_objects(data):
    """
    Returns a list of objects built with room data.
    args:
        data (dict): structure that contains all room data
    """
    objects = []
    object_data = data['objects']
    for o in object_data:
        name = o['name']
        new_object = Object(name, '')  #TODO: figure out actions - empty action for now
        objects.append(new_object)
    
    return objects 

def import_room_data():
    """
    Returns a list of Room structures
    """
    room_list = []

    for room_file in glob.iglob('Rooms/*.txt'):
        with open(room_file) as json_file:
            data = json.load(json_file)
            room = init_room(data)
            room_list.append(room)

    return room_list