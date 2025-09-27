from random import randint

def roll():
    return randint(1,6)

print("Welcome to the Risk and Roll Game !..")

while True:
    try:
        players=int(input("Enter the number of players want to play the game (2-4) : "))
        if players == 1:
            print("Atleast 2 players required !..")
        elif players<1 or players >4:
            print("Players out of range")
        else:
            break
    except ValueError:
        print("Unexpected value please try again with integer ")

print(players)



MAX_SCORE=50
player_scores=[0 for _ in range(players)]



player_count=0
while max(player_scores)<=MAX_SCORE:
    print(f"Its Player {player_count+1} Turn ")
    while True:
        is_roll=input("Do you wanna roll (yes/no) : ").lower().strip()
        if is_roll == 'yes':
            value=roll()

            if value!=1:
                print(f"🎲 Player {player_count+1} rolled a value {value}")
                player_scores[player_count]+=value
                print(f"➡️ Player {player_count+1} score is {player_scores[player_count]}")

                if player_scores[player_count]>=50:
                    print(f"🏆 Player {player_count+1} won with the score {player_scores[player_count]}")
                    quit()
            else:
                player_scores[player_count]=0
                print(f"💀 Player {player_count+1} rolled  1 and the score resets to {player_scores[player_count]}")
                break
        elif is_roll=='no':
            print(f"🔄 Player {player_count+1} ends their turn with the score {player_scores[player_count]}")
            break
        else:
            print("Invalid selection please try again ")
            continue
    player_count = (player_count + 1) % players





