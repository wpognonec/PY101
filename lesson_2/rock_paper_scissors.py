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
        _choice = input("==> ").lower()

        if _choice in CHOICES:
            return CHOICES[_choice]
        if _choice in CHOICES.values():
            return _choice
        os.system(CLEAR)
        prompt(f"{_choice} is not a valid choice.")


def format_choice(_choice):
    if _choice == "spock":
        formatted_choice = "(Sp)ock"
    else:
        formatted_choice = f"({_choice[0].upper()}){_choice[1:]}"
    return formatted_choice


def get_winner(_choice, _computer_choice):
    if _computer_choice in WIN_COMBO[_choice]:
        return "player"
    if _choice == _computer_choice:
        return "tie"
    return "computer"


def display_winner(_winner):
    match _winner:
        case "player":
            prompt("You win!")
        case "computer":
            prompt("You loose!")
        case "tie":
            prompt("It's a tie!")


def update_scores(_winner, _scores):
    match _winner:
        case "player":
            _scores["player"] += 1
        case "computer":
            _scores["computer"] += 1


def display_score(_scores):
    prompt(f'The current score is {_scores["player"]}-{_scores["computer"]}')
    if _scores["player"] == 3:
        prompt("You have won the game!")
    elif _scores["computer"] == 3:
        prompt("The computer has won the game!")


def get_yes_no():
    while True:
        _choice = input("==> ").lower()
        if _choice not in ["y", "n"]:
            os.system(CLEAR)
            prompt("Please enter 'y' or 'n'")
        else:
            break
    return _choice

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
