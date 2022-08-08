# make note of these imports.
import numpy
import pygame
import math
import sys

"""
declare global variables for:
board color (blue - 0, 0, 255),
empty spot color (black - 0, 0, 0),
player 1 chip color (red - 255, 0, 0),
player 2 chip color (yellow - 255, 255, 0),
number of rows (6), and
number of columns (7).

You may use any colors you wish, but
the common colors are listed with their
rgb values. You may also change the size
of the board to experiment.
"""
# REPLACE NONE VALUES BELOW WITH THE CORRECT DATA TYPE
BOARD_COLOR = None # (red, green, blue)
SPOT_COLOR = None
P1_COLOR = None 
P2_COLOR = None

COLUMNS = None # int
ROWS = None

def make_board():
    '''
    Use numpy to create an empty array whose shape
    corresponds to the number of rows and columns.

    Returns
    -------
    board = ndarray

    Implements (See also)
    ---------------------
    numpy.zeros(shape)
    '''
    # ----------------
    # INSERT CODE HERE
    # ----------------

def loc_works(board, column):
    '''
    Returns True or False based on a check to see if 
    the selected column on the board is full, or if 
    it is playable.

    Parameters
    ----------
    board : ndarray
    column : int

    Returns
    -------
    True or False : bool

    Implements (See also)
    ---------------------
    ROWS
    '''
    # ----------------
    # INSERT CODE HERE
    # ----------------

def next_row(board, column):
    '''
    Selects the next available row within the column

    Parameters
    ----------
    board = ndarray
    column = int

    Returns
    -------
    row = int
    '''
    # ----------------
    # INSERT CODE HERE
    # ----------------

def print_board(board):
    '''
    Print a vertically flipped version of the board to the console.

    Parameters
    ----------
    board = ndarray

    Implements (See also)
    ---------------------
    numpy.flip(array, axis)
    '''
    # ----------------
    # INSERT CODE HERE
    # ----------------

def win_check(board, chip):
    '''
    Checks for combos of 4 along vertical, horizontal, and 
    negatively and positively sloped diagonal lines.

    Parameters
    ----------
    board = ndarray
    chip = int

    Returns
    -------
    True : bool
    '''
    # this code block checks for combos of 4 along horizontal lines
    for column in range(COLUMNS - 3):
        for row in range(ROWS):
            if board[row][column] == chip \
            and board[row][column + 1] == chip \
            and board[row][column + 2] == chip \
            and board[row][column + 3] == chip:
                return True

    for column in range(COLUMNS):
        for row in range(ROWS - 3):
            # ----------------
            # INSERT CODE HERE
            # ----------------

    for column in range(COLUMNS - 3):
        for row in range(ROWS - 3):
            # ----------------
            # INSERT CODE HERE
            # ----------------

    for column in range(COLUMNS - 3):
        for row in range(3, ROWS):
            # ----------------
            # INSERT CODE HERE
            # ----------------

