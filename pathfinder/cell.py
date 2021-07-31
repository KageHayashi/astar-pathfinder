import pygame
from colors import Color

class Cell():
    def __init__(self, row, col, cols, rows, cell_size, grid):
        # Basic cell info
        self.row = row
        self.col = col
        self.color = Color.WHITE
        self.cols = cols
        self.rows = rows
        self.grid = grid
        self.cell_size = cell_size

        # Specific cell function
        self.value = 0 # 0 = Normal, 1 = Open/Neighbor, 2 = Wall/Obstacle, 3 = Start, 4 = End
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
        self.in_open = False
        self.in_close = False

    def get_color(self) -> 'None':
        if self.value == 0:
            self.color = Color.WHITE
        elif self.value == 1:
            self.color = Color.GREEN
        elif self.value == 2:
            self.color = Color.BLACK
        elif self.value == 3:
            self.color = Color.BLUE
        elif self.value == 4:
            self.color = Color.YELLOW

        # TO-DO: Show alorithm working colors.
        ## Dijkstra's
        if self.visited:
            self.color = Color.RED
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
        rect = pygame.Rect(self.col*self.cell_size, self.row*self.cell_size, 
                           self.cell_size, self.cell_size)
        pygame.draw.rect(self.grid.screen, self.get_color(), rect, 0) # The filled rect
        pygame.draw.rect(self.grid.screen, Color.BLACK, rect, 1) # The border of the rect
        pygame.display.update()

    def display_cell_text(self) -> None:
        '''
        Displays the cell text onto the cell rectangle
        '''
        text = self.font.render(self.text, True, Color.BLACK)
        self.grid.screen.blit(text, (self.row*self.cell_size+3, 
                                     self.col*self.cell_size+3))

    def get_neighbors(self) -> ['Cell']:
        '''
        Returns a list of all the neighboring cells
        '''
        #north, south , east, west offsprings
        nsew = ((self.col, self.row-1), (self.col, self.row+1), 
                (self.col+1, self.row), (self.col-1, self.row))
        
        for direction in nsew:
            if direction[0] == -1 or direction[1] == -1: # Check if at top row or left-most column
                continue
            elif direction[0] < self.cols \
                    and direction[0] >= 0 \
                    and direction[1] < self.rows \
                    and direction[1] >= 0 \
                    and not (self.grid.grid_base[direction[1]][direction[0]].value == 1):
                self.neighbors.append(self.grid.grid_base[direction[1]][direction[0]])

        #north-east, south-east, south-west, north-west offsprings
        neseswnw = ((self.col+1, self.row-1), (self.col+1, self.row+1), 
                    (self.col-1, self.row+1), (self.col-1, self.row-1))
        
        for direction in neseswnw:
            if direction[0] == -1 or direction[1] == -1:
                continue
            elif direction[0] < self.cols \
                    and direction[0] >= 0 \
                    and direction[1] < self.rows \
                    and direction[1] >= 0 \
                    and not (self.grid.grid_base[direction[1]][direction[0]].value == 1):
                self.neighbors.append(self.grid.grid_base[direction[1]][direction[0]])

        return self.neighbors