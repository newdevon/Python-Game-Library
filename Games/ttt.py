def render():
    '''
    Returns a string describing the board in its
    current state. It should look something like this:

     1 | 2 | 3
     - + - + -
     4 | 5 | 6
     - + - + -
     7 | 8 | 9

    Returns
    -------
    board_state : str

    Implements (See also)
    ---------------------
    BOARD : dict
    '''
    print(f"{BOARD[1]} | {BOARD[2]} | {BOARD[3]}")
    print("- + - + -")
    print(f"{BOARD[4]} | {BOARD[5]} | {BOARD[6]}")
    print("- + - + -")
    print(f"{BOARD[7]} | {BOARD[8]} | {BOARD[9]}")

def get_action(player):
    '''
    Prompts the current player for a number between 1 and 9.
    Checks* the returning input to ensure that it is an integer
    between 1 and 9 AND that the chosen board space is empty.

    Parameters
    ----------
    player : str

    Returns
    -------
    action : int

    Raises
    ======
    ValueError, TypeError

    Implements (See also)
    ---------------------
    BOARD : dict

    *Note: Implementing a while loop in this function is recommended,
    but make sure you aren't coding any infinite loops.
    '''
    print(f"\n{player}'s turn to move")

    while True:
        try:        
            move = int(input("Where would you like to move? (1-9): "))
            if 0 < move < 10 and BOARD[move] == ' ':
                return move
            else:
                raise ValueError
        except ValueError:
            print("Please make a number choice between 1-9 on available spaces")
            render()
            print(f"\n{player}'s turn to move")
        except TypeError:
            print("Enter digits between 1-9 only")

def victory_message(player):
    '''
    Prints the updated board and returns a victory message for the
    winning player.

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    victory_message : str

    Implements (See also)
    ---------------------
    print_t3() : func
    '''
    render()
    print(f"{player}'s wins!")

def check_win(player):
    '''
    Checks victory conditions. If found, calls victory_message().
    This can be done with one long chain of if/elif statements, but
    it can also be condensed into a single if/else statement, among
    other strategies (pattern matching if you have python 3.10 or above).

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    True or False : bool

    Implements (See also)
    ---------------------
    BOARD : dict
    victory_message(player) : func
    '''
    won = False
    if BOARD[1] == player and BOARD[2] == player and BOARD[3] == player:
        won = True
    elif BOARD[4] == player and BOARD[5] == player and BOARD[6] == player:
        won = True
    elif BOARD[7] == player and BOARD[8] == player and BOARD[9] == player:
        won = True
    elif BOARD[1] == player and BOARD[5] == player and BOARD[9] == player:
        won = True
    elif BOARD[3] == player and BOARD[5] == player and BOARD[7] == player:
        won = True
    elif BOARD[1] == player and BOARD[4] == player and BOARD[7] == player:
        won = True
    elif BOARD[2] == player and BOARD[5] == player and BOARD[8] == player:
        won = True
    elif BOARD[3] == player and BOARD[6] == player and BOARD[9] == player:
        won = True

    if won:
        victory_message(player)
        return won
    else:
        return won

def play_t3():
    '''
    This is the main game loop that is called from the launcher (main.py)

    Implements (See also)
    ---------------------
    BOARD : dict
    render() : func
    get_action(player) : func
    check_win(player) : func
    play_t3()* : func

    *Note: this function refers to itself. Be careful about
    inescapable infinite loops.
    '''
    global BOARD
    BOARD = {1: ' ',  2: ' ',  3: ' ',

        4: ' ',  5: ' ',  6: ' ',

        7: ' ',  8: ' ',  9: ' '}


    while True:
        print("Welcome to Tic Tac Toe!\n")

        player = 'X'
        game_round = 0
        game_over = False

        while not game_over:

            # Print the current state of the board
            render()

            # Get the current player's action and assign it to a variable called 'action'.
            action = get_action(player)

            # Assign the current player ('X' or 'O') as a value to BOARD. Use the 'action' variable as the key.
            BOARD[action] = player

            # Increment the game round by 1.
            game_round += 1

            # Check if the game is winnable (game_round >= 4),
            if game_round >= 4:
                # then check for win conditions (check_win(player)),
                if check_win(player) == True:
                    # and if there's a win, end the game (game_over = True),
                    game_over = True
                    # and break the loop (break).
                    break

            # Check if there are any open spots left (game_round == 9),
            if game_round >= 9:
                # and if there aren't, print a tie message,
                print("DRAW! No more spaces left!")
                # end the game,
                # and break the while loop.
                break

            # switch players with a quick conditional loop.
            if player == 'X':
                player = 'O'
            else:
                player = 'X'

        # prompt for a restart and assign the input to a 'restart' variable.
        play_again = input("Try again (yes/no)? ")
        if play_again != "yes":
            break

        # if yes, clear each key in the board with a for loop
        for key in BOARD:
            if BOARD[key] != ' ':
                BOARD[key] = ' '
        
        # and reinitiate the game loop (play_t3()).