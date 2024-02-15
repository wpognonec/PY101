import random
import os
import json

with open('rps_strings.json', 'r') as file:
    DATA = json.load(file)

CHOICES: dict = DATA["choices"]
WIN_COMBO: dict = DATA["win_combos"]
CLEAR = "cls" if os.name == "nt" else "clear"

def prompt(msg):
    print(f"==> {msg}")

def input_choice():
    while True:
        formatted_choices = [format_choice(item, parens=True)
                             for item in CHOICES.values()]
        prompt("Choose one: " + ", ".join(formatted_choices))
        choice = input("==> ").lower()

        if choice in CHOICES:
            return CHOICES[choice]
        if choice in CHOICES.values():
            return choice
        prompt(
            f"{choice} is not a valid choice." if choice
            else "You must enter a choice"
        )

def input_yes_no():
    while True:
        choice = input("==> ").lower()
        if choice not in ["y", "n"]:
            prompt("Please enter 'y' or 'n'")
        else:
            break
    return choice

def format_choice(choice: str, parens=False):
    if parens and choice == "spock":
        formatted_choice = "(Sp)ock"
    elif parens:
        formatted_choice = f"({choice[0].upper()}){choice[1:]}"
    else:
        formatted_choice = f"{choice[0].upper()+choice[1:]}"
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
            prompt("You lose!")
        case "tie":
            prompt("It's a tie!")

def display_score(scores):
    prompt(
        'The current score is '
        f'player: {scores["player"]} - computer: {scores["computer"]}'
    )
    if scores["player"] == 3:
        prompt("You have won the game!")
    elif scores["computer"] == 3:
        prompt("The computer has won the game!")

def display_choices(choice, computer_choice):
    prompt(
        f"You chose {format_choice(choice)}, "
        f"computer chooses {format_choice(computer_choice)}"
    )

def display_rules():
    prompt(DATA["rules"])

def update_scores(winner, scores):
    match winner:
        case "player":
            scores["player"] += 1
        case "computer":
            scores["computer"] += 1

def play_again(game_number):
    if game_number:
        prompt("Would you like to play again? (y/n):")
        choice = input_yes_no()
        if choice[0] == "n":
            prompt("Thank you for playing!")
            return False
    return True

def play_round(scores):
    prompt("Best of 3 wins!")
    choice = input_choice()
    computer_choice = random.choice(list(CHOICES.values()))

    os.system(CLEAR)
    display_choices(choice, computer_choice)
    winner = get_winner(choice, computer_choice)
    display_winner(winner)
    update_scores(winner, scores)
    display_score(scores)

def display_games_played(game_number):
    game_string = "games" if game_number > 1 else "game"
    prompt(f"You have played {game_number} {game_string} total!")

def intro():
    os.system(CLEAR)
    choices = [format_choice(item) for item in CHOICES.values()]
    prompt(f"Welcome to {" ".join(choices)}!")
    prompt("Would you like to see the rules? (y/n)")
    choice = input_yes_no()
    if choice[0] == "y":
        display_rules()

def main():
    game_number = 0
    intro()
    while play_again(game_number):
        scores = {"player": 0, "computer": 0}
        while scores["player"] != 3 and scores["computer"] != 3:
            play_round(scores)

        game_number += 1
        display_games_played(game_number)

main()
