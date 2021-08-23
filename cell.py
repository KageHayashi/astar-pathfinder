import pygame, random, math

from typing import List
from heuristics import calculate_manhanttan_heuristics

# Color configs for each different cell type
CELL_COLOR_STATUS = {'normal': (255,255,255),
                     'wall'  : (0,0,0),
                     'open'  : (0,255,0),
                     'close' : (255,0,0),
                     'path'  : (0,0,255)}

class Cell():
    def __init__(self, i, j, cols, rows, cell_w, cell_h):
        # Basic cell info
        self.i = i
        self.j = j
        self.is_wall = 0
        self.parent = None
        self.neighbors = []
        self.maze_neighbors = []
        self.status = 'normal'
        self.color = CELL_COLOR_STATUS[self.status]

        # Game info
        self.cols = cols
        self.rows = rows
        self.cell_w = cell_w
        self.cell_h = cell_h

        # Values for A*
        self.f = 0
        self.g = 0
        self.h = 0

        # Values for Dijkstra
        self.dist = math.inf

        # Randomize wall generation
        # if random.random() <= .4:
        #     self.is_wall = 1

    def show(self, screen):
        from play import fpsClock, fps
        '''Displays the cell'''
        self.color = CELL_COLOR_STATUS[self.status]
        if self.is_wall:
            self.color = (0,0,0)
        rect = pygame.Rect(self.j*self.cell_w, self.i*self.cell_h, 
                           self.cell_w, self.cell_h)
        pygame.draw.rect(screen, self.color, rect, 0) # The filled rect
        pygame.draw.rect(screen, (0,0,0), rect, 1) # The border of the rect

    def find_neighbors(self, grid) -> List['Cell']:
        '''
        Finds and returns the neighbors of the cell.
        '''
        #north, south, east, west neighbor locations
        nsew = ((self.i-1, self.j),(self.i+1, self.j),
                (self.i, self.j+1),(self.i, self.j-1))
        
        # north-east, south-east, north-west, south-west neighbor locations
        neseswnw = ((self.i-1, self.j+1),(self.i+1, self.j+1),
                    (self.i-1, self.j-1),(self.i+1, self.j-1))
        
        all_directions = nsew + neseswnw
        
        # Use all_directions to traverse diagonally as well
        for i_prime, j_prime in nsew:
            # Bounds check
            if i_prime < 0 or i_prime > self.rows-1 \
                or j_prime < 0 or j_prime > self.cols-1:
                continue
            else:
                self.neighbors.append(grid[i_prime][j_prime])

        return self.neighbors

    def find_maze_neighbors(self, grid) -> List['Cell']:
        '''
        Finds and returns the maze neighbors of the cell. Basically, two 
        cell skip in all directions.
        
        Note: Should probably integrate find_neighbor functions into one
        function that takes a parameter that determines how many cells in 
        each direction to search.
        '''
        #north, south, east, west neighbor locations
        nsew = ((self.i-2, self.j),(self.i+2, self.j),
                (self.i, self.j+2),(self.i, self.j-2))
        
        # north-east, south-east, north-west, south-west neighbor locations
        neseswnw = ((self.i-2, self.j+2),(self.i+2, self.j+2),
                    (self.i-2, self.j-2),(self.i+2, self.j-2))
        
        all_directions = nsew + neseswnw
        
        for i_prime, j_prime in nsew:
            # Bounds check
            if i_prime < 0 or i_prime > self.rows-1 \
                or j_prime < 0 or j_prime > self.cols-1:
                continue
            else:
                self.maze_neighbors.append(grid[i_prime][j_prime])

        return self.maze_neighbors