def play_c4():
    '''
    Initializes and maintains the primary game loop. 
    Renders the board in a new window via pygame,
    tracks events such as exit, mouse movement, and 
    mouse clicks.

    Implements (See also)
    ---------------------
    global variables --
        COLUMNS : int
        ROWS : int
        BOARD_COLOR : tuple of 3 ints
        SPOT_COLOR : tuple of 3 ints
        P1_COLOR : tuple of 3 ints
        P2_COLOR : tuple of 3 ints

    self-made functions --
        make_board()
        print_board(board)
        loc_works(board, column)
        next_row(board, column)
        place_chip(board, row, column, chip)
        win_check(board, chip)

    internal functions --
        draw_board(board)

    module functions --
        math.floor(int)
        sys.exit()
        pygame
            .init()
            .display
                .set_mode(size)
                .update()
                .blit(source, destination)
            .draw
                .rect(surface, color, rect)
                .circle(surface, color, center, radius)
            .font
                .Sysfont(name, size)
                .render
            .event.get()
            .QUIT
            .MOUSEMOTION
            .MOUSECLICK
            .time.wait(milliseconds)
            .quit()
    '''
    # First, we'll define some internal functions.
    def draw_board(board):
        '''
        Use pygame to draw the current state of the 
        board in a new window.


        Parameters
        ----------
        board : ndarray

        Implements (See also)
        ---------------------
        COLUMNS : int
        ROWS : int
        BOARD_COLOR : rgb
        SPOT_COLOR : rgb
        P1_COLOR : rgb
        P2_COLOR : rgb

        pygame
            .draw
                .rect(surface, color, rect)
                .circle(surface, color, center, radius)
            .display.update()
        
        '''
        # draws a rectangle and circle for each spot in the grid of the board.
        for column in range(COLUMNS):
            for row in range(ROWS):
                pygame.draw.rect(   
                    screen, 
                    BOARD_COLOR, 
                    (
                        column * screen_size, 
                        row * screen_size + screen_size,
                        screen_size, 
                        screen_size
                    )
                )
                pygame.draw.circle( 
                    screen, 
                    SPOT_COLOR, 
                    (
                        int(column * screen_size + screen_size / 2), 
                        int(row * screen_size + screen_size + screen_size / 2)
                    ), 
                    circle_radius
                )

        # populates the board with pieces of the right color
        for column in range(COLUMNS):
            for row in range(ROWS):      
                if board[row][column] == 1:
                    pygame.draw.circle( 
                        screen,
                        P1_COLOR,
                        (
                            int(column * screen_size + screen_size / 2),
                            screen_height - int(row * screen_size + screen_size / 2)
                        ), 
                        circle_radius
                    )
                elif board[row][column] == 2: 
                    pygame.draw.circle( 
                        screen, 
                        P2_COLOR, 
                        (
                            int(column * screen_size + screen_size / 2), 
                            screen_height - int(row * screen_size + screen_size / 2)
                        ), 
                        circle_radius
                    )

        # updates the display
        pygame.display.update()

    def place_chip(board, row, column, chip):
        '''
        Assigns the current player's chip to the selected spot
        on the board.

        Parameters
        ----------
        board = ndarray
        row = int
        column = int
        chip = int
        '''
        # ----------------
        # INSERT CODE HERE
        # ----------------

    # Now we'll make the board and print it in the console.
    c4_board = ????? # MAKE THE BOARD AND ASSIGN IT
    ????? # PRINT THE BOARD

    # We'll define some local, mutable variables.
    game_over = False
    turn = 0

    # Initialize all pygame imports.
    pygame.init()

    # Next, we define the size of the screen and initialize that as well.
    screen_size = 100

    circle_radius = int(screen_size/2 - 5) # for making our board spots.
    screen_width = COLUMNS * screen_size
    screen_height = ROWS * screen_size
    size = (screen_width, screen_height)
    screen = pygame.display.set_mode(size)

    # With that done, we can render the board in a new window.
    ????? # DRAW THE UPDATED BOARD

    # Set the font we'll use for the victory/tie message.
    game_font = pygame.font.SysFont("monospace", 75)

    # and here's the primary loop! This is where we listen for events
    # and initiate updates based on those events.
    while not game_over:

        for event in pygame.event.get():

            # Ff the player quits the window, we'll exit the program.
            if event.type == pygame.QUIT:
                sys.exit()

            # If the mouse moves, we'll update the position of the chip
            # above the board.
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(   
                    screen, 
                    SPOT_COLOR, 
                    (
                        0, 
                        0 , 
                        screen_width, 
                        screen_size
                    )
                )
                x = event.pos[0]
                
                if turn == 0:
                    pygame.draw.circle(
                        screen, 
                        P1_COLOR, 
                        (
                            x, 
                            int(screen_size / 2)
                        ), 
                        circle_radius
                    )
                else:
                    pygame.draw.circle(
                        screen, 
                        P2_COLOR, 
                        (
                            x, 
                            int(screen_size / 2)
                        ), 
                        circle_radius
                    )

            pygame.display.update()

            # if the mouse is clicked, we'll check to make sure the
            # move is valid and drop a chip in that column. Then we'll
            # update and render the board switch players.
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(
                    screen, 
                    SPOT_COLOR, 
                    (
                        0, 
                        0, 
                        screen_width, 
                        screen_size
                    )
                )

                if turn == 0:
                    x = event.pos[0]
                    column = int(math.floor(x / screen_size))

                    if ?????: # CHECK FOR VALID LOCATION IN COLUMN
                        row = ????? # SELECT NEXT AVAILABLE ROW
                        ????? # PLACE P1 CHIP

                        if ?????: # CHECK FOR P1 VICTORY
                            label = game_font.render("P1 wins!", 1, P1_COLOR)
                            screen.blit(label, (40, 10))
                            game_over = True

                else:
                    x = event.pos[0]
                    column = int(math.floor(x/screen_size))

                    if ?????: # CHECK FOR VALID LOCATION IN COLUMN
                        row = ????? # SELECT NEXT AVAILABLE ROW
                        ????? # PLACE P2 CHIP

                        if ?????: # CHECK FOR P2 VICTORY
                            label = game_font.render("P2 wins!", 2, P2_COLOR)
                            screen.blit(label, (40, 10))
                            game_over = True

                # PRINT THE UPDATED BOARD
                # DRAW THE UPDATED BOARD

                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(3000)
                    pygame.quit()