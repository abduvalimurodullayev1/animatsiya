import pygame
import sys
import random

pygame.init()

# Game constants
WIDTH, HEIGHT = 800, 800
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Python Snake Xenzia')


# Snake class
class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.grow = False

    def update(self):
        head_x, head_y = self.positions[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)

        if new_head in self.positions[1:] or new_head == (-1, -1):
            pygame.quit()
            sys.exit()

        self.positions.insert(0, new_head)

        if self.grow:
            self.grow = False
        else:
            self.positions.pop()

    def change_direction(self, direction):
        if direction == 'UP' and self.direction != (0, 1):
            self.direction = (0, -1)
        elif direction == 'DOWN' and self.direction != (0, -1):
            self.direction = (0, 1)
        elif direction == 'LEFT' and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif direction == 'RIGHT' and self.direction != (-1, 0):
            self.direction = (1, 0)

    def render(self):
        for x, y in self.positions:
            pygame.draw.rect(screen, GREEN, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))


# Food class
class Food:
    def __init__(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def update(self):
        pass

    def render(self):
        pygame.draw.rect(screen, RED,
                         (self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))


snake = Snake()
food = Food()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction('UP')
            elif event.key == pygame.K_DOWN:
                snake.change_direction('DOWN')
            elif event.key == pygame.K_LEFT:
                snake.change_direction('LEFT')
            elif event.key == pygame.K_RIGHT:
                snake.change_direction('RIGHT')

    snake.update()

    if snake.positions[0] == food.position:
        snake.grow = True
        food.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    screen.fill(BLACK)
    snake.render()
    food.render()
    pygame.display.flip()

    clock.tick(FPS)
