from rps import player_vs_computer, player_vs_player
from ng import number_guesser
from rt import reaction_time
from ttt import play_t3
import time

def app():
    print("Welcome to the Python Game Library C: \n", )

    print("We have Rock, Paper, Scissor and Number Guesser\n")
    print("Which game would you like to play? \n")
    
    while True:
        try:
            game = int(input("(1) Rock Paper Scissor 1v1\n(2) Rock Paper Scissor vs Ai\n(3) Number Guessor\n(4) Reaction Time\n(5) Tic Tac Toe\nYour choice? "))

            if game == 1: player_vs_player()
            elif game == 2: player_vs_computer()
            elif game == 3: number_guesser()
            elif game == 4: reaction_time()
            elif game == 5: play_t3()

        except ValueError:
            print("\nPlease enter a valid entry\n")

        play_again = input("exit library? (yes/no): ")
        if play_again == "yes":
            print("Shutting down...")
            time.sleep(1)
            break

app()