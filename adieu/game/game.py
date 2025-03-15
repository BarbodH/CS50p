import random

# Prompt the user for a valid level (positive integer)
while True:
    level_input = input("Level: ")

    # Check if the input is numeric
    if level_input.isdigit():  # isdigit() checks if the input is a valid number
        level = int(level_input)
        if level > 0:
            break  # Exit the loop if the level is a valid positive integer
        else:
            print("Please enter a positive integer.")
    else:
        print("Invalid input. Please enter a valid positive integer.")

# Generate a random integer between 1 and the level (inclusive)
secret_number = random.randint(1, level + 1)

# Prompt the user to guess the number
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < secret_number:
                print("Too small!")
            elif guess > secret_number:
                print("Too large!")
            else:
                print("Just right!")
                break  # Exit the loop when the guess is correct
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
