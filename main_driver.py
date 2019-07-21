# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# main_driver.py
# This file drives the game

import sys
import data_import
import data_printer
from Player import *
from Game import *
from Room import *
from Action import *

def main():
    """The driver function for the game."""
    # Set up game
    new_game = Game()

    # Load files for Rooms
    rooms = data_import.import_room_data()

    # Load files for Objects

    # Load files for Features

    # Get starting room
    starting_room = None
    for room in rooms:
        if room.room_type == RoomType.START_ROOM:
            starting_room = room
    if starting_room is None:
        print("Error: No Starting Room Set")    # Planning on implementing a better error flag, just using this for now

    # Set up player
    new_player = Player.Player(starting_room)

    # Print intro to Game.
    new_game.print_intro()

    # Start Game
    play_game(new_game, new_player)


def play_game(game1, player1):
    """To Be Refined"""
    prompt = ">>>"

    while game1.game_over is False:
        # Get current room
        current_room = player1.location

        # Display health
        data_printer.print_health_levels(player1)

        # Determine Into to display (short or long) - PS: I moved this logic into the method for printing intros?
        # Display the intro
        data_printer.print_room_intro(current_room)

        # Get user input
        user_input = input(prompt)

        # Determine if next action is moving rooms or action within room by checking if the users input is in the
        # list of exits
        # probably a more elegant way to do this, but using this for now!

        if user_input in current_room.north_exits:
            player1.location = move_room(current_room, current_room.north)

        elif user_input in current_room.south_exits:
            player1.location = move_room(current_room, current_room.south)

        elif user_input in current_room.east_exits:
            player1.location = move_room(current_room, current_room.east)

        elif user_input in current_room.west:
            player1.location = move_room(current_room, current_room.west)

        # If action is not changing room, figure out what it is doing
        else:
            # Get verbs for the room
            possible_actions = current_room.get_verbs()
            # Determine if the action is possible given the objects/features
            if user_input in possible_actions:
                determine_action(user_input)
                # Adding a break here to not get stuck!
                break
            else:
                # If action is not in list of verbs, print error message
                print("Error: not a valid action. Type <help> to see valid verbs")

        # Algorithm to determine health
        player1.player_status()

        # Check for game status
        game1.check_game_status(player1)
        
        break   #put temporary break in to prevent infinite loop :)

if __name__ == "__main__":
    main()

