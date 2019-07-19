# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# main_driver.py
# This file drives the game

import data_import
import data_printer
from Player import *
from Game import *
from Room import *

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
        if room.room_type == RoomType.START_ROOM:
            starting_room = room
    if starting_room is None:
        print("Error: No Starting Room Set")    # Planning on implementing a better error flag, just using this for now

    # Set up player
    new_player = Player.Player(starting_room)   # Not sure why but this needed the extra "Player." here...gonna do some research to see if we can remove

    # Print intro to Game.
    new_game.print_intro()

    # Start Game
    play_game(new_game, new_player)   


def play_game(game1, player1):
    """To Be Refined"""
    while game1.game_over is False:
        # Get current room
        current_room = player1.location

        # Display health
        data_printer.print_health_levels(player1)

        # Determine Into to display (short or long) - PS: I moved this logic into the method for printing intros?
        # Display the intro
        data_printer.print_room_intro(current_room)

        # Get user input

        # Call next action

        # Algorithm to determine health
        
        break   #put temporary break in to prevent infinite loop :)

if __name__ == "__main__":
    main()
