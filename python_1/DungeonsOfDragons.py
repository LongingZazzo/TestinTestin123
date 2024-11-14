def SweetDreamsEND():
    """
    This function handles the 'Sweet Dreams' ending where the player eats the fruit
    and decides to rest.
    """
    print("You eat the fruit and start to feel sleepy; you decide to rest your eyes for a bit.")
    print("You got the 'Sweet Dreams' ending.")

def LargeRoom():
    """
    This function represents the scene where the player enters a large room with fruits.
    It prompts the user to decide whether to eat the fruit or leave the room.
    """
    print("You enter a large room with weird-looking fruits sitting in bushes.")
    print("You're feeling a little hungry. Do you try the fruit?")
    
    user_choice = get_user_choice(["eat", "leave"])
    if user_choice == "eat":
        SweetDreamsEND()
        return "sweet_dreams"

def Weapons():
    """
    This function represents the scene where the player finds a stash of weapons after
    following the kobold. More choices can be added here.
    """
    print("You follow the Kobold and find a stash of weapons. What do you do next?")
    # Add more choices and outcomes here

def OuttaHereEND():
    """
    This function handles the 'Outta Here' ending where the player decides to leave and
    go back home.
    """
    print("You leave and go back home to your cat Waffles.")
    print("You got the 'Outta Here' ending.")

def introScene():
    """
    This function starts the game by asking the player whether they want to enter or leave.
    It leads to different outcomes based on the player's choice.
    """
    print("You awaken at a dungeon door. What do you do?")
    user_choice = get_user_choice(["go in", "leave"])
    
    if user_choice == "leave":
        OuttaHereEND()
        return "outta_here"
    elif user_choice == "go in":
        return "go_in"

def AttackScene():
    """
    This function presents the player with an attack scene, where they must choose whether
    to fight or run from a kobold. It leads to different paths depending on the player's decision.
    """
    print("You go inside and immediately get attacked by a kobold.")
    
    user_choice = get_user_choice(["fight", "run"])
    if user_choice == "run":
        print("You run away like a coward.")
        print("You got the 'Coward' ending.")
        return "coward_ending"
    elif user_choice == "fight":
        print("You kick the kobold and step on its tail; it runs away.")
        return follow_or_continue()

def follow_or_continue():
    """
    This function asks the player whether to follow the kobold or continue forward.
    Each choice leads to a different outcome.
    """
    print("Do you follow it or continue forward?")
    user_choice = get_user_choice(["follow", "continue"])
    
    if user_choice == "follow":
        Weapons()
    elif user_choice == "continue":
        LargeRoom()

def get_user_choice(options):
    """
    This function displays a list of options and waits for the user to input a valid choice.
    It ensures the input is one of the options provided.
    """
    user_choice = ""
    while user_choice not in options:
        print("Choices: " + "/".join(options))
        user_choice = input().strip().lower()
    return user_choice

def main():
    """
    This function is the main entry point of the game. It handles the game flow and 
    repeats until the player chooses to stop.
    """
    print("Welcome to Dungeons Of Dragons")
    print("Or better known as DOD")
    print("This is a text-based game where your choices will determine your endings.")
    print("This is part 1: Stray Hero")
    print("How about we start with a name:")
    
    player_name = input().strip()  # String variable for the player's name
    print("Safe travels, " + player_name + "!")
    
    # List of possible outcomes
    game_endings = ["coward_ending", "sweet_dreams", "outta_here"]
    
    while True:
        scene_result = introScene()
        
        if scene_result == "outta_here":
            if not play_again():
                break
        
        elif scene_result == "go_in":
            attack_result = AttackScene()
            if attack_result in game_endings:  # Check if the game ended
                if not play_again():
                    break

def play_again():
    """
    This function asks the player whether they want to play again.
    It returns a boolean value indicating their choice.
    """
    replay = input("Would you like to play again? (yes/no): ").strip().lower()
    return replay == 'yes'

if __name__ == "__main__":
    main()
