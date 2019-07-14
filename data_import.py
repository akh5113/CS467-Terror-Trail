# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# data_import.py
# This file imports room data into the room data structure

import json
import glob
from Room import *

def initRoom(data):
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
    objects = initRoomObjects(data)

    room = Room(name, long_intro, short_intro, long_exit, short_exit, north, south, east, west, features, objects)

    return room

def initRoomObjects(data):
    """
    Returns a list of objects built with object json data.
    args:
        data (dict): structure that contains data of objects within a room
    """
    objects = []
    objectData = data['objects']
    for o in objectData:
        name = o['name']
        newObject = Object(name, '')  #TODO: figure out actions - empty action for now
        objects.append(newObject)
    
    return objects 

def importRoomData():
    """
    Returns a list of Room structures
    """
    roomList = []

    for roomFile in glob.iglob('Rooms/*.txt'):
        with open(roomFile) as json_file:
            data = json.load(json_file)

            room = initRoom(data)

            roomList.append(room)

    return roomList