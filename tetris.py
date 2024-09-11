import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 500
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)

# Tetromino shapes
tetrominoes = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1], [1, 1]],  # O
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]  # Z
]

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tetris')

# Game grid
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]


# Tetromino class
class Tetromino:
    def __init__(self):
        self.x = GRID_WIDTH // 2 - 1
        self.y = 0
        self.shape = random.choice(tetrominoes)
        self.color = random.choice([CYAN, BLUE, ORANGE, YELLOW, GREEN, PURPLE, RED])

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

    def draw(self):
        for y, row in enumerate(self.shape):
            for x, col in enumerate(row):
                if col:
                    pygame.draw.rect(screen, self.color,
                                     (self.x * GRID_SIZE + x * GRID_SIZE,
                                      self.y * GRID_SIZE + y * GRID_SIZE,
                                      GRID_SIZE, GRID_SIZE))

    def can_move(self):
        for y, row in enumerate(self.shape):
            for x, col in enumerate(row):
                if col:
                    if (self.y + y >= GRID_HEIGHT or self.x + x < 0 or
                            self.x + x >= GRID_WIDTH or
                            grid[self.y + y][self.x + x]):
                        return False
        return True

    def place(self):
        for y, row in enumerate(self.shape):
            for x, col in enumerate(row):
                if col:
                    # Game grid
                    grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]


# Functions
def draw_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x]:
                pygame.draw.rect(screen, WHITE,
                                 (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)


def check_rows():
    global grid
    full_rows = [row for row in range(GRID_HEIGHT) if all(grid[row])]
    if full_rows:
        grid = [[0] * GRID_WIDTH] * len(full_rows) + [row[:] for row in grid if not all(row)]


# Initialize game objects
current_piece = Tetromino()
next_piece = Tetromino()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_piece.move_left()
                if not current_piece.can_move():
                    current_piece.move_right()
            elif event.key == pygame.K_RIGHT:
                current_piece.move_right()
                if not current_piece.can_move():
                    current_piece.move_left()
            elif event.key == pygame.K_DOWN:
                current_piece.move_down()
                if not current_piece.can_move():
                    current_piece.place()
                    current_piece = next_piece
                    next_piece = Tetromino()
            elif event.key == pygame.K_UP:
                current_piece.rotate()
                if not current_piece.can_move():
                    current_piece.rotate()

    screen.fill(BLACK)

    # Draw current piece
    current_piece.draw()

    # Draw grid and check for completed rows
    draw_grid()
    check_rows()

    pygame.display.flip()
    clock.tick(FPS)
