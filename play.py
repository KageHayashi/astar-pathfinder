import pygame, random, sys

from cell import Cell
from astar import astar

# Basic Pygame configs
pygame.init()
pygame.display.set_caption('A* Pathfinder')

# Define game parameters
width, height = 1000,1000
rows, cols = 100,100
cell_w = width / cols
cell_h = height / rows

# Create screen and lock framerate
screen = pygame.display.set_mode((width, height))
fps = 30
fpsClock = pygame.time.Clock()

# Create game grid and define start node and end node
grid = [[Cell(i, j, cols, rows, cell_w, cell_h) for j in range(cols)] for i in range(rows)]
start = grid[0][0]
end = grid[rows-1][cols-1]
start.is_wall = 0
end.is_wall = 0


def update_cells(grid, path, open_cells, closed_cells) -> None:
    '''Updates the grid. i.e Coloring cells.'''
    for row in grid:
        for cell in row:
            cell.show(screen, (255,255,255))

    for cell in open_cells:
        cell.show(screen, (0,255,0))

    for cell in closed_cells:
        cell.show(screen, (255,0,0))

    for cell in path:
        cell.show(screen, (0,0,255))

    pygame.display.flip()
    fpsClock.tick(fps)
    
def check_kill(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def check_play(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            try:
                astar(grid, start, end)
            except Exception as e:
                raise

def game_loop():
    # Start game loop
    while True:
        for event in pygame.event.get():
            check_kill(event)
            check_play(event)

if __name__ == "__main__":
    game_loop()
