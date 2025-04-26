def computer_guess_the_number():
    print("Welcome to Guess the Number - Computer Edition!")
    print("Think of a number between 1 and 100, and I'll try to guess it!")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        # Computer makes a guess
        guess = (low + high) // 2
        attempts += 1

        # Ask the user for feedback
        print(f"\nIs your number {guess}?")
        feedback = input("Enter 'h' if it's too high, 'l' if it's too low, or 'c' if it's correct: ").lower()

        # Adjust the range based on feedback
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"Yay! I guessed your number in {attempts} attempts!")
            break
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")

    # If the range is exhausted
    if low > high:
        print("Hmm, something went wrong. Did you change your number?")

# Run the game
computer_guess_the_number()