import random
import sys
import time

def rock_paper_scissors():
    """This is a simple game of Rock, Paper, Scissors. The rules are based on the classic Rock,
Paper Scissors game."""
    wins = 0
    losses = 0
    ties = 0

    print("Welcome to the Rock, Paper, Scissors Game by Euler.")
    while True:
        print(f"\n📑📑📑 Wins: {wins}     Losses: {losses}     Ties: {ties}")
        print("\nEnter 'r' for ROCK 🪨, 'p' for PAPER 📄, 's' for SCISSORS ✂ or 'q' to Quit ❌.")
        
        # Takes user choice and ensures input is valid.
        while True:
            user_choice = input('Your move: ').lower()
            if user_choice == 'r':
                user_choice = 'ROCK 🪨'
                break
            elif user_choice == 'p':
                user_choice = 'PAPER 📄'
                break
            elif user_choice == 's':
                user_choice = 'SCISSORS ✂️'
                break
            elif user_choice == 'q':
                print("Bye, hoping to see you soon.")
                sys.exit()
            else:
                print("Invalid Input!")
        
        # Dsiplays user choice and awaits suspense.
        print(f"{user_choice} versus ...")
        
        # Assigns a random choice to the computer.
        computer_choice = random.choice(['ROCK 🪨', 'PAPER 📄', 'SCISSORS ✂' ])
        
        # Pause for suspense.
        time.sleep(1)
        
        # Displays the choices of both user and computer.
        print(f"\n{user_choice}  versus {computer_choice}.")

        # Another pause for suspense.
        time.sleep(1)
        
        # Determines the outcome of the round.
        if computer_choice == user_choice:
            print("It's a Tie!")
            ties += 1
        elif user_choice == "PAPER 📄" and computer_choice == "ROCK 🪨":
            print("\nYAY, YOU WIN.")
            wins += 1
        elif user_choice == "SCISSORS ✂️" and computer_choice == "ROCK 🪨":
            print("\nYAY, YOU LOSE.")
            losses += 1
        elif user_choice == "ROCK 🪨" and computer_choice == "PAPER 📄":
            print("\nYAY, YOU LOSE.")
            losses += 1
        elif user_choice == "SCISSORS ✂️" and computer_choice == "PAPER 📄":
            print("\nYAY, YOU WIN.")
            wins += 1
        elif user_choice == "ROCK 🪨" and computer_choice == "SCISSORS ✂":
            print("\nYAY, YOU WIN.")
            wins += 1
        elif user_choice == "PAPER 📄" and computer_choice == "SCISSORS ✂":
            print("\nYAY, YOU LOSE.")
            losses += 1
        
        # Initiates a new round for the game.
        print("\n\nLet's go again!")

rock_paper_scissors()
