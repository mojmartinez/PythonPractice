from random import randint

print("Rock...")
print("Paper...")
print("Scissors...")

player = input("Player, make you move: ").lower()

rand_num = randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer plays {computer}" )

if player == computer:
    print("It's a Tie!")
elif player == "rock":
    if computer == "scissors":
        print("Player Wins!")
    else:
        print("Computer Wins!")
elif player =="paper":
    if computer == "rock":
        print("Player Wins!")
    else:
        print("Computer Wins!")
elif player == "scissors": 
    if computer == "rock":
        print("Computer Wins!")
    else:
        print("Player Wins!")
else: 
    print("Please enter a valid move!")