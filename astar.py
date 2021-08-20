import sys

import pygame, random
from pygame.locals import *
 
pygame.init()
pygame.display.set_caption('A* Pathfinder')

width, height = 500, 500
rows, cols = 25,25
cell_w = width / cols
cell_h = height / rows

screen = pygame.display.set_mode((width, height))
fps = 15
fpsClock = pygame.time.Clock()


class Cell():
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.f = 0
        self.g = 0
        self.h = 0
        self.is_wall = 0
        self.parent = None
        self.neighbors = []

        # Randomize wall generation
        if random.random() <= .25:
            self.is_wall = 1

    def show(self, color):
        if self.is_wall:
            color = (0,0,0)
        rect = pygame.Rect(self.i*cell_w, self.j*cell_h, 
                           cell_w, cell_h)
        pygame.draw.rect(screen, color, rect, 0) # The filled rect
        pygame.draw.rect(screen, (0,0,0), rect, 1) # The border of the rect

    def find_neighbors(self, grid):
        '''
        Returns a list of all the neighboring cells
        '''
        #north, south, east, west neighbor locations
        nsew = ((self.i-1, self.j),(self.i+1, self.j),
                (self.i, self.j+1),(self.i, self.j-1))
        
        # north-east, south-east, north-west, south-west neighbor locations
        neseswnw = ((self.i-1, self.j+1),(self.i+1, self.j+1),
                    (self.i-1, self.j-1),(self.i+1, self.j-1))
        
        all_directions = nsew + neseswnw
        
        for i_prime, j_prime in all_directions:
            # Bounds check
            if i_prime < 0 or i_prime > rows-1 \
                or j_prime < 0 or j_prime > cols-1:
                continue
            else:
                self.neighbors.append(grid[i_prime][j_prime])
        
def calculate_manhanttan_heuristics(current_cell, end_cell):
	return abs(current_cell.i - end_cell.i) + abs(current_cell.j - end_cell.j)

grid = [[Cell(i, j) for j in range(cols)] for i in range(rows)]
for row in grid:
    for cell in row:
        cell.find_neighbors(grid)

start = grid[0][0]
end = grid[rows-1][cols-1]

open_cells = [start]
closed_cells = []

path = []

# Game loop
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                while True:
                    # A-Star
                    if (open_cells != []):
                        lowest_f_index = 0
                        for i in range(len(open_cells)):
                            if open_cells[i].f < open_cells[lowest_f_index].f:
                                lowest_f_index = i
                        
                        current = open_cells[lowest_f_index]
                        # print("Current cell: ", current.i, current.j)

                        if open_cells[lowest_f_index] == end:
                            # Find path
                            path_route = [(cell.i,cell.j) for cell in path]
                            print("FOUND!")
                            print("Nodes visited: ", len(path_route))
                            print("Path: ", path_route)
                            break

                        open_cells.remove(current)
                        closed_cells.append(current)
                        # print("Open cells: ", open_cells)
                        # print("Closed cells: ", closed_cells)

                        for neighbor in current.neighbors:
                            # print("Neighbor: ", neighbor.i, neighbor.j)
                            if neighbor not in closed_cells and not neighbor.is_wall:
                                tempG = current.g + 1
                                if neighbor in open_cells:
                                    if tempG < neighbor.g:
                                        neighbor.g = tempG
                                else:
                                    neighbor.g = tempG
                                    open_cells.append(neighbor)
                                
                                neighbor.h = calculate_manhanttan_heuristics(neighbor, end)
                                neighbor.f = neighbor.g + neighbor.h
                                neighbor.parent = current
                                # print(neighbor.f)
                    else:
                        print("NO PATH")

                    # Draw & Update
                    for row in grid:
                        for cell in row:
                            cell.show((255,255,255))

                    for cell in open_cells:
                        cell.show((0,255,0))

                    for cell in closed_cells:
                        cell.show((255,0,0))

                    path = []
                    temp = current
                    while (temp.parent):
                        path.append(temp.parent)
                        temp = temp.parent
                    path_route = [(cell.i,cell.j) for cell in path]

                    for cell in path:
                        cell.show((0,0,255))

                    pygame.display.flip()
                    fpsClock.tick(fps)