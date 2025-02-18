print("Welcome to Quiz Game")
playing = input("Do you to play the game? (yes/no)")
if playing.lower() != "yes":
    print("sorry to see you going")
    quit()
print("okay let's play a game")
answer = input("What does Cpu stands for")
score = 0
if answer.lower() == "central processing unit":
    print("corret")
    score += 5
else:
    print("incorrect")
answer = input("Which protocol is primarily used for transferring web pages over the internet?")
score = 0
if answer.lower() == "http":
    print("corret")
    score += 5
else:
    print("incorrect")
answer = input("What does RAM stands for")
score = 0
if answer.lower() == "random access memory":
    print("corret")
    score += 5
else:
    print("incorrect")
answer = input("What does Gpu stands for")
score = 0
if answer.lower() == "graphics processing unit":
    print("corret")
    score += 5
else:
    print("incorrect")
print(f"your score is {score}")
