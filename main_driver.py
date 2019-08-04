# CS467 - Capstone Project
# Coast-to-Coast Group: Brittany Dunn, Anne Harris, Polly Sobeck
# main_driver.py
# This file drives the game

import sys
import data_import
import data_printer
import time
import shutil
from Player import *
from Game import *
from Room import *
from Action import *

def main():
    """The driver function for the game."""
    # Print intro to Game.
    data_printer.print_intro()

    # Determine how to start game
    valid_choice = False
    while valid_choice is False:
        main_menu_input = input(">>>")
        if main_menu_input == "new game":
            valid_choice = True

            # Enforce only valid console widths
            validate_console_size()

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

            # Start Game
            play_game(new_game, new_player)

        elif main_menu_input in ["loadgame", "load game"]:
            valid_choice = True

            # Enforce only valid console widths
            validate_console_size()

            # Load Saved Player Data
            loaded_player = data_import.load_player()

            # Load Saved Game Data
            loaded_game = data_import.load_game()

            if (not loaded_game or not loaded_player ):
                print("Error: Unable to load game!")
                exit()
            else:
                print("Game resumed!")
                # Play game with saved player and game data
                play_game(loaded_game, loaded_player)
        
        elif main_menu_input == "set width":
            data_printer.set_width()

        elif main_menu_input == "quit":
            valid_choice = True
            print("Goodbye!")
            exit()

        else:
            valid_choice = False
            print("Please enter a valid command:"
                  " <new game>"
                  " <load game>"
                  " <set width>"
                  " <quit>")


def play_game(game1, player1):
    """Implement the game workflow and checks for game ending.
        1. Gets the players current room status
        2. Displays the health of the player
        4. Prints either long or short into
        5. Prints exits
        6. Sets the room to visited
        7. While the user has not moved rooms, enter while loop
            a. prompt the user and get input
            b. split input
            c. determine if action effects game or player and call appropriate function
            d. calculate players health
        8. Check the game status
    """
    prompt = ">>>"

    while game1.game_over is False:
        # Get current room
        current_room = player1.location

        #print current room
        print("****************************************************")
        print("You are in the {}".format(current_room.name))
        print("****************************************************")

        # Display health
        data_printer.print_health_levels(player1)

        # Determine Into to display (short or long)
        # Display the intro
        data_printer.print_room_intro(current_room)

        # Display exit info so user knows how to exit
        data_printer.print_room_exit(current_room)

        # Set room to visited
        current_room.visited = True

        # variable to loop back if invalid input or if player has not moved rooms
        moved_rooms = False

        while moved_rooms is False:
            # Get user input
            user_input = input(prompt)
            # Split user input into command , preposition, object/feature/room
            split_input = user_input.split()
            # First is the command
            if split_input:
                command = split_input[0]
            else:
                command = "INVALID"
            # If second word part of location
            if len(split_input) >=2 and split_input[1] in ["trail", "habitat", "spring", "field", "station"]:
                command = ' '.join(split_input[0:])
                preposition = ""
                use_on = ""                
            elif len(split_input) >= 2:
                # If there is prepostion
                if split_input[1] in ["at", "in", "on", "up"]:
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

            # If action is savegame
            elif command.lower() == "savegame":
                game1.save_game(player1)
                moved_rooms = False

            # If action is loadgame
            elif command.lower() == "loadgame":
                game1 = data_import.load_game()
                player1 = data_import.load_player()

                if (not game1 or not player1):
                    print("Error: Unable to load game!")
                else:
                    print("Game resumed!")

            # If action is health
            elif command.lower() == "health":
                game1.health_status(player1)
                
            # If action is exit
            elif command.lower() == "exit":
                game1.list_exit(player1.location)
                
            # If action is quit
            elif command.lower() == "quit":
                user_input = input("Would you like to save before quitting?")
                if user_input in ["yes","Yes","YES","Y","y"]:
                    game1.save_game(player1)
                    
                game1.quit_game()
                break        
                
            ############################################################################
            # Commands related to player action and not game state
            ############################################################################
            else:
                valid_action = False
                # Determine if the action is possible given the objects/features
                #TODO determine verbs for this for specific room instead of whole game verbs
                if command in game1.verbs:
                    moved_rooms = determine_action(game1.rooms, player1, current_room, command, preposition, use_on)
                    valid_action = True
                    
                else:
                    # Check command was not an exit name
                    for room in game1.rooms:
                        if command.lower() in room.east_exits or command.lower() in room.west_exits or \
                                command.lower() in room.north_exits or command.lower() in room.south_exits:
                            # change command to use_on
                            use_on = command
                            # change command to go
                            command = "go"
                            # call move_room function in actions to get next room
                            next_room = move_room(use_on,current_room, game1.rooms, player1)
                            # call moved_locations to try to move to that room
                            moved_rooms = moved_locations(next_room,player1)
                            valid_action = True
                    
                # If action is not in list of verbs or an exit name, print error message
                if valid_action is False:
                    print("Error: not a valid action. Type <help> to see valid verbs")

                # Calculate players new health
                player1.player_status(moved_rooms)

        # Check for game status
        game1.check_game_status(player1)
        if game1.game_over is True:
            break

def validate_console_size():
    """
    Validates that the players console window is between 82 and 100 columns
    and a minimum of 30 rows high.
    If invalid, quit game.
    """
    width, height = shutil.get_terminal_size(fallback=(90, 24))
    if width < 82 or width > 100:
        print("Invalid console width - quitting game.")
        exit()
    if height < 30:
        print("Invalid console height - quitting game.")
        exit()

if __name__ == "__main__":
    main()

