# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Room.py
# This file defines the Room class


class RoomBase:
    """
    This is the base class for all of the Room instances.
    """
    def __init__(self, name, description, north, south, east, west):
        """
        Constructor.

        args:
            name (str): Name of the room.
            description (str): Description of the room
        """
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

