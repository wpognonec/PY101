import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(msg):
    print(f'==> {msg}')

def display_winner(choice, computer_choice):
    prompt(f'You chose {choice}, computer chooses {computer_choice}')

    if ((choice == 'rock' and computer_choice == 'scissors') or
        (choice == 'paper' and computer_choice == 'rock') or
        (choice == 'scissors' and computer_choice == 'paper')):
        prompt("You win!")
    elif ((choice == 'rock' and computer_choice == 'paper') or
        (choice == 'paper' and computer_choice == 'scissors') or
        (choice == 'scissors' and computer_choice == 'rock')):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

answer = 'y'
while answer[0] == 'y':
    prompt(f'Choose one: {', '.join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt('That is not a valid choice')
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)
    
    prompt("Do you want to play again (y/n)?")
    answer = input().lower()
    while answer and answer[0] not in ['y', 'n']:
        prompt('Please enter "y" or "n"')
        answer = input().lower()