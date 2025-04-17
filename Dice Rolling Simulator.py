import random

roll = random.randint(1, 6)
print("You rolled a", roll)
num_rolls = int(input("How many times do you want to roll the dice? "))

for i in range(num_rolls):
    roll = random.randint(1, 6)
    print(f"Roll {i + 1}: You rolled a {roll}")
    play_again = (
        input("\nDo you want to roll the dice again? (yes/no): ").strip().lower()
    )
    if play_again != "yes":
        print("\nThanks for playing! Goodbye!")
        break
