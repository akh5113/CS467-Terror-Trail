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

        # varaible to loop back if invalid input
        successful_action = False

        while successful_action is False:
            # Get user input
            user_input = input(prompt)
            # Split user input into command , preposition, object/feature/room
            split_input = user_input.split()
            # First is the command
            command = split_input[0]
            # Determine if there was a preposition
            if len(split_input) == 2:
                # No preposition
                use_on = split_input[1]
                preposition = ""
            # If there is prepostion
            elif len(split_input) == 3:
                preposition = split_input[1]
                use_on = split_input[2]
            # If there is a one word command, others are empty
            else:
                use_on = ""
                preposition = ""

            # If action is moving rooms
            basic_move_cmds = ["go","move","walk","exit","travel","cross"]
            if command.lower() in basic_move_cmds:
                # call move room action function to get next room
                next_room = move_room(use_on, current_room, game1.rooms, player1)
                # if no matching room found
                if next_room == None: 
                    # Then invalid command
                    print("It doesn't look like you currently can or want to go that way. Try a different exit.")
                # if there is a matching room
                else:
                    # move player to room
                    player1.location = next_room
                    print("Moved to", player1.location.name)
                    successful_action = True

            # If action is help
            elif command.lower() == "help":
                game1.help()

            # If action is quit
            elif command.lower() == "quit":
                game1.quit_game()
                successful_action = True

            # If action is look
            elif command.lower() == "look" and preposition == "":
                # call function to print long form explanation of the room
                look(current_room)
                successful_action = True
            
            # If action is look at
            elif command.lower() == "look" and preposition.lower() == "at":
                # call function to explain feature or object
                if look_at(use_on,player1,current_room,game1.rooms):
                    successful_action = True
                # if look at not sucessful
                else:
                    print("What you're trying to look at isn't here. Try looking at something else")
                    successful_action = False
                    
            # If action is not changing room, figure out what it is doing
            else:
                # Get verbs for the room
                possible_actions = current_room.get_verbs()
                # Determine if the action is possible given the objects/features
                if user_input in possible_actions:
                    determine_action(player1, command, use_on)
                    # Adding a break here to not get stuck!
                    successful_action = True
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

