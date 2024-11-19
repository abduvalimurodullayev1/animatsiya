import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Futbol O‘yini")

green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

player_size = 50
player_speed = 5
player1 = pygame.Rect(100, screen_height // 2 - player_size // 2, player_size, player_size)
player2 = pygame.Rect(screen_width - 150, screen_height // 2 - player_size // 2, player_size, player_size)

ball_size = 20
ball_speed_x = 4
ball_speed_y = 4
ball = pygame.Rect(screen_width // 2 - ball_size // 2, screen_height // 2 - ball_size // 2, ball_size, ball_size)

goal_width = 20
goal_height = 100
goal1 = pygame.Rect(0, screen_height // 2 - goal_height // 2, goal_width, goal_height)
goal2 = pygame.Rect(screen_width - goal_width, screen_height // 2 - goal_height // 2, goal_width, goal_height)

score1 = 0
score2 = 0
font = pygame.font.SysFont(None, 35)

running = True  
clock = pygame.time.Clock()


def draw_objects():
    screen.fill(green)

    # Futbolchilar
    pygame.draw.rect(screen, white, player1)
    pygame.draw.rect(screen, white, player2)

    # To'p
    pygame.draw.ellipse(screen, black, ball)

    # Gol darvozalari
    pygame.draw.rect(screen, red, goal1)
    pygame.draw.rect(screen, red, goal2)

    # Gol Hisobi
    score_text = font.render(f"Score: {score1} - {score2}", True, white)
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 10))

    pygame.display.update()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= player_speed
    if keys[pygame.K_s] and player1.bottom < screen_height:
        player1.y += player_speed

    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= player_speed
    if keys[pygame.K_DOWN] and player2.bottom < screen_height:
        player2.y += player_speed

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y = -ball_speed_y
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x = -ball_speed_x
    if ball.left <= goal_width:
        score2 += 1
        ball.x = screen_width // 2
        ball.y = screen_height // 2
        ball_speed_x = -ball_speed_x
    if ball.right >= screen_width - goal_width:
        score1 += 1
        ball.x = screen_width // 2
        ball.y = screen_height // 2
        ball_speed_x = -ball_speed_x

    draw_objects()
    clock.tick(60)
