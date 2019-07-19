# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Room.py
# This file defines the Room class

from Object import *
from enum import Enum
from Feature import *


class RoomType(Enum):
    START_ROOM = 0
    MID_ROOM = 1
    END_ROOM = 2


class Room:
    """ This is the base class for all of the Room instances. """
    def __init__(self, name,
                 long_intro,
                 short_intro,
                 long_exit,
                 short_exit,
                 north,
                 south,
                 east,
                 west,
                 features,
                 objects,
                 room_type):
        """
        Constructor.

        args:
            name (str): Name of the room.
            long_intro (str): Longer, more detailed description of the room. The user will see this only the first
                    time they enter a room.
            short_intro (str): Shorter description of the room. The user will see this upon reentering a room.
            long_exit (str): Longer description of ways the user can exit a room
            short_exit (str): Shorter description of how the user exits a room
            north (Room): Room to the North.
            south (Room): Room to the South.
            east (Room): Room to the East.
            west (Room): Room to the West.
            features (Tuple): Features in a room (immutable)
            objects (list): objects found in a room
            """
        self.name = name
        self.long_intro = long_intro
        self.short_intro = short_intro
        self.long_exit = long_exit
        self.short_exit = short_exit

        # What rooms are adjacent
        self.north = north
        self.south = south
        self.east = east
        self.west = west

        # Features in the Room
        self.features = features

        # Objects in Room
        self.objects = objects

        self.isLocked = False       # If room has required object to enter
        self.visited = False        # If the room has been visited
        self.completed = False      # If the object/task has been completed in the room

        self.room_type = room_type

    def get_name(self):
        """Return the Room name.

        Returns:
            str: name of the Room
        """
        return self.name

    def get_description(self, description_type):
        """Return the appropriate description of the Room.

        Args:
            description_type (str): Type of description needed (long, short, long exit, short exit)
        Returns:
           str: description of room
        """
        if description_type == "long_intro":
            return self.long_intro
        elif description_type == "short_intro":
            return self.short_intro
        elif description_type == "long_exit":
            return self.long_exit
        elif description_type == "short_exit":
            return self.short_exit

    def is_visited(self):
        """ Gives the status if the player has been to the room.

        Returns:
             self.visited (Boolean): if the player has visited the room before.
        """
        return self.visited

    def is_completed(self):
        """Gives the status if the room has been completed.

        A rooms completion status is based on if features have been examined and if any objects that needed to be
        picked up have been.

        Returns:
            self.completed (Boolean): If the room has been completed
        """
        return self.completed

    def get_feature(self, option):
        """Gets the feature of the room to examine.
        Args:
            option (int): representing the first or the second feature
        Returns:
            self.feature: the feature of the room
        """
        if option == 1:
            return self.features()[0]
        else:
            return self.features()[1]

    def get_object(self, obj_name):
        """Gets the object from the room

        Args:
            obj_name (str): the name of the object found in room
        Returns:
            object (Object): the object from the room
        Raise:

        """
        for room_object in self.objects:
            if obj_name == room_object:
                return room_object

        return "Not an object in this room"

    def add_object(self, obj):
        """Adds an object to the room"""
        self.objects.append(obj)

    def remove_object(self, obj_name):
        """Removes a specified object from a room"""
        self.objects[:] = [o for o in self.objects if o.get_name() != objName]
