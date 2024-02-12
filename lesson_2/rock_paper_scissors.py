import random
import os

CHOICES = {
    "r": "rock",
    "p": "paper",
    "s": "scissors",
    "l": "lizard",
    "sp": "spock",
}

WIN_COMBO = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["rock", "scissors"],
}

CLEAR = "cls" if os.name == "nt" else "clear"


def prompt(msg):
    print(f"==> {msg}")


def get_choice():
    while True:
        prompt(
            "Choose one: "
            + ", ".join([format_choice(item) for item in CHOICES.values()])
        )
        choice = input("==> ").lower()

        if choice in CHOICES:
            return CHOICES[choice]
        if choice in CHOICES.values():
            return choice
        os.system(CLEAR)
        prompt(f"{choice} is not a valid choice.")


def format_choice(choice):
    if choice == "spock":
        formatted_choice = "(Sp)ock"
    else:
        formatted_choice = f"({choice[0].upper()}){choice[1:]}"
    return formatted_choice


def get_winner(choice, computer_choice):
    if computer_choice in WIN_COMBO[choice]:
        return "player"
    if choice == computer_choice:
        return "tie"
    return "computer"


def display_winner(winner):
    match winner:
        case "player":
            prompt("You win!")
        case "computer":
            prompt("You loose!")
        case "tie":
            prompt("It's a tie!")


def update_scores(winner, scores):
    match winner:
        case "player":
            scores["player"] += 1
        case "computer":
            scores["computer"] += 1


def display_score(scores):
    prompt(f'The current score is {scores["player"]}-{scores["computer"]}')
    if scores["player"] == 3:
        prompt("You have won the game!")
    elif scores["computer"] == 3:
        prompt("The computer has won the game!")


def get_yes_no():
    while True:
        choice = input("==> ").lower()
        if choice not in ["y", "n"]:
            os.system(CLEAR)
            prompt("Please enter 'y' or 'n'")
        else:
            break
    return choice


def display_rules():
    prompt('''Best of 3 wins.
    - Scissors cuts Paper
    - Paper covers Rock
    - Rock crushes Lizard
    - Lizard poisons Spock
    - Spock smashes Scissors
    - Scissors decapitates Lizard
    - Lizard eats Paper
    - Paper disproves Spock
    - Spock vaporizes Rock
    - Rock crushes Scissors
    ''')


def intro():
    os.system(CLEAR)
    prompt("Welcome to Rock Paper Scissors Lizard Spock!")
    prompt("Would you like to see the rules? (y/n)")
    choice = get_yes_no()
    if choice[0] == "y":
        display_rules()
    play()


def play():
    while True:
        scores = {"player": 0, "computer": 0}
        while scores["player"] != 3 and scores["computer"] != 3:
            choice = get_choice()
            computer_choice = random.choice(list(CHOICES.values()))

            os.system(CLEAR)
            prompt(f"You chose {choice}, computer chooses {computer_choice}")
            winner = get_winner(choice, computer_choice)
            display_winner(winner)
            update_scores(winner, scores)
            display_score(scores)

        prompt("Would you like to play again? (y/n):")
        choice = get_yes_no()
        if choice[0] == "n":
            break

intro()
