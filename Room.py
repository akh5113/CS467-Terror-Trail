# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Room.py
# This file defines the Room class


class RoomBase:
    """
    This is the base class for all of the Room instances.
    """
    def __init__(self, name, long_descrpt, short_descrpt, exit_descrpt, north, south, east, west):
        """
        Constructor.

        args:
            name (str): Name of the room.
            long_descrpt (str): Longer, more detailed description of the room. The user will see this only the first
                    time they enter a room.
            short_descrpt (str): Shorter description of the room. The user will see this upon reentering a room.
            exit_descrpt (str): Description of ways the user can exit a room
            north (Room): Room to the North.
            south (Room): Room to the South.
            east (Room): Room to the East.
            west (Room): Room to the West.
            """
        self.name = name
        self.long_descrpt = long_descrpt
        self.short_descrpt = short_descrpt
        self.exit_descrpt = exit_descrpt
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def get_name(self):
        """Return the Room name.

        Returns:
            str: name of the Room
        """
        return self.name

    def get_long_descrpt(self):
        """Return the long description of the Room.

            Returns:
                str: name of the Room
        """
        return self.long_descrpt

    def get_short_descrpt(self):
        return self.short_descrpt

    def get_exit_descrpt(self):
        return self.exit_descrpt

    def get_north(self):
        return self.north

    def get_south(self):
        return self.south

    def get_east(self):
        return self.east

    def get_west(self):
        return self.west


