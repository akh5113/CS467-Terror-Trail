# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Feature.py
# This file defines the Feature class, a subclass of Room


class Feature:
    def __init__(self, room_name, feature_name, actions, description1, description2):
        """Constructor."""
        self.room_name = room_name
        self.feature_name = feature_name
        self.actions = actions              # List
        self.description_with_objects = description1
        self.description_no_objects = description2
        self.viewed = False







