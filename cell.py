import pygame, random

from typing import List
from heuristics import calculate_manhanttan_heuristics

class Cell():
    def __init__(self, i, j, cols, rows, cell_w, cell_h):
        self.i = i
        self.j = j
        self.f = 0
        self.g = 0
        self.h = 0
        self.is_wall = 0
        self.parent = None
        self.neighbors = []

        self.cols = cols
        self.rows = rows
        self.cell_w = cell_w
        self.cell_h = cell_h

        # Randomize wall generation
        if random.random() <= .25:
            self.is_wall = 1

    def show(self, screen, color):
        '''Displays the cell'''
        if self.is_wall:
            color = (0,0,0)
        rect = pygame.Rect(self.i*self.cell_w, self.j*self.cell_h, 
                           self.cell_w, self.cell_h)
        pygame.draw.rect(screen, color, rect, 0) # The filled rect
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
        
        for i_prime, j_prime in all_directions:
            # Bounds check
            if i_prime < 0 or i_prime > self.rows-1 \
                or j_prime < 0 or j_prime > self.cols-1:
                continue
            else:
                self.neighbors.append(grid[i_prime][j_prime])

        return self.neighbors