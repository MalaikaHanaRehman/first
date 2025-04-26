import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        # Get the player's guess
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        # Check if the guess is correct
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

    # If the player runs out of attempts
    if attempts == max_attempts:
        print(f"\nSorry, you've run out of attempts. The number was {secret_number}. Better luck next time!")

# Run the game
guess_the_number()