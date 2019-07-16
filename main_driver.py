# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# main_driver.py
# This file drives the game

import data_import
from Player import *
from Game import *


def main():
    """The driver function for the game."""
    # Set up game
    new_game = Game()

    # Load files for Rooms
    rooms = data_import.import_room_data()

    # Load files for Objects

    # Get starting room
    starting_room = None
    for room in rooms:
        if room.room_type == 0:
            starting_room = room
    if starting_room is None:
        print("Error: No Starting Room Set")    # Planning on implementing a better error flag, just using this for now

    # Set up player
    new_player = Player(starting_room)

    # Print intro to Game.
    new_game.print_intro()

    # Start Game
    play_game(new_game, new_player)


if __name__ == "__main__":
    main()

def play_game(game1, player1):
    """To Be Refined"""
    while game1.game_over is False:
        # Get current room
        current_room = player1.location
