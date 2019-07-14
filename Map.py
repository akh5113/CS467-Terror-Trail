# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Map.py
# This file defines the Map class, a sub-class of Room

import Room


class Map(Room):
    """Defines the map of the game.

    A subclass of the Room class, the Map class handles the directions for the Rooms
    """
    def __init__(self, name, north, south, east, west):
        """Constructor."""
        super().__init__(name, north, south, east, west)

    def get_next_room(self, direction):
        """
        Gets the room requested

        args:
            direction (str): the direction of the requested room (north, south, east, west)
        Returns:
            self.direction (Room object): returns the room object of the room in the requested direction.
        """
        if direction == "north":
            return self.north
        elif direction == "south":
            return self.south
        elif direction == "east":
            return self.east
        else:
            return self.west

    def _is_valid(self, direction):
        """Returns if the direction specified is valid

        Returns:
            (boolean) representing if there is a room attached
            """
        next_room = self.get_next_room(direction)
        if next_room is None:
            return False
        return True
