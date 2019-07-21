# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# Feature.py
# This file defines the Feature class, a subclass of Room


class Feature:
    def __init__(self, room_name, feature_name, actions, description1, description2):
        """Constructor.

        Args:
            room_name (Room): The Room object the feature is in.
            feature_name (str): The name of the feature.
            actions (str, list):  A list of the possible actions/verbs for this feature.
            description1 (str): A description if there are objects still to be interacted with.
            description2(str): A description if there are no objects to be interacted with.
        """
        self.room_name = room_name
        self.feature_name = feature_name
        self.actions = actions             # List
        self.description_with_objects = description1
        self.description_no_objects = description2
        self.viewed = False

    def objects_found(self):
        if self.room_name.objects is None:
            return False
        else:
            return True
