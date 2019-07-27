# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# data_import.py
# This file imports room data into the room data structure

import json
import glob
import pickle
from Room import *

def init_room(data):
    """
    Returns a room built with the room json data.
    args:
        data (dict): structure that contains all room data
    """
    name = data['room_name']
    long_intro = data['long_intro']
    short_intro = data['short_intro']
    long_exit = data['long_exit']
    north = data['north']
    south = data['south']
    east = data['east']
    west = data['west']
    features = init_room_features(name, data)
    objects = init_room_objects(data)
    north_exits = init_list(data['north_exits'])
    south_exits = init_list(data['south_exits'])
    east_exits = init_list(data['east_exits'])
    west_exits = init_list(data['west_exits'])
    room_type = data['room_type']
    restricted = data['restricted']

    room = Room(name, 
                long_intro, 
                short_intro, 
                long_exit, 
                north, 
                south, 
                east, 
                west, 
                features, 
                objects, 
                north_exits, 
                south_exits, 
                east_exits, 
                west_exits, 
                room_type,
                restricted)

    return room

def init_room_features(room_name, data):
    """
    Returns a list of features built with room data.
    args:
        data (dict): structure that contains all room data
    """
    features = []
    feature_data = data['features']
    for feature in feature_data:
        feature_name = feature['name']
        actions = init_list(feature['actions'])
        desc1 = feature['description1']
        desc2 = feature['description2']

        new_feature = Feature(room_name, feature_name, actions, desc1, desc2)
        features.append(new_feature)

    return features


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
        description = o['description']
        actions = init_list(o['actions'])
            
        new_object = Object(name, description, actions)
        objects.append(new_object)
    
    return objects

def init_list(data):
    """
    Returns a list structure for various object types
    args:
        data: contains items to be turned into a list
    """
    list_items = []
    for item in data:
        if item != "":
            list_items.append(item)
    return list_items

def import_room_data():
    """
    Returns a list of Room structures
    """
    room_list = []

    for room_file in glob.iglob('Rooms/*.txt'):
        with open(room_file, encoding="utf8") as json_file:
            data = json.load(json_file)
            room = init_room(data)
            room_list.append(room)

    return room_list

def load_game():
    """Returns a Game object with the last saved game data"""
    # load in saved files
    if glob.glob("saved_game.txt"):
        loaded_game = pickle.load(open("saved_game.txt", "rb"))
        return loaded_game

def load_player():
    """Returns a Player object with the last saved player data"""
    # load in saved files
    if glob.glob('saved_player.txt'):
        loaded_player = pickle.load(open("saved_player.txt", "rb"))
        return loaded_player