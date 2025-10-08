import random 
symbols=['🍒','🍋','💎']

MIN_LINE=1
MAX_LINE=3

MIN_POINTS=10
MAX_POINTS=100

MIN_SPEND=10

total_points=100

def user_deposit():
    global total_points
    if total_points==100:
        print(f"Already total points reached to max limit {MAX_POINTS}")
        return
    while True:
        try:
            points=int(input(f"Enter points you want to add between {MIN_POINTS} - {MAX_POINTS}"))
            if MIN_POINTS <= points <=MAX_POINTS:
                
                total_points+=points
                print(f"{points} added successfully , Total points : {total_points}")
                return
            else:
                print(f"Unable to add points please addd between {MIN_POINTS} - {MAX_POINTS}")
        except ValueError:
            print("Please enter a valid number !..")

def spin():
    global total_points
    while True:
        try:
            no_of_lines=int(input("Enter the number of lines you want to guess !.. :"))
            if MIN_LINE <= no_of_lines <= MAX_LINE:
                lines_won=0

                while True:
                    points=int(input("How many points you want to use for each line ?.. :"))
                    if points<MIN_SPEND:
                        print(f"SOrry minimum spend is {MIN_SPEND}")
                        continue
                    if points*no_of_lines>total_points:
                        print(f"Unable to use {points} , Total points {total_points}")
                        deposit=input("Enter d to deposit points : ").strip().lower()
                        if deposit=='d':
                            user_deposit()
                        else:
                            print("Deposit cancelled !.")
                    else:
                        print(f"You are using {points} for {no_of_lines} line , Total spend : {points*no_of_lines} ")
                        for _ in range(no_of_lines):
                            first=random.choice(symbols)
                            second=random.choice(symbols)
                            third=random.choice(symbols)
                            print(f"{first} | {second} | {third}")
                            if first==second==third:
                                lines_won+=1
                            else:
                                total_points-=points
                        points_won=(points*2)*lines_won
                        total_points+=points_won
                        print(f"You won {points_won} , Total points: {total_points}")
                        return lines_won
            else:
                print("Please enter valid lines in limit 1-3")
                continue
        except ValueError:
            print("Please enter a valid number !.")
            
def main():
    while True:
        user_choice=input("Press enter to continue , d to depost , q to quit :").strip().lower()
        if user_choice=="":
                spin()
        elif user_choice=='d':
            deposit=input(f"You have {total_points} points do you want to deposit (y/n) :").strip().lower()
            if deposit=='y':
                user_deposit()
            else:
                print("Deposit Cancelled")
        elif user_choice=='q':
            print("Have a nice day !.")
            break
        else:
            print("Invalid selection please press enter to start or select q to quit :")



print("Welcome to Lucky match game !..")
print(f"You have free {total_points} points to start !.")

start=input("Press enter to start : ").strip()
if start=="":
    main()
else:
    print("You quit the game !.")