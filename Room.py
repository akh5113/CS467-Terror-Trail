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
                 north_exits,
                 south_exits,
                 east_exits,
                 west_exits,
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
            """
        self.name = name
        self.long_intro = long_intro
        self.short_intro = short_intro
        self.long_exit = long_exit
        self.short_exit = short_exit

        # What rooms are adjacent to the room
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

        self.room_type = RoomType[room_type]

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
        elif description_type == "short_exit":
            return self.short_exit

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
        """Get specific object from the room

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

    def check_room_restriction(self,next_room,player1):
        """
        Verify the room can be accessed using the objects in inventory
        args:
            self(Room): room player is currently in
            next_room(Room): room player wants to move to
            player1(Player): current player(used to access inventory)
        #TODO possibly implement this under Room.py as a class function???
        """
        # Waterfall next room
        if next_room.name == "Waterfall":
            # Check if self is river
            if self.name == "River":
                # if yes, check inventory for raft
                if player1.check_inventory("Raft"):
                    # if player has raft, ask if they want to use
                    print("Would you like to use your raft to travel to the Waterfall?")
                    use_raft = input(">>>")
                    yes_raft = ["yes","Yes","YES","Y","y"]
                    # if they want to use the raft
                    if use_raft in yes_raft:
                        print("You have decided to use your raft to travel from the River to the Waterfall.")
                        # return waterfall
                        return next_room
                    #if they don't want to use the raft, then no movement
                    print("You have decided not to use your raft right now.")
                    return None
                # if they don't have a raft in inventory
                else:
                   # can't travel this way
                   print("It looks like you need something to travel from the River to the Waterfall. You should do some more exploring")
                   return None
            # If current room isn't the river
            else:
                # they can travel to waterfall without raft
                return next_room    
        # River next room
        elif next_room.name == "River":
            # Check if current room is Waterfall
            if self.name == "Waterfall":
                # if yes, check inventory for raft
                if player1.check_inventory("Raft"):
                    # if player has raft, ask if they want to use
                    print("Would you like to use your raft to travel to the River?")
                    use_raft = input(">>>")
                    yes_raft = ["yes","Yes","YES","Y","y"]
                    # if they want to use the raft
                    if use_raft in yes_raft:
                        print("You have decided to use your raft to travel from the Waterfall to the River.")
                        # return River
                        return next_room
                    #if they don't want to use the raft, then no movement
                    print("You have decided not to use your raft right now.")
                    return None
                # if they don't have a raft in inventory
                else:
                   # can't travel this way
                   print("It looks like you need something to travel from the Waterfall to the River. You should do some more exploring")
                   return None
            # If current room isn't the waterfall
            else:
                # they can travel to river without raft
                return next_room
        # Cave next room    
        elif next_room.name == "Cave":
            # Check if current room is River
            if self.name == "River":
                # if yes, check inventory for raft and oar
                if player1.check_inventory("Raft") and player1.check_inventory("Oar"):
                    # if player has raft and oar, ask if they want to use
                    print("Would you like to use your raft and oar to travel to the Cave?")
                    use_raft_oar = input(">>>")
                    yes_raft_oar = ["yes","Yes","YES","Y","y"]
                    # if they want to use the raft and oar
                    if use_raft_oar in yes_raft_oar:
                        print("You have decided to use your raft and to travel from the River to the Cave.")
                        # return cave
                        return next_room
                    #if they don't want to use the raft, then no movement
                    print("You have decided not to use your raft and oar right now.")
                    return None
                # if they don't have a raft in inventory
                else:
                   # can't travel this way
                   print("It looks like you need some things to travel from the River to the Cave. You should do some more exploring")
                   return None        
            # Check if current room is Glacier
            elif self.name == "Glacier":
                # if yes, check inventory for shoes and rope
                if player1.check_inventory("Shoes") and player1.check_inventory("Rope"):
                    # if player has shoes and rope, ask if they want to use
                    print("Would you like to put on your shoes and use  the rope to travel to the Cave?")
                    use_shoes_rope = input(">>>")
                    yes_shoes_rope = ["yes","Yes","YES","Y","y"]
                    # if they want to use the raft
                    if use_shoes_rope in yes_shoes_rope:
                        print("You have decided to put on your shoes and use the rope to cross the Glacier to the Cave.")
                        # return cave
                        return next_room
                    #if they don't want to use the shoes and rope, then no movement
                    print("You have decided not to use your shoes and rope right now.")
                    return None
                # if they don't have a raft in inventory
                else:
                   # can't travel this way
                   print("It looks like you need some things to travel from the Glacier to the Cave. You should do some more exploring")
                   return None 
            # If current isn't Glacier or River
            else:
                # they can travel to the Cave without extra equipment
                return next_room
        # Forest next room
        elif next_room.name == "Forest":
            # Check if current room is Glacier
            if self.name == "Glacier":
                # if yes, check inventory for shoes and rope
                if player1.check_inventory("Shoes") and player1.check_inventory("Rope"):
                    # if player has shoes and rope, ask if they want to use
                    print("Would you like to put on your shoes and use  the rope to travel to the Forest?")
                    use_shoes_rope = input(">>>")
                    yes_shoes_rope = ["yes","Yes","YES","Y","y"]
                    # if they want to use the raft
                    if use_shoes_rope in yes_shoes_rope:
                        print("You have decided to put on your shoes and use the rope to cross the Glacier to the Forest.")
                        # return Forest
                        return next_room
                    #if they don't want to use the shoes and rope, then no movement
                    print("You have decided not to use your shoes and rope right now.")
                    return None
                # if they don't have a raft in inventory
                else:
                   # can't travel this way
                   print("It looks like you need some things to travel from the Glacier to the Forest. You should do some more exploring")
                   return None 
            # If current isn't Glacier
            else:
                # they can travel to the Forest without extra equipment
                return next_room
        # Campsite next room
        elif next_room.name == "Campsite":
            # Check if current room is Bike Trail
            if self.name == "Bike Trail":
                # if yes, check inventory for biek
                if player1.check_inventory("Bike"):
                    # if player has bike, ask if they want to use
                    print("Would you like to bike to the Campsite?")
                    use_bike = input(">>>")
                    yes_bike = ["yes","Yes","YES","Y","y"]
                    # if they want to use the bike
                    if use_bike in yes_bike:
                        print("You have decided to ride your bike down the Bike Trail to the Campsite.")
                        # return campsite
                        return next_room
                    #if they don't want to use the bike, then no movement
                    print("You have decided not to use your bike right now.")
                    return None
                # if they don't have a bike in inventory
                else:
                   # can't travel this way
                   print("It looks like you need something to travel through the Bike Trail. You should do some more exploring")
                   return None 
            # Check if current room is Animal Habitat
            if self.name == "Animal Habitat":
                # Check if the room has not been completed
                if self.completed is False:
                    # Animal hasn't been discovered yet
                    print("You should really find out what animal lives here before going that way.")
                    return None
                else:
                    return next_room
            # If current isn't the Bike Trail or Animal Habitat
            else:
                # they can travel to the Campsite without extra equipment
                return next_room
        # Bike Trail next room
        elif next_room.name == "Bike Trail":
            # Check if current room is Campsite
            if self.name == "Campsite":
                # if yes, check inventory for biek
                if player1.check_inventory("Bike"):
                    # if player has bike, ask if they want to use
                    print("Would you like to bike to the beginning of the Bike Trail?")
                    use_bike = input(">>>")
                    yes_bike = ["yes","Yes","YES","Y","y"]
                    # if they want to use the bike
                    if use_bike in yes_bike:
                        print("You have decided to ride your bike up the Bike Trail from the Campsite.")
                        # return bike trail
                        return next_room
                    #if they don't want to use the bike, then no movement
                    print("You have decided not to use your bike right now.")
                    return None
                # if they don't have a bike in inventory
                else:
                   # can't travel this way
                   print("It looks like you need something to travel back up the Bike Trail. You should do some more exploring")
                   return None 

            # If current isn't the Campsite
            else:
                # they can travel to the Bike Trail without extra equipment
                return next_room   
        # None of the above
        else:
            return None