def simple_madlib():
    print("Let's play Mad Libs!")

    # Get user inputs
    animal = input("Enter an animal: ")
    color = input("Enter a color: ")
    food = input("Enter a food: ")
    place = input("Enter a place: ")

    # Simple Mad Libs story
    story = f"""
    One day, a {color} {animal} went to {place} to eat {food}.
    Everyone was so surprised to see a {color} {animal} eating {food} in {place}!
    """

    # Print the story
    print("\nHere's your Mad Libs story:\n")
    print(story)

# Run the Mad Libs game
simple_madlib()