# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Object.py
# This file defines the Object base class


class Object:
    """
    Base Class for the Objects in the game.
    """
    def __init__(self, name, action):
        """Constructor.
        args:
           name (str): name of the object.
           action (str): action of the object.
        """
        self.name = name
        self.action = action

        self.used = False       # Has the object been found/used

    def get_name(self):
        """Returns the name of the object"""
        return self.name

    def get_action(self):
        """Returns the action for the object"""
        return self.action