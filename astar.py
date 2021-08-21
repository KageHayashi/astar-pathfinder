import pygame

from os import close
from typing import List
from cell import Cell
from helpers import find_lowest_f, reconstruct_path, update_path
from heuristics import calculate_manhanttan_heuristics


def astar(grid, start, end) -> bool:
    import play
    '''
    Runs the A* search given a grid, starting cell, and end cell.
    Returns true if there's a path, false otherwise.
    '''
    # The set of cells that are open
    # Initially set to only the start node
    open_cells = [start]

    # The set of cells that are closed
    # Initially empty
    closed_cells = []

    # Holds the cells of the path route so far taken
    path = []

    while (open_cells != []):
        lowest_f = find_lowest_f(open_cells)
        current = lowest_f

        # Found a path to end
        if current == end:
            path = update_path(current)
            path.append(current)
            play.update_cells(grid, path, open_cells, closed_cells)
            print("FOUND!")
            print(reconstruct_path(path))
            return True

        open_cells.remove(current)
        closed_cells.append(current)

        # For each neighbor, calculate their f value and append to open set if 
        # not already visited
        current.find_neighbors(grid)
        for neighbor in current.neighbors:
            if neighbor not in closed_cells and not neighbor.is_wall:
                tempG = current.g + 1

                # Update cell g value if already in open set, 
                # else add to open set
                if neighbor in open_cells:
                    if tempG < neighbor.g:
                        neighbor.g = tempG
                else:
                    neighbor.g = tempG
                    open_cells.append(neighbor)
                
                # Calculate f value and assign parent
                neighbor.h = calculate_manhanttan_heuristics(neighbor, end)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.parent = current

        # Update path taken so far by looping through
        # all parents and adding to path
        path = update_path(current)

        # Update the grid and display to screen
        play.update_cells(grid, path, open_cells, closed_cells)

        # Check kill. Makes it possible to quit while searching
        for event in pygame.event.get():
            play.check_kill(event)

    return False