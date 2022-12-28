import random

choices = ["Rock", "Paper", "Scissors"]

while True:
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("Rock, Paper, Scissors?: ").capitalize()
    print("Computer : ", computer)
    print("Player : ", str(player))
    if computer == player:
        print("Tie!")
    elif computer == 'Rock':
        if player == "Paper":
            print("You win!")
        else:
            print("Computer win!")
    elif computer == 'Paper':
        if player == "Scissors":
            print("You win!")
        else:
            print("Computer win!")
    elif computer == 'Scissors':
        if player == "Rock":
            print("You win!")
        else:
            print("Computer win!")

    play_again = input("Play again? (yes/no) : ").capitalize()
    if play_again != "Yes":
        break
# help("modules")