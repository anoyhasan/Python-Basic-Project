import random


def game_play():
    choices = ["Rock", "Paper", "Scissors"]
    user_choices = input("Choose Rock, Paper, Scissors : ").title()
    cumputer_choices = random.choice(choices)

    print(f"Cumputer choose : {cumputer_choices}")

    if user_choices == cumputer_choices:
        print("It's a tie!")
    elif (
        (user_choices == "Rock" and cumputer_choices == "Scissors")
        or (user_choices == "Scissors" and cumputer_choices == "Paper")
        or (user_choices == "Paper" and cumputer_choices == "Rock")
    ):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")


game_play()
