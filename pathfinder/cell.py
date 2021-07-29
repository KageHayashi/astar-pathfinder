import pygame
from colors import Color

class Cell():
    def __init__(self, x, y, cols, rows, cell_size, grid):
        # Basic cell info
        self.x = x 
        self.y = y
        self.color = Color.BLACK
        self.cols = cols
        self.rows = rows
        self.grid = grid
        self.cell_size = cell_size

        # Specific cell function
        self.value = 0 # 0 = Normal, 1 = Wall/Obstacle, 2 = Start, 3 = End
        self.state = 0 # 0 = Normal, 1 = Hovered, 2 = Pressed
        self.font = pygame.font.SysFont('Calibri', int(cell_size//5))
        self.text = "-"

        # Specific Algorithmic values
        self.neighbors = []
        self.parent = None
        
        ## Dijkstra's
        self.visited = False
        self.distance = float('inf')
        
        ## A*
        self.f = 0
        self.g = 0
        self.h = 0
        self.in_open = 0
        self.in_close = 0

    def get_color(self) -> 'RGB Tuple':
        if self.value == 0:
            self.color = Color.WHITE
        elif self.value == 1:
            self.color = Color.RED
        elif self.value == 2:
            self.color = Color.BLUE
        elif self.value == 3:
            self.color = Color.GREEN

        # TO-DO: Show alorithm working colors.
        ## Dijkstra's
        if self.visited:
            self.color = Color.GREEN
        ## A*
        if self.in_open:
            self.color = Color.GREEN
        elif self.in_close:
            self.color = Color.RED

        # TO-DO: Make state color based off of value color
        if self.state == 1:
            self.color = Color.GREY
        
        return self.color

    def display_cell(self) -> None:
        '''
        Displays the cell onto the grid screen
        '''
        rect = pygame.Rect(self.y*self.cell_size, self.x*self.cell_size, 
                           self.cell_size, self.cell_size)
        pygame.draw.rect(self.grid.screen, self.get_color(), rect, 0) # The filled rect
        pygame.draw.rect(self.grid.screen, Color.BLACK, rect, 1) # The border of the rect

    def display_cell_text(self) -> None:
        '''
        Displays the cell text onto the cell rectangle
        '''
        text = self.font.render(self.text, True, Color.BLACK)
        self.grid.screen.blit(text, (self.y*self.cell_size+3, 
                                     self.x*self.cell_size+3))