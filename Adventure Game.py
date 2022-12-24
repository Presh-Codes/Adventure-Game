name = input("What is your name?\n")
print("Welcome", name, "to this game, would you like to continue with the adventure? Yes or No\n")
would_continue = input()
if would_continue.lower() == "yes":
    print("Alright. You're running down a field and get to a dead end")
    print("Would you climb over the wall or run back to find another way?")
    answer1 = input("Type 'climb' to climb over and 'turn' to run back\n").lower()
    if answer1 == "climb":
        print("You jumped over but landed inbetween a pack of lions. They ate you, so you lose!")
    elif answer1 == "turn":
        print("You turned around and ended up in a maze")
        print("would you like to go forward, to the right or to the left?")
        answer2 = input("Type 'F' to go forward, 'R' to move to the right or 'L' to move to the left\n").lower()
        if answer2 == "f":
            print("You got to a dead end and there's no way out, You lose!")
        elif answer2 == "r":
            print("You can either go left or right")
            answer3 = input("Type 'R' to go right or 'L' to go left").lower()
            if answer3 == "r":
                print("You got to a dead end and there's no way out, You lose!")
            elif answer3 == "l":
                print("You got to a dead end and there's no way out, You lose!")
            else:
                print("Invalid option, You lose!")
        elif answer2 == "l":
            print("You can either go left or right")
            answer4 = input("Type 'R' to go right or 'L' to go left").lower()
            if answer4 == "r":
                print("You got out of the maze successfully, then you got to a river")
                print("Would you swim across or go around it?")
                answer5 = input("Type 'swim' to swim across or 'go around' to go around").lower()
                if answer5 == "swim":
                    print()
                elif answer5 == "go around":
                    print()
                else:
                    print("Invalid option, You lose!")
            elif answer4 == "l":
                print("You got to a dead end and there's no way out, You lose!")
            else:
                print("Invalid option, You lose!")
        else:
            print("Invalid option, You lose!")
    else:
        print("Invalid option, You lose!")
else:
    print("Alright!")
    quit()