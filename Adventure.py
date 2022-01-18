import time
import random


def print_pause(outcome):  # This function prints a outcome to the  screen
    print(outcome)  # and pauses for 2 secs before the next outcome
    time.sleep(2)


def intro(armory, enemy):   # This function calls the print_pause function
    print_pause("You are in a the battle field\n")
    print_pause(f"You Sense a { enemy } is somewhere around\n")
    print_pause("You move to a warehouse .\n")
    print_pause("To your right is a dark tunnel.\n")


def tunnel(armory, enemy):  # define tunnel activites
    if "rifle" in armory:
        print_pause("\nLooking for escape route.")
        print_pause("\nYou see a passage that"
                    "looks familiar")
        print_pause("\nYou go back to the field.")
    else:
        print_pause("\nStaring into the passage")
        print_pause("it is a tiny tunnel.")
        print_pause("\nYou check  your surrounding and "
                    "found a  Rifle")
        print_pause("\nYou walk out of the passage to the field.\n")
        armory.append("rifle")
    field(armory, enemy)


def house(armory, enemy):  # defines house activities
    print_pause("\nApproaching the house.")
    print_pause(f"\nYou knock and a {enemy}  comes out.")
    print_pause(f"\nThe {enemy} attacks  you!")
    while True:
        choice2 = input("\nDo you want to fight or "
                        "run?")
        if "fight" in choice2.lower():
            if "rifle" in armory:
                print_pause(f"\nThe {enemy}  attacks you, "
                            "you uncock your Rifle, "
                            "ready for the impending attack.")
                print_pause(f"\nYou aim at the { enemy}")
                print_pause(f"\nYou eliminate the  {enemy}"
                            ". You are victorious.")
            else:
                print_pause("\nFuck!!,")
                print_pause("\nYou were overpowered.")
                print_pause("\nYou lost.")
            play_again()
            break
        if "run" in choice2.lower():
            print_pause(f"You are determined to get{enemy}.")
            field(armory, enemy)
        else:
            print_pause("Sorry, I don't understand.")


def field(armory, enemy):   # Things that happen to the player in the field
    print_pause("Enter 1 to acess the house.")
    print_pause("Enter 2 to acess the tunnel.")
    print_pause("What would you like to do?")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1.lower() == "1":
            house(armory, enemy)
            break
        elif choice1.lower() == "2":
            tunnel(armory, enemy)
            break
        else:
            print_pause("Sorry, I don't understand")


def play_again():
    repeat = input("\nWould you like to play this"
                   " game again? (yes/no)").lower()
    if repeat == "yes":
        print_pause("\n\nRestarting  game ...\n\n")
        play_game()
    elif repeat == "no":
        print_pause("\nThanks for Playing!!.\n")
    else:
        play_again()


def play_game():
    armory = []
    enemies = ["Wolf", "Tiger", "Leopard", "Deer"]
    enemy = random.choice(enemies)
    intro(armory, enemy)
    field(armory, enemy)


play_game()
