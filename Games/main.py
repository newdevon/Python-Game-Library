from rps import player_vs_computer, player_vs_player
from ng import number_guesser
from rt import reaction_time
from ttt import play_t3
from cf import play_c4
from pong import play_pong
import time

def main():
    print("Welcome to the Python Game Library C: \n", )

    print("We have Pong, Connect 4, Tic-Tac-Toe, Number Guesser, Reaction Time, and Rock-Paper-Scissors\n")
    print("Which game would you like to play? \n")
    
    while True:
        try:
            game = int(input("(1) Connect 4\n(2) Tic-Tac-Toe\n(3) Number Guesser\n(4) Reaction Time\n(5) Rock-Paper-Scissor 1v1\n(6) Rock-Paper-Scissor vs Ai\n(7) Pong\nYour choice? "))

            if game == 1: play_c4()
            elif game == 2: play_t3()
            elif game == 3: number_guesser()
            elif game == 4: reaction_time()
            elif game == 5: player_vs_player()
            elif game == 6: player_vs_computer()
            elif game == 7: play_pong()

        except ValueError:
            print("\nPlease enter a valid entry\n")

        play_again = input("exit library? (yes/no): ")
        if play_again == "yes":
            print("Shutting down...")
            time.sleep(1)
            break

#This condition checks if this python file runs directly as a script and not through an import as a module. `__name__ is relative to the main script file`
if __name__ == '__main__':
    main()