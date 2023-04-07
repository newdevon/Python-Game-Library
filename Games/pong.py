import pygame
# pygame.init() # should init for every pygame import

WIDTH, HEIGHT = 700, 500
# WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Our game window
# pygame.display.set_caption("Pong") # Window Title

FPS = 60

#COLORS Defined
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (116,167,239)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 7

WINNING_SCORE = 10
# SCORE_FONT = pygame.font.SysFont("couriernew", 50)

class Paddle:
    COLOR = WHITE
    VELOCITY = 4 # Speed at which paddle moves

    # constructor for 2 paddle objects
    def __init__(self, x, y, width, height): 
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    def draw(self, win): # draws the paddle
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up = True): # moves the paddle up or down
        if up:
            self.y -= self.VELOCITY
        else:
            self.y += self.VELOCITY

    def reset(self): # reset position after win
        self.x = self.original_x
        self.y = self.original_y

class Ball:
    MAX_VEL = 6
    COLOR = BLUE

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL # reverses when we go in other direction
        self.y_vel = 0 # this is changing constantly

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self): # ball movement
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self): # reset position after score
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1


def draw(win, paddles, ball, left_score, right_score): # drawing the game's sprites and level in current tick
    win.fill(BLACK)
    
    # draw left and right scores
    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    win.blit(left_score_text, (WIDTH * (1/4)  - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, (WIDTH * (3/4) - right_score_text.get_width()//2, 20))

    # draw left and right paddles
    for paddle in paddles:
        paddle.draw(win)

    # draw white dotted line down the middle
    for i in range(10, HEIGHT, HEIGHT//20): # `HEIGHT//20` means +25 to `i` every iteration
        if i % 2 == 1: # odd
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))

    # draw ball position
    ball.draw(win)

    # pygame.draw works with top-down overlap, whatever is drawn later will show on top
    pygame.display.update() # need to re-update the display after any draw


def handle_collision(ball, left_paddle, right_paddle):
    # Check floor and ceiling constraints
    if ball.y + ball.radius >= HEIGHT: # floor
        ball.y_vel *= -1 # reverse ball in Y direction 
    elif ball.y - ball.radius <= 0 : # ceiling
        ball.y_vel *= -1

    # Check left and right paddle contact
    if ball.x_vel < 0: # moving leftwards and left paddle
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height: # within Y range
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width: # X at right paddle edge
                ball.x_vel *= -1

                middle_y = left_paddle.y + left_paddle.height/2
                difference_in_y = middle_y - ball.y # negative means below middle y and positive above
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel

    else: # moving leftwards and right paddle
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height: # within Y range
            if ball.x + ball.radius >= right_paddle.x: # X at left paddle edge
                ball.x_vel *= -1

                middle_y = right_paddle.y + right_paddle.height/2
                difference_in_y = middle_y - ball.y # negative means below middle y and positive above
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel


def handle_keyboard_presses(keys, left_paddle, right_paddle):
    # ALSO handle if paddles will move off-screen
    left_paddle_up_allowed = left_paddle.y - left_paddle.VELOCITY >= 0
    left_paddle_down_allowed = left_paddle.y + left_paddle.height + left_paddle.VELOCITY <= HEIGHT
    right_paddle_up_allowed = right_paddle.y - right_paddle.VELOCITY >= 0
    right_paddle_down_allowed = right_paddle.y + right_paddle.height + right_paddle.VELOCITY <= HEIGHT

    
    if keys[pygame.K_w] and left_paddle_up_allowed: # if `W` key is pressed
        left_paddle.move(up=True)
    
    if keys[pygame.K_s] and left_paddle_down_allowed: # if `S` key is pressed 
        left_paddle.move(up=False)

    # if `W` key is pressed
    if keys[pygame.K_UP] and right_paddle_up_allowed: 
        right_paddle.move(up=True)
    # if `S` key is pressed
    if keys[pygame.K_DOWN] and right_paddle_down_allowed: 
        right_paddle.move(up=False)

def handle_post_win(win, win_text, ball, left_paddle, right_paddle, left_score, right_score):
    win.fill(BLACK)
    
    # draw left and right scores
    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    win.blit(left_score_text, (WIDTH * (1/4)  - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, (WIDTH * (3/4) - right_score_text.get_width()//2, 20))

    # draw left and right paddles
    left_paddle.draw(win)
    right_paddle.draw(win)

    # draw white dotted line down the middle
    for i in range(10, HEIGHT, HEIGHT//20): # `HEIGHT//20` means +25 to `i` every iteration
        if i % 2 == 1: # odd
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))

    text = SCORE_FONT.render(win_text, 1, WHITE)
    win.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)
    ball.reset()
    left_paddle.reset()
    right_paddle.reset()


def play_pong():
    pygame.init() # should init for every pygame import
    WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Our game window
    pygame.display.set_caption("Pong") # Window Title
    global SCORE_FONT
    SCORE_FONT = pygame.font.SysFont("couriernew", 50)

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)

    left_score, right_score = 0, 0
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) # keeps uniform speed of game between all PCs
        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # game exit condition
                run = False
                break

        # Check User Keypresses
        keys = pygame.key.get_pressed() # contain a list of all keys pressed
        handle_keyboard_presses(keys, left_paddle, right_paddle)

        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

        # Left and Right Scoring
        if ball.x < 0:
            right_score += 1
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()

        won = False
        if left_score >= WINNING_SCORE:
            won = True
            win_text = "Left Player Won!"

        elif right_score >= WINNING_SCORE:
            won = True
            win_text = "Right Player Won!"

        if won:
            handle_post_win(WIN, win_text, ball, left_paddle, right_paddle, left_score, right_score)
            left_score, right_score = 0, 0
            
    pygame.quit()

