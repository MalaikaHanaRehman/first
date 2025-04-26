import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: rock, paper, or scissors.")

    # Define the choices
    choices = ["rock", "paper", "scissors"]

    # Get the player's choice
    player_choice = input("Your choice: ").lower()

    # Validate the player's choice
    if player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    # Computer makes a random choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

# Run the game
rock_paper_scissors()