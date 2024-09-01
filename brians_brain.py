import random
import pygame

pygame.init()

# Define colors for the different states
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)  # Firing state
RED = (255, 0, 0)  # Refractory state

WIDTH, HEIGHT = 600, 600
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def draw_grid(grid):
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if grid[row][col] == 1:  # Firing
                color = YELLOW
            elif grid[row][col] == 2:  # Refractory
                color = RED
            else:  # Off
                color = GREY
            top_left = (col * TILE_SIZE, row * TILE_SIZE)
            pygame.draw.rect(screen, color, (*top_left, TILE_SIZE, TILE_SIZE))

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))

    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))


def gen(num):
    grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for _ in range(num):
        x = random.randrange(0, GRID_WIDTH)
        y = random.randrange(0, GRID_HEIGHT)
        grid[y][x] = 1  # Start as Firing
    return grid


def adjust_grid(grid):
    new_grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    for y in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            state = grid[y][col]
            neighbors = get_neighbours((col, y), grid)
            firing_neighbors = neighbors.count(1)

            if state == 0 and firing_neighbors == 2:  # Off to Firing
                new_grid[y][col] = 1
            elif state == 1:  # Firing to Refractory
                new_grid[y][col] = 2
            elif state == 2:  # Refractory to Off
                new_grid[y][col] = 0
            else:  # No change
                new_grid[y][col] = state

    return new_grid


def get_neighbours(pos, grid):
    x, y = pos
    neighbours = []

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT:
                neighbours.append(grid[ny][nx])

    return neighbours


def brians_brain():
    running = True
    grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    playing = False
    count = 0
    update_freq = 30

    while running:
        clock.tick(FPS)

        if playing:
            count += 1

        if count >= update_freq:
            count = 0
            grid = adjust_grid(grid)

        pygame.display.set_caption("Playing" if playing else "Paused")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                grid[row][col] = (grid[row][col] + 1) % 3  # Cycle through states

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing

                if event.key == pygame.K_c:
                    grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
                    playing = False
                    count = 0

                if event.key == pygame.K_r:
                    grid = gen(random.randrange(2, 10) * GRID_WIDTH)

        screen.fill(BLACK)
        draw_grid(grid)
        pygame.display.update()
    pygame.quit()