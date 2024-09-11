import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15
PADDLE_SPEED = 25
BALL_SPEED = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Paddles
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move_up(self):
        self.rect.y -= PADDLE_SPEED
        if self.rect.top < 0:
            self.rect.top = 0

    def move_down(self):
        self.rect.y += PADDLE_SPEED
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

# Ball
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
        self.dx = BALL_SPEED
        self.dy = BALL_SPEED

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Ball collision with top or bottom
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy = -self.dy

    def check_collision(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.dx = -self.dx

    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.dx = BALL_SPEED
        self.dy = BALL_SPEED

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

# Create paddles and ball
player1 = Paddle(20, HEIGHT // 2 - PADDLE_HEIGHT // 2)
player2 = Paddle(WIDTH - 30, HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1.move_up()
            elif event.key == pygame.K_s:
                player1.move_down()
            elif event.key == pygame.K_UP:
                player2.move_up()
            elif event.key == pygame.K_DOWN:
                player2.move_down()

    ball.move()
    ball.check_collision(player1)
    ball.check_collision(player2)

    if ball.rect.left <= 0 or ball.rect.right >= WIDTH:
        ball.reset()

    screen.fill(BLACK)
    player1.draw()
    player2.draw()
    ball.draw()

    pygame.display.flip()
    clock.tick(60)
