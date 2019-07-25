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
    # Print intro to Game.
    data_printer.print_intro()
    main_menu_input = input(">>>")

    # Determine how to start game
    if main_menu_input == "new game":
        # Load files for Rooms including Features and Objects within rooms
        rooms = data_import.import_room_data()

        # Set up game
        new_game = Game(rooms)

        # Get starting room
        starting_room = None
        for room in rooms:
            if room.room_type == RoomType.START_ROOM:
                starting_room = room
        if starting_room is None:
            print("Error: No Starting Room Set")    # Planning on implementing a better error flag, just using this for now

        # Set up player
        new_player = Player(starting_room)

        # Print intro to Game.
        new_game.print_intro()

        # Start Game
        play_game(new_game, new_player)

    elif main_menu_input in ["loadgame", "load game"]:
        #TODO implement loading of saved state
        # play_game(loaded_gme, loaded_player)
        exit()  #temporary

    else:
        print("Goodbye!")
        exit()


def play_game(game1, player1):
    """To Be Refined"""
    prompt = ">>>"

    while game1.game_over is False:
        # Get current room
        current_room = player1.location

        # Display health
        data_printer.print_health_levels(player1)

        # Determine Into to display (short or long)
        # Display the intro
        data_printer.print_room_intro(current_room)
        # Display exit info so user knows how to exit
        data_printer.print_room_exit(current_room)

        # Set room to visited
        current_room.visited = True

        # varaible to loop back if invalid input or if player has not moved rooms
        moved_rooms = False

        while moved_rooms is False:
            # Get user input
            user_input = input(prompt)
            # Split user input into command , preposition, object/feature/room
            split_input = user_input.split()
            # First is the command
            command = split_input[0]

            if len(split_input) >= 2:
                # If there is prepostion
                if (split_input[1] in ["at", "in", "on", "up"]):
                    preposition = split_input[1]
                    use_on = ' '.join(split_input[2:])
                else:
                    use_on = ' '.join(split_input[1:])
                    preposition = ""
            # If there is a one word command, others are empty
            else:
                use_on = ""
                preposition = ""

            ############################################################################
            #
            # DETERMINE ACTION
            #
            ############################################################################

            ############################################################################
            # Commands related to the game and not player action
            ############################################################################

            # If action is help
            if command.lower() == "help":
                game1.help()
                moved_rooms = False

            # if action is savegame
            elif command.lower() == "savegame":
                game1.save_game()
                moved_rooms = False

            elif command.lower() == "loadgame":
                game1.load_game()

            # If action is quit
            elif command.lower() == "quit":
                game1.quit_game()
                break

            ############################################################################
            # Commands related to player action and not game state
            ############################################################################
            else:
                # Determine if the action is possible given the objects/features
                #TODO determine verbs for this for specific room instead of whole game verbs
                if command in game1.verbs:
                    determine_action(game1.rooms, player1, current_room, command, preposition, use_on)
                    if (current_room.name != player1.location.name):
                        moved_rooms = True
                else:
                    # If action is not in list of verbs, print error message
                    print("Error: not a valid action. Type <help> to see valid verbs")
                    moved_rooms = False

            # Calculate players new health with each move
            player1.player_status()

        # Check for game status
        game1.check_game_status(player1)

if __name__ == "__main__":
    main()

