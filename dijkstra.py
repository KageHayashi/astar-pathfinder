import pygame
import math

from os import close, fspath
from typing import List
from cell import Cell
from helpers import find_lowest_dist, find_lowest_f, reconstruct_path, update_path
from heuristics import calculate_manhanttan_heuristics


def dijkstra(grid, start, end) -> bool:
    import play
    # Set q is the queue for cells and set p is to keep track 
    # of all cells taken already in order to colorize them.
    q = []
    p = []

    # We begin at the start cell
    start.dist = 0
    q.append(start)

    while (q != []):
        # Find the cell with the lowest dist value from 
        # the queue and make that our current cell
        current = find_lowest_dist(q)
        p.append(current)
        q.remove(current)

        # If we found a path to the end
        # print the path and return True
        if current == end:
            path = update_path(current)
            path.append(end)
            for c in p:
                c.status = 'close'
            for c in path:
                c.status = 'path'
            play.show_cells(grid, play.fps)
            print(reconstruct_path(path))
            return 1

        # For each neighbor of the current cell,
        # calculate a new dist value based on the current 
        # cell. If the new dist value is less than the 
        # previous value, append the neighbor to our queue
        for neighbor in current.find_neighbors(grid):
            temp = current.dist + 1
            if temp < neighbor.dist and not neighbor.is_wall:
                neighbor.status = 'close'
                neighbor.dist = temp
                neighbor.parent = current
                q.append(neighbor)
        
        # Colorize cells taken
        path = update_path(current)
        for c in p:
            c.status = 'close'
        for c in path:
            c.status = 'path'
        play.show_cells(grid, play.fps)

        # Check kill. Makes it possible to quit while searching
        for event in pygame.event.get():
            play.check_kill(event)
    
    print('no path')
    return 0