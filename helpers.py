from typing import List
from cell import Cell

def find_lowest_f(open_cells):
    '''
    Given a set of open cells, finds and returns
    the cell with the lowest f value.
    '''
    lowest_f = open_cells[0]
    for cell in open_cells:
        if cell.f < lowest_f.f:
            lowest_f = cell
    
    return lowest_f

def update_path(current):
    '''
    Given the current cell, find the path we took to 
    get there.
    '''
    path = []
    temp = current
    while (temp.parent):
        path.append(temp.parent)
        temp.parent.status = 'path'
        temp = temp.parent

    return path

def reconstruct_path(path: List[Cell]) -> str:
    '''
    Returns a string with the i,j coordinates 
    of cells taken in path
    '''
    path.reverse()
    path_route = [(cell.i,cell.j) for cell in path]
    s = ""
    s += f"Cells visited: {len(path_route)}\n"
    s += f"Path: {path_route}"
    
    return s