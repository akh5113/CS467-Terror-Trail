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

        # Start Game
        play_game(new_game, new_player)

    elif main_menu_input in ["loadgame", "load game"]:
        #TODO implement loading of saved state
        # play_game(loaded_gme, loaded_player)
        print("not yet implemented")    #temporary
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

        # variable to loop back if invalid input or if player has not moved rooms
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

            # If action is savegame
            elif command.lower() == "savegame":
                game1.save_game()
                moved_rooms = False

            # If action is loadame
            elif command.lower() == "loadgame":
                game1.load_game()

            # If action is health
            elif command.lower() == "health":
                game1.health_status(player1)
                
            # If action is exit
            elif command.lower() == "exit":
                game1.list_exit(player1.location)
                
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
                    # Calculate players new health with each move
                    # TODO need to determine how each action affects health
                    # TODO may want to move to actions aftering deciding how actions affect health levels
                    # currently an incorrect room choice will decrease health
                    # currently moved here to prevent non-action commands or incorrect cmds from decresing health
                    player1.player_status()        
                    
                else:
                    # Check command was not an exit name
                    for room in game1.rooms:
                        if command.lower() in room.east_exits or command.lower() in room.west_exits or command.lower() in room.north_exits or command.lower() in room.south_exits:
                            # change command to use_on
                            use_on = command
                            # change command to go
                            command = "go"
                            # call move_room function in actions to get next room
                            next_room = move_room(use_on,current_room, game1.rooms, player1)
                            # call moved_locations to try to move to that room
                            moved_rooms = moved_locations(next_room,player1)
                    
                    # If action is not in list of verbs or an exit name, print error message
                    if command != "go" and moved_rooms == False:
                        print("Error: not a valid action. Type <help> to see valid verbs")
                    else:
                       player1.player_status()  


        # Check for game status
        game1.check_game_status(player1)

if __name__ == "__main__":
    main()

