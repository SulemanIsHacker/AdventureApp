type_name = input("Enter your name:\n")
print(f"Welcome {type_name} to the adventure game")
while True:
    answer = input(
        "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

    if answer.lower() == "left":
        answer = input(
            "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")
        if answer.lower() == "swim":
            print("You swam acrross and were eaten by an alligator.")
            want_play = input('Do you want to play again!:\n')
            if want_play.lower() == 'yes':
                continue
            else:
                print("Quiting the program.")
                quit()

        elif answer.lower() == "walk":
            print("You walked for many miles, ran out of water and you lost the game.")
            want_play = input('Do you want to play again!:\n')
            if want_play.lower() == 'yes':
                continue
            else:
                print("Quiting the program.")
                quit()
        else:
            print('Not a valid option. You lose.')
            want_play = input('Do you want to play again!:\n')
            if want_play.lower() == 'yes':
                continue
            else:
                print("Quiting the program.")
                quit()

    elif answer.lower() == "right":
        answer = input(
            "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
        if answer.lower() == "back":
            print("You go back and lose.")
            want_play = input('Do you want to play again!:\n')
            if want_play.lower() == 'yes':
                continue
            else:
                print("Quiting the program.")
                quit()
                
        elif answer.lower() == "cross":
            answer = input(
                "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
            if answer == "yes":
                print("You talk to the stanger and they give you gold. You WIN!")
            elif answer == "no":
                print("You ignore the stranger and they are offended and you lose.")
            want_play = input('Do you want to play again!:\n')
            if want_play.lower() == 'yes':
                continue
            else:
                print("Quiting the program.")
                quit()
    else:
        print('Not a valid option. You lose.')
        quit()

    print(f"Thanks for trying {type_name}")