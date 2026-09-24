import random

print("ROCK_PAPER_SCISSORS")

while True:

    user = input("Choose rock, paper or scissors: ").lower()

    computer = random.choice(["rock", "paper", "scissors"])

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif user == "rock" and computer == "scissors":
        print("You win!")

    elif user == "paper" and computer == "rock":
        print("You win!")

    elif user == "scissors" and computer == "paper":
        print("You win!")

    elif user in ["rock", "paper", "scissors"]:
        print("Computer wins!")

    else:
        print("Invalid choice. Please choose rock, paper or scissors.")

    again = input("Do you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break