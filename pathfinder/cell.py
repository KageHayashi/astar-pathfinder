import pygame

class Cell():
    def __init__(self, x, y, cols, rows, grid):
        self.x = x 
        self.y = y
        self.color = (0,0,0)
        # Values: 0 = Normal, 1 = Wall, 2 = Start, 3 = End
        self.value = 0

        # States: 0 = Normal, 1 = Hovered, 2 = Pressed
        self.state = 0

    def get_color(self) -> 'RGB Tuple':
        if self.value == 0:
            self.color = (255,255,255)
        else:
            self.color = (255,0,0)

        # TO-DO: Make state color based off of value color
        if self.state == 1:
            self.color = (200,200,200)
        
        return self.color