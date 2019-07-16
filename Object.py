# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Object.py
# This file defines the Object base class


class Object:
    """
    Base Class for the Objects in the game.
    """
    def __init__(self, name, additional_actions):
        """Constructor.
        args:
           name (str): name of the object.
           action (str): action of the object.
        """
        self.name = name

        self.actions = ["Pick Up", "Drop"]
        for verb in additional_actions:
            self.actions.append(verb)

        self.used = False       # Has the object been found/used

    def get_action(self, action_name):
        """Returns the action for the object

        To be refined
        """
        return self.action
