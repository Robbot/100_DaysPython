from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
secret_number = random.randint(0,100)
#print(f"Psst, the correct answer is {secret_number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
def guess(attempts):
    while attempts != 0:
        guessed_number = int(input("Make a guess: "))

        if secret_number > guessed_number:
            print("Too low.")
        elif secret_number < guessed_number:
            print("Too high.")
        else:
            print(f"You got it! The answer was {secret_number}")
            exit()
        attempts = attempts - 1
        print(f"Guess again.\nYou have {attempts} remaining to guess the number.")
    if attempts == 0:
        print("You've run out of guesses, you lose.")
if difficulty == "easy":
    guess(10)
elif difficulty == "hard":
    guess(5)
else:
    print("Exit game")