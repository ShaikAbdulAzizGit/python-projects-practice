import random

ROCK='r'
PAPER='p'
SCISSOR='s'

map={
        'r':'Rock',
        'p':'Paper',
        's':'Scissors'
    }
choices=tuple(map.keys())


def user_input():
    while True:
        user_choice=input("Rock , Paper or Scissors (r,p,s) :").lower().strip()
        if user_choice not in choices:
            print("Invlaid choice please try again !..")
        else :
            return user_choice
def display_results(user_choice,computer_choice):
    print(f"You choose : {map[user_choice]}")
    print(f"Computer choose : {map[computer_choice]}")

def game_result(user_choice,computer_choice):
    if user_choice==computer_choice:
        print("Draw !..")
    elif (user_choice==ROCK and computer_choice==SCISSOR or
        user_choice==PAPER and computer_choice==ROCK or
        user_choice==SCISSOR and computer_choice==PAPER):
        print("You won!.")
    else:
        print("You lose!.")
        
def play_game():
    
    while True:
        user_choice=user_input()
        computer_choice=random.choice(choices)
        display_results(user_choice,computer_choice)
        game_result(user_choice,computer_choice)
        play_again=input("(y) for continue !..:").lower().strip()
        if play_again=='y':
            continue
        else:
            break


play_game()

