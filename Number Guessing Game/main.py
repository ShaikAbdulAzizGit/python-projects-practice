from random import randint
computer_guess=randint(1,100)
guesses=0
while True:
    guesses+=1
    try:
        user_choice=int(input("Guess the number !.."))
        if user_choice<=0 or user_choice>100:
            print("Please guess the number between 0 to 100")
            continue
        if user_choice<computer_guess:
            print("Too low !..")
        elif user_choice>computer_guess:
            print("Too High !..")
        else:
            print(f"Congratulations You won and the number is {computer_guess}")
            print(f"You got it on {guesses} guesses")
            break
    except ValueError:
        print("Invalid value please try again !..")
