import random

VALID_CHOICES = ("rock", "paper", "scissors", "Spock", "Lizard")

WIN_COMBO = (
    ("rock", "scissors"),
    ("rock", "Lizard"),
    ("paper", "rock"),
    ("paper", "Spock"),
    ("scissors", "paper"),
    ("scissors", "Lizard"),
    ("Spock", "rock"),
    ("Spock", "scissors"),
    ("Lizard", "paper"),
    ("Lizard", "Spock"),
)


def prompt(msg):
    print(f"==> {msg}")


def display_winner(choice, computer_choice):
    prompt(f"You chose {choice}, computer chooses {computer_choice}")

    if (choice, computer_choice) in WIN_COMBO:
        prompt('You win!')
    elif choice == computer_choice:
        prompt('It\'s a tie!')
    else:
        prompt('You loose!')


answer = "y"
while answer[0] == "y":
    prompt(f'Choose one: {', '.join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That is not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()
    while answer and answer[0] not in ["y", "n"]:
        prompt('Please enter "y" or "n"')
        answer = input().lower()
