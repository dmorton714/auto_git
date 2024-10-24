import random
from auto_git import main

choices = ["rock", "paper", "scissors"]
user = input("Choose rock, paper, or scissors: ").lower()
computer = random.choice(choices)

if user == computer:
    print(f"Both chose {user}. It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print(f"You win! {user} beats {computer}.")
else:
    print(f"You lose! {computer} beats {user}.")



main()
