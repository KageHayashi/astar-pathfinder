from cell import Cell
from grid import Grid
from colors import Color

import heuristics

def astar(grid, start, finish):
    openCells = []
    closeCells = []
    openCells.append(start)
    start.in_open = True
    steps = 0
    lowestF = 0
    while len(openCells) > 0:
        current_cell = openCells[lowestF]
        steps+=1
        for i in range(len(openCells)):
            if openCells[i].f < current_cell.f:
                current_cell = openCells[i]
                lowestF = i

        current_cell.value = 1
        current_cell.f = 0

        openCells.pop(lowestF)
        current_cell.get_neighbors()
        neighbors = current_cell.neighbors

        #for each offspring
        for neighbor in neighbors:
            col = neighbor.col
            row = neighbor.row
            #if offspring is the goal, stop search
            if col == finish.col and row == finish.row:
                neighbor.g = current_cell.g + 1
                neighbor.h = heuristics.calculate_euclidean_heuristics(neighbor, finish)
                neighbor.f = neighbor.g + neighbor.h
                print("Done")
                print("Steps taken:", steps)
                neighbor.value = 3
                return True

            #If offspring not in closeCells and not blocked then calculate temporary values of g, h, and f.
            if neighbor not in closeCells:
                tempG = current_cell.g + 1
                tempH = heuristics.calculate_euclidean_heuristics(neighbor, finish)
                tempF = tempG + tempH

                #if cell with the same position as offspring is already in the openCells with a smaller f value, skip it
                #in other words, put the offspring into the openCells if it's not already on the openCells or if the cell already in the list has a bigger f value
                if neighbor not in openCells:
                    neighbor.g = tempG
                    neighbor.h = tempH
                    neighbor.f = tempF
                    openCells.append(neighbor)
                elif neighbor in openCells and tempF < neighbor.f:
                    neighbor.f = tempF
        #end of offspring loop

        #push current_cell onto closeCells
        closeCells.append(current_cell)
        current_cell.in_close = True

        for neighbor in neighbors:
            neighbor.value = 2
            neighbor.value = 2
            # print(child.x, child.y)
            # print(child.x, child.y, child.f)

        '''FOLOWING USED FOR DEBUGGING'''
        # print("open: ")
        # for cell in openCells:
        #     print(f'({cell.x}, {cell.y}, {cell.f})')
        # print("closed: ")
        # for cell in closeCells:
        #     print(f'({cell.x}, {cell.y}, {cell.f})')
        # print("offsprings: ")
        # for cell in offsprings:
        #     print(f'({cell.x}, {cell.y}, {cell.f})')
        # print("")

        #Visualize the path
        for i in range(len(openCells)):
            openCells[i].display_cell()

        for i in range(len(closeCells)):
            if closeCells[i] != start:
                closeCells[i].display_cell()

    return True