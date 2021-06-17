def print_intro():
    print("__________                    .___             .__        ")
    print("\______   \_____    ____    __| _/____   _____ |__| ____  ")
    print(" |     ___/\__  \  /    \  / __ |/ __ \ /     \|  |/ ___\ ")
    print(" |    |     / __ \|   |  \/ /_/ \  ___/|  Y Y  \  \  \___ ")
    print(" |____|    (____  /___|  /\____ |\___  >__|_|  /__|\___  >")
    print("                \/     \/      \/    \/      \/        \/ ")
    print("   _____                              .__                              ")
    print("  /  _  \ ______   ____   ____ _____  |  | ___.__.______  ______ ____  ")
    print(" /  /_\  \\____ \ /  _ \_/ ___\\__  \ |  |<   |  |\____ \/  ___// __ \ ")
    print("/    |    \  |_> >  <_> )  \___ / __ \|  |_\___  ||  |_> >___ \\  ___/ ")
    print("\____|__  /   __/ \____/ \___  >____  /____/ ____||   __/____  >\___  >")
    print("        \/|__|               \/     \/     \/     |__|       \/     \/ ")
    print("  ________                       ")
    print(" /  _____/_____    _____   ____  ")
    print("/   \  ___\__  \  /     \_/ __ \ ")
    print("\    \_\  \/ __ \|  Y Y  \  ___/ ")
    print(" \______  (____  /__|_|  /\___  >")
    print("        \/     \/      \/     \/ ")
def print_hospital():
    print("                                                     ___")
    print("                                             ___..--'  .`.")
    print("                                    ___...--'     -  .` `.`.")
    print("                           ___...--' _      -  _   .` -   `.`.")
    print("                  ___...--'  -       _   -       .`  `. - _ `.`.")
    print("           __..--'_______________ -         _  .`  _   `.   - `.`.")
    print("        .`    _ /\    -        .`      _     .`__________`. _  -`.`.")
    print("      .` -   _ /  \_     -   .`  _         .` |cdc medical|`.   - `.`.")
    print("    .`-    _  /   /\   -   .`        _   .`   |___Center__|  `. _   `.`.")
    print("  .`________ /__ /_ \____.`____________.`     ___       ___  - `._____`|")
    print("    |   -  __  -|    | - |  ____  |   | | _  |   |  _  |   |  _ |")
    print("    | _   |  |  | -  |   | |.--.| |___| |    |___|     |___|    |")
    print("    |     |--|  |    | _ | |'--'| |---| |   _|---|     |---|_   |")
    print("    |   - |__| _|  - |   | |.--.| |   | |    |   |_  _ |   |    |")
    print(" ---``--._      |    |   |=|'--'|=|___|=|====|___|=====|___|====|")
    print(" -- . ''  ``--._| _  |  -|_|.--.|_______|_______________________|")
    print("`--._           '--- |_  |:|'--'|:::::::|:::::::::::::::::::::::|")
    print("_____`--._ ''      . '---'``--._|:::::::|:::::::::::::::::::::::|")
    print("----------`--._          ''      ``--.._|:::::::::::::::::::::::|")
    print("`--._ _________`--._'        --     .   ''-----..............LGB'")
    print("     `--._----------`--._.  _           -- . :''           -    ''")
    print("          `--._ _________`--._ :'              -- . :''      -- . ''")
    print(" -- . ''       `--._ ---------`--._   -- . :''")
    print("          :'        `--._ _________`--._:'  -- . ''      -- . ''")
    print("  -- . ''     -- . ''    `--._----------`--._      -- . ''     -- . ''")
    print("                              `--._ _________`--._")
    print(" -- . ''           :'              `--._ ---------`--._-- . ''    -- . ''")
    print("          -- . ''       -- . ''         `--._ _________`--._   -- . ''")
    print(":'                 -- . ''          -- . ''  `--._----------`--._")
def print_pothole():
    print(" ___  ,--.  __________________________/   ,   /_______")
    print("     'O---O'    .-----.")
    print("                `-- --'")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   ,--.   _ _ _ _ _")
    print("       _____                       ~'O---O'")
    print("_______<      |_____        __________________________")
    print("           ||      /   ,   /    ")

from cn_game_extras import qa

def play_green_section():
    # question 3
    a= qa("You drive out of your house, you have two choices to go left or right. Choose direction (left, right)?", "left", "right")
    if a == True:
        print("You have chosen to go left")
        print("While drive along, hit a pot hole and crashed, the loud noise alerted the Zombies and they eat you alive.")
        print_pothole()
        #player_is_alive == True for alive and False for dead. We died so 
        return False

    print("""Your decided to go right. On your way, you come to Medical Research Centre where an old 
            Doctor has found a Cure for the  Zombie Virus but is trapped. He entrusts you to deliver 
            the Cure to the human Survival strong hold""")
    print_hospital()
    # Question 4
    a = qa("After leaving the Medical Research Centre you come to a fork in the road do you go right or left?", "right", "left")
    if a == False:
        print("""after leaving the Medical research centre and driving to deliver the virus cure, you decide to go left and 
            hit a pot hole and crash. The loud noise draws the Zombie to you. The over run and eat you alive. """)
        print("You have Chosen to go left")
        print_pothole()
        #player_is_alive == True for alive and False for dead. We died so 
        return False

    #player_is_alive == True for alive and False for dead. We are still alive
    return True