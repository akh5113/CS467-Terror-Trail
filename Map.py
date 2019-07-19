# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Map.py
# This file defines the Map class, a sub-class of Room

import Room


class Map(Room):
    """Defines the map of the game.

    A subclass of the Room class, the Map class handles the directions for the Rooms
    """
    def __init__(self, name, north, south, east, west, north_exits, south_exits, east_exits, west_exits):
        """Constructor."""
        super().__init__(name, north, south, east, west, north_exits, south_exits, east_exits, west_exits)

    def get_next_room(self, direction):
        """
        Gets the room requested by checking all short form names of a direction

        args:
            direction (str): the direction of the requested room (north, south, east, west)
        Returns:
            self.direction (Room object): returns the room object of the room in the requested direction.
        """
        if direction in self.north_exits:
            return self.north
        elif direction in self.south_exits:
            return self.south
        elif direction in self.east_exits:
            return self.east
        elif direction in self.west_extis:
            return self.west
        else:
            return None

    def _is_valid(self, direction):
        """Returns if the direction specified is valid

        Returns:
            (boolean) representing if there is a room attached
            """
        next_room = self.get_next_room(direction)
        if next_room is None:
            return False
        return True
