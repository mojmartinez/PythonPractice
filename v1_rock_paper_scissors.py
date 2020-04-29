print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make you move: ")
player2 = input("Player 2, make you move: ")

if player1 == "rock" and player2 == "scissors":
    print("Player One Wins!")
elif player1 == "rock" and player2 == "paper":
    print("Player Two Wins!")
elif player1 =="paper" and player2 == "rock":
    print("Player One Wins!")
elif player1 == "paper" and player2 == "scissors":
    print("Player Two Wins!")
elif player1 == "scissors" and player2 == "rock":
    print("Player Two Wins!")
elif player1 == "scissors" and player2 == "paper":
    print("Player One Wins!")
elif player1 == player2:
    print("It's a Tie!")
else: 
    print("Something went Wrong")