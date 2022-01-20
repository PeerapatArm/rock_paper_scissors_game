import random
while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("Choose:").lower()
    if player == computer:
        print("computer:",computer)
        print("player:",player)
        print("draw")
    elif player == "rock":
        if computer == "paper":
            print("computer:",computer)
            print("player:",player)
            print("You lose")
        if computer == "scissors":
            print("computer:",computer)
            print("player:",player)
            print("You win")
    elif player == "paper":
        if computer == "scissors":
            print("computer:",computer)
            print("player:",player)
            print("You lose")
        if computer == "rock":
            print("computer:",computer)
            print("player:",player)
            print("You win")
    elif player == "scissors":
        if computer == "rock":
            print("computer:",computer)
            print("player:",player)
            print("You lose")
        if computer == "paper":
            print("computer:",computer)
            print("player:",player)
            print("You win")
    play_again = input("Do you want to play again? yes/no:").lower()
    if play_again == "no":
        break
print("See ya")
