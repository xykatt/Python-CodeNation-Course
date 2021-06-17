def print_bridge():
    
        print ("""
        \u001b[32m         @\_______/@
                @|XXXXXXXX |
               @ |X||    X |
              @  |X||    X |
             @   |XXXXXXXX |
            @    |X||    X |             \u001b[0mV\u001b[32m
           @     |X||   .X |
          @      |X||.  .X |                      \u001b[0mV\u001b[32m
         @      |0XXXXXXXX0||
        @       |X||  . . X||
                |X||   .. X||                               @     @
                |X||  .   X||.                              ||====%
                |X|| .    X|| .                             ||    %
                |X||.     X||   .                           ||====%
               |XXXXXXXXXXXX||     .                        ||    %
               |XXXXXXXXXXXX||         .                 .  ||====% .
               |XX|        X||                .        .    ||    %  .
               |XX|        X||                   .          ||====%   .
               |XX|        X||              .          .    ||    %     .
               |XX|======= X||============================+ || .. %  ........
        ===== /            X||                              ||    %
                           X||           /)                 ||    %
        \u001b[34m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\u001b[0m
        """)

import time,sys
from cn_game_extras import qa

def play_blue_section():

    print("While on your way, you come to another fork in the road.")
    print("One a road leading to a bridge, the second leading to an off road path.")
    a = qa("Which way do you go (Offroad, Bridge)? ", "Bridge", "Offroad")
    # text after right path after off road
    if a == True :
        print_bridge()
        time.sleep(3) # text after choosing to go over the bridge
        print("You decide that the bridge is the best way, you can see the strong hold in the distance.")
        time.sleep(0.5)
        print("But while in the middle of the bridge you come to a lot of parked cars")
        time.sleep(0.5)
        print("The added weight of your RV and the parked cars causes the bridge to collapse.")
        time.sleep(1)
        message = "You fall from a great height, \u001b[31mleading to your death.\u001b[0m"
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        # return false is we died and true if still alive
        return False
    else:
        print("You decide Off-Road")
        return True
