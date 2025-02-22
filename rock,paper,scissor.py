#===ROCK-PAPER-SCISSORS-GAME===

import random 

print("Welcome to the Rock-Paper-Scissors game....!")
name = input("Enter your name : ")

Game = ["rock", "paper", "scissors"]
computer_input = random.choice(Game)

user_input = input(f"Hello {name} Enter your move i.e, rock , paper or scissors : ")

print(f"You have choosen {user_input} and Computer has choosen {computer_input}")

if (user_input == computer_input) :
    print("Computer and you have choosen the same move so it becomes a Tie!")

elif (user_input == "rock") :
    if (computer_input == "paper"):
        print("Computer wins! as paper covers rock")
    else :
        print(f"{name} wins! as rock smashes scissors")
    
elif (user_input == "paper") :
    if (computer_input == "scissors") :
        print("Computer wins! as scissors cuts paper")
    else :
        print(f"{name} wins! as paper covers rock")

elif (user_input == "scissor") :
    if(computer_input == "rock") :
        print("Computer wins! as rock smashes scissors")
    else :
        print(f"{name} wins! as scissors cuts paper")

print("Thanks for playing the game!!")