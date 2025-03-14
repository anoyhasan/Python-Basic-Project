import random

print("Number Guessing Game")


def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if guess > number:
            print("Too high! Try again.")
        elif guess < number:
            print("Too low! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
            break


guess_the_number()