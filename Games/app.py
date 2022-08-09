from rps import player_vs_computer, player_vs_player
from ng import number_guesser
from rt import reaction_time
from ttt import play_t3
from cf import play_c4
import time

def app():
    print("Welcome to the Python Game Library C: \n", )

    print("We have Connect 4, Tic-Tac-Toe, Number Guesser, Reaction Time, and Rock-Paper-Scissor\n")
    print("Which game would you like to play? \n")
    
    while True:
        try:
            game = int(input("(1) Connect 4\n(2) Tic-Tac-Toe\n(3) Number Guesser\n(4) Reaction Time\n(5) Rock-Paper-Scissor 1v1\n(6) Rock-Paper-Scissor vs Ai\nYour choice? "))

            if game == 1: play_c4()
            elif game == 2: play_t3()
            elif game == 3: number_guesser()
            elif game == 4: reaction_time()
            elif game == 5: player_vs_player()
            elif game == 6: player_vs_computer()

        except ValueError:
            print("\nPlease enter a valid entry\n")

        play_again = input("exit library? (yes/no): ")
        if play_again == "yes":
            print("Shutting down...")
            time.sleep(1)
            break

app()