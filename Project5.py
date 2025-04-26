import random

def hangman():
    print("Welcome to Hangman!")

    # List of words for the game
    words = ["python", "programming", "hangman", "computer", "algorithm", "developer"]

    # Randomly select a word
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6  # Number of attempts allowed

    print("The word has", len(secret_word), "letters.")

    while attempts > 0:
        # Display the current state of the word
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print("\nWord:", display_word)

        # Check if the word has been fully guessed
        if "_" not in display_word:
            print("Congratulations! You guessed the word:", secret_word)
            break

        # Get the player's guess
        guess = input("Guess a letter: ").lower()

        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Add the guessed letter to the list
        guessed_letters.append(guess)

        # Check if the guessed letter is in the secret word
        if guess not in secret_word:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        # Display the hangman progress (optional)
        if attempts == 5:
            print("  O  ")
        elif attempts == 4:
            print("  O  ")
            print("  |  ")
        elif attempts == 3:
            print("  O  ")
            print(" /|  ")
        elif attempts == 2:
            print("  O  ")
            print(" /|\\ ")
        elif attempts == 1:
            print("  O  ")
            print(" /|\\ ")
            print(" /   ")
        elif attempts == 0:
            print("  O  ")
            print(" /|\\ ")
            print(" / \\ ")

    # If the player runs out of attempts
    if attempts == 0:
        print("\nYou ran out of attempts! The word was:", secret_word)

# Run the game
hangman()