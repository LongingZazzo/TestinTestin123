def introScene():
        print("You awaken at a dungeon door, what do you do?")
        options = ["go in", "leave"]
        userInput = ""
        while userInput not in options:
            print("Choices: Go in/leave")
            userInput = input()
            if userInput == "leave":
                print("You leave and go home back to your cat Waffles")
                print("You got the 'Outta here' ending")
            if userInput == "go in":
                 AttackScene()
def AttackScene():
     print("You go inside and immediately get attacked by a kobolt")
     options = ["Fight","Run"]
     userInput = ""
     while userInput not in options:
          print("Choices: Fight/Run")
          userInput = input()
          if userInput == "run":
               print("You run away like a coward. You got the 'Cowards' ending")
          if userInput == "fight":
               print("You kick the Kobolt and step on its tail, it runs away")
if __name__ == "__main__":
    #While True:
    print("Welcome to Dungeons Of Dragons")
    print("Or better known as DOD")
    print("This is a text based game where your choices will determen your endings")
    print("This is part 1: Stray Hero")
    print("How about we start with a name:")
    name= input()
    print("Safe travels, " +name+ "")
    introScene()