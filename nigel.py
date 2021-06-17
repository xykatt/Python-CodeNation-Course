from cn_game_extras import qa_until, type_print

def play_yellow_section():

    #print_game_title_page()

    # question 1
    a = qa_until("Will you join the Quest to save mankind ", ["Yes", "No"])

    if a == 1 :
        type_print("You choice is to stay at home to survive, but the Zombie broke into your home and ate you",0.01)
        player_is_alive = False
    else:
        # question 2
        a= qa_until("Travel preparation, equipment and maps. Choose vehicle ", ["Car", "RV"])

        if a == 0 :
            type_print("You selected Car")
            type_print("Car is too loud and draws in the Zombies, who overwhelm your car and they eat you.",0.01)
            player_is_alive = False
        else:
            type_print("\nYou selected the RV, lets continue...")
            player_is_alive = True

    return player_is_alive
