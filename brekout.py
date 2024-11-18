import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakout O‘yini")

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)

paddle_width = 100
paddle_height = 20
paddle_speed = 10
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - paddle_height - 10, paddle_width,
                     paddle_height)

ball_radius = 10
ball_speed_x = 5
ball_speed_y = -5
ball = pygame.Rect(screen_width // 2, screen_height // 2, ball_radius * 2, ball_radius * 2)

block_width = 80
block_height = 30
block_rows = 5
block_cols = 10
blocks = []

for row in range(block_rows):
    for col in range(block_cols):
        blocks.append(
            pygame.Rect(col * (block_width + 10) + 30, row * (block_height + 10) + 30, block_width, block_height))

score = 0
font = pygame.font.SysFont(None, 35)
game_over = False


running = True
clock = pygame.time.Clock()


def draw_objects():
    screen.fill(black)

    pygame.draw.rect(screen, blue, paddle)

    pygame.draw.ellipse(screen, white, ball)

    # Blocks
    for block in blocks:
        pygame.draw.rect(screen, red, block)

    # Ballarni ko‘rsatish
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

    # O'yin tugagan bo'lsa, "O'yin tugadi" yozuvi
    if game_over:
        game_over_text = font.render("O'yin tugadi! Qayta boshlash uchun 'R' ni bosing", True, white)
        screen.blit(game_over_text, (screen_width // 2 - 200, screen_height // 2 - 20))

    pygame.display.update()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle.right < screen_width:
            paddle.x += paddle_speed

        # Ball harakatini yangilash
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Ball chegaradan chiqish
        if ball.left <= 0 or ball.right >= screen_width:
            ball_speed_x = -ball_speed_x
        if ball.top <= 0:
            ball_speed_y = -ball_speed_y

        if ball.bottom >= screen_height:
            game_over = True

        if paddle.colliderect(ball):
            ball_speed_y = -ball_speed_y

        for block in blocks[:]:
            if block.colliderect(ball):
                blocks.remove(block)
                ball_speed_y = -ball_speed_y
                score += 10

    draw_objects()
    clock.tick(60)

    # O‘yinni qayta boshlash
    if game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # O‘yinni qayta boshlash uchun o‘zgaruvchilarni qayta sozlash
            paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - paddle_height - 10,
                                 paddle_width, paddle_height)
            ball = pygame.Rect(screen_width // 2, screen_height // 2, ball_radius * 2, ball_radius * 2)
            blocks = [
                pygame.Rect(col * (block_width + 10) + 30, row * (block_height + 10) + 30, block_width, block_height)
                for row in range(block_rows) for col in range(block_cols)]
            score = 0
            ball_speed_x = 5
            ball_speed_y = -5
            game_over = False

pygame.quit()
