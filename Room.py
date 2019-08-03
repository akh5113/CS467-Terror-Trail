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
                 restricted):

        """
        Constructor.

        args:
            name (str): Name of the room.
            long_intro (str): Longer, more detailed description of the room. The user will see this only the first
                    time they enter a room.
            short_intro (str): Shorter description of the room. The user will see this upon reentering a room.
            long_exit (str): Longer description of ways the user can exit a room
            north (string): Name of room to the North.
            south (string): Name of room to the South.
            east (string): Name of room to the East.
            west (string): Name of room to the West.
            features (Tuple): Features in a room (immutable)
            objects (list): objects found in a room
            north_exits (list): names used to identify room to the North
            south_exits (list): names used to identify room to the South
            east_exits (list): names used to identify room to the East
            west_exits (list): names used to identify room to the West
            room_type (enum): to determine if the room is a start, mid, or ending room
            restricted (bool): if the room requires objects to enter
            """
        self.name = name
        self.long_intro = long_intro
        self.short_intro = short_intro
        self.long_exit = long_exit

        # What rooms are adjacent to the room
        self.north = north
        self.south = south
        self.east = east
        self.west = west

        # Features in the Room
        self.features = features

        # Objects in Room
        self.objects = objects

        self.visited = False        # If the room has been visited
        self.completed = False      # If the object/task has been completed in the room

        self.room_type = RoomType[room_type]

        self.restricted = restricted    # If room has required object to enter

        # Names for all adjacent rooms this is a list of strings
        self.north_exits = north_exits
        self.south_exits = south_exits
        self.east_exits = east_exits
        self.west_exits = west_exits

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

    def get_feature(self, option):
        """Gets the feature of the room to examine.
        Args:
            option (int): representing the first or the second feature
        Returns:
            self.feature: the feature of the room
        """
        if option == 1:
            return self.features[0]
        else:
            return self.features[1]

    def get_object(self, obj_name):
        """Get specific object from the room

        Args:
            obj_name (str): the name of the object found in room
        Returns:
            object (Object): the object from the room
        Raise:

        """
        for room_object in self.objects:
            if obj_name == room_object.name:
                return room_object

        return "Not an object in this room"

    def add_object(self, obj):
        """Adds an object to the room"""
        self.objects.append(obj)

    def remove_object(self, obj_name):
        """Removes a specified object from a room"""
        self.objects[:] = [o for o in self.objects if o.name != obj_name]

    def get_verbs(self):
        """Compiles all verbs possible in the room by combining the actions associated with objects
        and the actions associated with the features
        """
        object_verb_list = []
        feature_verb_list = []

        # get object verbs
        for o in self.objects:
            object_verb_list += o.actions

        # get feature verbs
        for f in self.features:
            feature_verb_list += f.actions

        return object_verb_list + feature_verb_list

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
        elif direction in self.west_exits:
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

    def check_room_completion(self):
        # Check if the feature is in that room
        f1 = self.features[0]
        f2 = self.features[1]
        if f1.viewed and f2.viewed:
            self.completed = True
        else:
            self.completed = False

    def check_room_restriction(self,next_room,player1):
        """
        Verify the room can be accessed using the objects in inventory
        args:
            self(Room): room player is currently in
            next_room(Room): room player wants to move to
            player1(Player): current player(used to access inventory)
        """
        # Waterfall next room and currently in river
        # Only need Raft
        if next_room.name == "Waterfall" and self.name == "River" or next_room.name == "River" and self.name == "Waterfall":
            print("You must use a raft to travel between the waterfall and the river.")
            # if yes, check inventory for raft
            raft_results = paddle(player1, "Raft")
            if raft_results:
                return next_room
            else:
               # can't travel this way
               data_printer.word_wrap("It looks like you need something to travel from the River to the Waterfall. You should do some more exploring")
               return None

        # Cave next room and River Current Room
        elif next_room.name == "Cave" and self.name == "River":
            print("in restriction checker")
            raft_results = paddle(player1, "Raft", "Oar")
            if raft_results:
                return next_room
            else:
               # can't travel this way
               data_printer.word_wrap("It looks like you need some things to travel from the River to the Cave. You should do some more exploring.")
               return None

        # Cave or Forest next room and Glacier current room
        elif (next_room.name == "Cave" or next_room.name == "Forest") and self.name == "Glacier":
            #check for objects in inventory
            if player1.check_inventory("Shoes") and player1.check_inventory("Rope"):
                # check if object has been used
                rope = player1.get_object("Rope")
                shoes = player1.get_object("Shoes")
                if rope.used and shoes.used:
                    return next_room
                elif rope.used and not shoes.used:
                    data_printer.word_wrap("You're rope is secure, but you need to put on something to help from slipping across.")
                elif not rope.used and shoes.used:
                    print("You won't slip, but you'll never make it across without some rope secured.")
                else:
                    print("You need to secure a rope and put on shoes before you can cross.")
                return None
            elif player1.check_inventory("Shoes") and not player1.check_inventory("Rope"):
                print("You need to find some rope first")
                return None
            elif not player1.check_inventory("Shoes") and player1.check_inventory("Rope"):
                print("You need to find some shoes first.")
                return None
            else:
                print("You need to find rope and shoes before you can get to the Cave")
                return None

        # Campsite next room and current room bike trail
        elif next_room.name == "Campsite" and self.name == "Bike trail":
            # Call Ride funcion to check inventory
            print("You must ride a bike to the Campsite.")
            successful_ride = ride(player1)
            if successful_ride:
                return next_room
            else:
                return None

        # Campsite next room and current room Animal Habitat
        elif next_room.name == "Campsite" and self.name == "Animal habitat":
            # Check if the room has not been completed
            if self.completed is False:
                # Animal hasn't been discovered yet
                print("You should really find out what animal lives here before going that way.")
                return None
            else:
                return next_room

        # Bike Trail next room and Campsite current room
        # Restriction: must have bike and tire in inventory and tire must be used
        elif next_room.name == "Bike trail" and self.name == "Campsite":
            # Call Ride function to check inventory
            print("You must ride a bike to ride back up the Bike Trail")
            successful_ride = ride(player1)
            if successful_ride:
                return next_room
            else:
                return None

        # If current room doesn't need utilize restriction to get to next room
        else:
            return next_room
