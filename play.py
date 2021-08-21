from hashlib import new
import pygame, random, sys

from cell import Cell
from astar import astar

# Basic Pygame configs
pygame.init()
pygame.display.set_caption('A* Pathfinder')

# Define game parameters
width, height = 500,500
rows, cols = 50,50
cell_w = width / cols
cell_h = height / rows

# Create screen and lock framerate
screen = pygame.display.set_mode((width, height))
fps = 25
fpsClock = pygame.time.Clock()

def new_grid():
    grid = [[Cell(i, j, cols, rows, cell_w, cell_h) for j in range(cols)] for i in range(rows)]
    return grid

def show_cells(grid) -> None:
    '''Updates the grid. i.e Coloring cells.'''
    for row in grid:
        for cell in row:
            cell.show(screen)

    pygame.display.flip()
    fpsClock.tick(fps)

def check_kill(event):
    '''Checks to see if pygame window was closed.'''
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def game_loop():
    grid = new_grid()
    start = grid[0][0]
    end = grid[cols-1][rows-1]
    start.is_wall = 0
    end.is_wall = 0
    
    show_cells(grid)
    
    while True:
        for event in pygame.event.get():
            check_kill(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    try:
                        astar(grid, start, end)
                    except Exception as e:
                        raise
                if event.key == pygame.K_r:
                    grid = new_grid()
                    start = grid[int(random.random()*(cols-1))][int(random.random()*(rows-1))]
                    end = grid[int(random.random()*(cols-1))][int(random.random()*(rows-1))]
                    start.is_wall = 0
                    end.is_wall = 0
                    show_cells(grid)

if __name__ == "__main__":
    game_loop()
