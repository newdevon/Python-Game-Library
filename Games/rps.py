"""Rock Paper Scissors Implementation with 1v1 or User vs Ai

Done with simple if-else conditions and an array
"""
import random
import time

choices = ["rock","paper","scissor"]
"""
Rock -> Scissors
Scissors -> Paper
Paper -> Rock
"""
class UnknownChoiceError(Exception): pass #handles bad inputs

def player_vs_player():
    while True:
        print("Choose Rock, Paper, or Scissor")
        p1, p2 = None, None

        while True:
            try:
                p1 = input("Player 1, Type your weapon: ").lower()
                p2 = input("Player 2, Type your weapon: ").lower()

                if p1 not in choices or p2 not in choices:
                    raise UnknownChoiceError

                break

            except UnknownChoiceError:
                print("Please pick Rock Paper, or Scissor only")


        if p1.lower() == p2.lower():
            print("Same choice picked")
            print("Game is a draw")
        elif p1 == "rock":
            if p2 == "paper":
                print("Paper wraps the Rock...")
                print("Player 2 wins!")
            elif p2 == "scissor":
                print("Rock breaks Scissor")
                print("Player 1 wins!")
        elif p1 == "paper":
            if p2 == "rock":
                print("Paper wraps the Rock...")
                print("Player 1 wins!")
            elif p2 == "scissor":
                print("...Scissor cuts Paper")
                print("Player 2 wins!")
        elif p1 == "scissor":
            if p2 == "rock":
                print("Rock breaks Scissor")
                print("Player 2 wins!")
            elif p2 == "paper":
                print("...Scissor cuts Paper")
                print("Player 2 wins!")
        
        play_again = input("Play again? (yes/no): ").lower()

        if play_again != "yes":
            "Till next time!"
            break

def player_vs_computer():
    while True:
        computer = random.choice(choices)
        player = input("Rock, Paper, or Scissor?: ").lower()

        while player not in choices:
            print("Wrong input, try typing again")
            player = input("Rock, Paper, or Scissor?: ").lower()

        if player == computer:
            print("Player picked: ", player)
            time.sleep(1)
            print("Computer picked: ", computer)
            print("Same choice picked")
            print("Game is a draw")
        elif player == "rock":
            if computer == "paper":
                print("Player picked: ", player)
                time.sleep(1)
                print("Computer picked: ", computer)    
                print("Paper wraps the Rock...")
                print("Player 2 wins!")
            elif computer == "scissor":
                print("Player picked: ", player)
                time.sleep(1)
                print("Computer picked: ", computer)
                print("Rock breaks Scissor")
                print("Player 1 wins!")
        elif player == "paper":
            if computer == "rock":
                print("Player picked: ", player)
                time.sleep(1)
                print("Computer picked: ", computer)
                print("Paper wraps the Rock...")
                print("Player 1 wins!")
            elif computer == "scissor":
                print("Player picked: ", player)
                time.sleep(1)
                print("Computer picked: ", computer)
                print("...Scissor cuts Paper")
                print("Player 2 wins!")
        elif player == "scissor":
            if computer == "rock":
                print("Player picked: ", player)
                time.sleep(1)
                print("Computer picked: ", computer)
                print("Rock breaks Scissor")
                print("Player 2 wins!")
            elif computer == "paper":
                print("Player picked: ", player)
                time.sleep(1)
                print("Computer picked: ", computer)
                print("...Scissor cuts Paper")
                print("Player 2 wins!")
        
        play_again = input("Play again? (yes/no): ").lower()

        if play_again != "yes":
            "Till next time!"
            break