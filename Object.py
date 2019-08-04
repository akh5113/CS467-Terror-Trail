# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Object.py
# This file defines the Object base class


class Object:
    """
    Base Class for the Objects in the game.
    """
    def __init__(self, name, description, original_feature, additional_actions):
        """Constructor.
        args:
           name (str): name of the object.
           description (str): description of the object
           action (str): action of the object.
        """
        self.name = name
        self.description = description

        self.actions = ["pick up", "drop", "take", "add", "leave", "abandon", "grab"]
        for verb in additional_actions:
            self.actions.append(verb)

        self.original_feature = original_feature

        self.used = False       # Has the object been found/used


