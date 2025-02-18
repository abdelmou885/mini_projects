import random
number=random.randint(1,20)
guesses=0
while True:
    guesses +=1
    user_number=int(input("Enter a number between 1 and 20: "))
    if user_number==number:
        print("You guessed the number!")
        break
    elif user_number>number:
        print("Your guessed number is higher")
    else:
        print("Your guessed number is lower")
print(f"You have got it in {guesses} guesses")
