from colors import Color
import pygame
from cell import Cell

class Grid:
    def __init__(self, rows, cols, width, height, screen):
        # Rows and cols are the number of cells 
        # Width and height refer to the window size of the whole grid
        # Screen is the pygame screen object to display the grid
        # Cell_size is the pixel size of a single cell
        self.rows = rows 
        self.cols = cols 
        self.width = width 
        self.height = height 
        self.screen = screen 
        self.cell_size = height/rows

        self.SHOW_CELL_TEXT = True

        # grid_base is the 2-D array representation of the grid
        self.grid_base = [[None for j in range(cols)] for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                self.grid_base[i][j] = Cell(i, j, cols, rows, self.cell_size, self)


    # def display(self):
    #     '''
    #     Displays the grid onto the screen
    #     '''
    #     for i in range(self.rows):
    #         for j in range(self.cols):
    #             rect = pygame.Rect(j*self.cell_size, i*self.cell_size, self.cell_size, self.cell_size)
                
    #             # The filled rect
    #             pygame.draw.rect(self.screen,self.grid_base[i][j].get_color(), rect, 0)

    #             # The border of the rect
    #             pygame.draw.rect(self.screen, Color.BLACK, rect, 1)

    def display(self):
        for row in self.grid_base:
            for cell in row:
                cell.display_cell()
                if self.SHOW_CELL_TEXT:
                    cell.display_cell_text()


    def reset_hover(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid_base[i][j].state == 1:
                    self.grid_base[i][j].state = 0


    def print_grid_base(self):
        '''
        Prints the grid base onto the terminal. Good for debugging.
        '''
        for i in range(self.rows):
            for j in range(self.cols):
                if j < self.cols - 1:
                    print(self.grid_base[i][j].value, end='  ')
                else:
                    print(self.grid_base[i][j].value)