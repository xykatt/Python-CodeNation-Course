from cn_game_extras import qa_until, type_print

from nigel import play_yellow_section
from yussuf import play_green_section
from jarrod import play_blue_section
from kat import play_purple_section

player_is_alive = True
playing_game = True

#Game play loop
while playing_game :

    #Announce the beginning of the game
    type_print("\nBreaking News of Zombie Virus\n\n",0.01)

    #check game design documentation flowchart to understand these colours
    if player_is_alive == True :
        player_is_alive = play_yellow_section()

    if player_is_alive == True :
        player_is_alive = play_green_section()

    if player_is_alive == True :
        player_is_alive = play_blue_section()

    if player_is_alive == True :
        player_is_alive = play_purple_section()
   

    #if we are here and the player_is_alive then they when
    if player_is_alive == True :
        type_print("\n\nYou survived and have saved humanity\n")
    else:
        type_print("\n\nYou are dead\nGame Over.\n")

    #ask if the player wants to play again
    yn = qa_until("Do you want to play again", ["Y","N"])

    # if yn was "Y" reset game to play again
    if yn == 0:
        playing_game = True
        player_is_alive = True
    else:
        playing_game = False
        player_is_alive = False        

print("Goodbye")
