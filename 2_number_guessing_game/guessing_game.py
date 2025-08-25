import random  # Import the random module to generate random numbers


def guessing_game():
    attempts = 0
    secret_number = random.randint(1, 100)  # Generate random number between 1-100

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Make a guess:"))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(
                    f"Congratulations! You've guessed it in {attempts} attempts!")
                break
        except ValueError:  
            print("Please enter a valid number!") # Handle invalid input (non-numbers)


guessing_game()

"""
A number guessing game where the player tries to guess a random number between 1-100.
The game provides feedback (too high/too low) and counts attempts.
"""
