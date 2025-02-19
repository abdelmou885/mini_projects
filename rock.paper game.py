import random

options = ["rock", "paper", "scissor"]
user_wins = 0
computer_wins = 0
trials =5
while True:
    print(f"you have only {trials} tries")
    player_input=input(" rock, paper, scissor or q to quit: ").lower()
    trials=trials-1
    if player_input == "q":
        print("sorry to see you go")
        break
    if player_input not in options:
        print("it's not a valid option")
        continue
    random_choice = random.choice(options)
    if player_input == "rock" and random_choice == "scissor":
        print("you won")
        user_wins +=1
    elif player_input == "paper" and random_choice == "rock":
        print("you won")
        user_wins += 1
    elif player_input == "scissor" and random_choice == "paper":
        print("you won")
        user_wins += 1
    else:
        print("you lost")
        computer_wins += 1
    if trials== 0 :
        print("you finished the game")
        break
print(f"you won {user_wins} times and lost {computer_wins}")
print("Game Over")