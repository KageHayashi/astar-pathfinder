from dijkstra import dijkstra
from hashlib import new
import pygame, random, sys

from cell import Cell
from astar import astar

# Basic Pygame configs
pygame.init()
pygame.display.set_caption('A* Pathfinder')

# Define game parameters
width, height = 500,500
rows, cols = 25,25
cell_w = width / cols
cell_h = height / rows

# Create screen and lock framerate
screen = pygame.display.set_mode((width, height))
fps = 30
fpsClock = pygame.time.Clock()

def new_grid():
    grid = [[Cell(i, j, cols, rows, cell_w, cell_h) for j in range(cols)] for i in range(rows)]
    return grid

def create_maze(grid):
    '''
    Creates a maze using the given grid.
    Uses an iterative randomized depth-first search.
    '''
    
    # Set every cell to wall first
    for row in grid:
        for cell in row:
            cell.is_wall = 1

    open_stack = []
    visited = []

    # Choose a random cell as the initial cell
    open_stack.append(grid[int(random.random()*(cols-1))][int(random.random()*(rows-1))])

    counter = 0
    while (open_stack != []):
        counter += 1
        current = open_stack.pop()
        current.is_wall = 0
        # print("current:", current.i, current.j)

        randomized_neighbors = current.find_maze_neighbors(grid)
        random.shuffle(randomized_neighbors)

        for neighbor in randomized_neighbors:
            if neighbor not in visited:
                # print("neighbor:", neighbor.i, neighbor.j)
                delta_i, delta_j = abs(current.i - neighbor.i), abs(current.j - neighbor.j)
                
                # Adjust delta location
                if delta_i == 0 and delta_j > 0:
                    delta_j -= 1
                if delta_i == 0 and delta_j < 0:
                    delta_j += 1
                if delta_i > 0 and delta_j == 0:
                    delta_i -= 1
                if delta_i < 0 and delta_j == 0:
                    delta_i += 1
                if delta_i > 0 and delta_j > 0:
                    delta_j -= 1
                    delta_i -= 1
                if delta_i < 0 and delta_j < 0:
                    delta_j += 1
                    delta_i += 1

                # print("delta:", delta_i, delta_j)
                open_stack.append(current)

                i, j = current.i + delta_i, current.j + delta_j
                if i >= 0 and i <= rows-1 and j >= 0 and j <= cols-1:
                # neighbor.is_wall = 0
                    grid[i][j].is_wall = 0
                visited.append(neighbor)
                open_stack.append(neighbor)
                break

def place_wall(pos_i, pos_j, grid, start, end):
    '''Places a wall on the grid at pos_i, pos_j'''
    cell = grid[pos_i][pos_j]
    
    if cell != start and cell != end:
        cell.is_wall = True
    show_cells(grid, 0)

def remove_wall(pos_i, pos_j, grid, start, end):
    '''Removes the wall on the grid at pos_i, pos_j'''
    cell = grid[pos_i][pos_j]
    
    if cell != start and cell != end:
        cell.is_wall = False
    show_cells(grid, 0)

def reset_cells_to_normal(grid):
    '''Resets all cells to normal'''
    for row in grid:
        for cell in row:
            cell.status = 'normal'

def show_cells(grid, speed) -> None:
    '''Updates the grid. i.e Coloring cells.'''
    for row in grid:
        for cell in row:
            cell.show(screen)

    pygame.display.update()
    fpsClock.tick(speed)

def check_kill(event):
    '''Checks to see if pygame window was closed.'''
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def game_loop():
    '''
    Main game loop. Creates a new grid, create a maze of walls,
    and start checking game events.
    '''
    grid = new_grid()
    create_maze(grid)
    start = grid[0][0]
    end = grid[cols-1][rows-1]
    start.is_wall = 0
    end.is_wall = 0
    
    show_cells(grid, fps)
    
    while True:
        for event in pygame.event.get():
            check_kill(event)
            
            # Check mouse events
            mouse_pressed = pygame.mouse.get_pressed()
            if mouse_pressed:
                pos = pygame.mouse.get_pos()
                mouse_i = pos[1] // (height // rows)
                mouse_j = pos[0] // (width // cols)

                # Left mouse button clicked
                if mouse_pressed[0]:
                    place_wall(mouse_i, mouse_j, grid, start, end)
                # Right mouse button clicked
                elif mouse_pressed[-1]:
                    remove_wall(mouse_i, mouse_j, grid, start, end)

            # Check keyboard events
            if event.type == pygame.KEYDOWN:
                # Starts the game with SPACEBAR
                if event.key == pygame.K_SPACE:
                    try:
                        reset_cells_to_normal(grid)
                        dijkstra(grid, start, end)
                    except Exception as e:
                        raise
                # Restart the game with R
                if event.key == pygame.K_r:
                    grid = new_grid()
                    #start = grid[int(random.random()*(cols-1))][int(random.random()*(rows-1))]
                    #end = grid[int(random.random()*(cols-1))][int(random.random()*(rows-1))]
                    start = grid[0][0]
                    end = grid[cols-1][rows-1]
                    start.is_wall = 0
                    end.is_wall = 0
                    show_cells(grid, fps)

if __name__ == "__main__":
    game_loop()
