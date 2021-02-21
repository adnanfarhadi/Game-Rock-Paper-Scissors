# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import  randint

def main():


    print("Rock...".lower())
    print("Paper...".lower())
    print("Scissors...".lower())
    print("------------------------")

    randomNumber = randint(0, 2)
    computerMove = "rock"

    if randomNumber == 0:
        computerMove = "rock"
    elif randomNumber == 1:
        computerMove = "paper"
    elif randomNumber == 2:
        computerMove = "scissors"

    Player_1 = input("Player_1 , Make Your Move : ").lower()
    Player_2 = computerMove
    print(f"Player_2 , Make Your Move :{computerMove} ")

    if Player_1 == Player_2:
        print("Thats a tie ...")
    elif Player_1 == "rock":
        if Player_2 == "scissors":
            print("player_1 wins!...")
        elif Player_2 == "paper":
            print("player_2 wins!...")
    elif Player_1 == "paper":
        if Player_2 == "rock":
            print("player_1 wins!...")
        elif Player_2 == "scissors":
            print("player_2 wins!...")
    elif Player_1 == "scissors":
        if Player_2 == "paper":
            print("player_1 wins!...")
        elif Player_2 == "rock":
            print("player_2 wins!...")
    else:
        print("something went worng...")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
