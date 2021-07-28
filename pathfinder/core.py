import pygame, sys
from grid import Grid

BLACK = (0, 0, 0)
WHITE = (255,255,255)
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
GRID_ROWS = 5
GRID_COLS = 5

def main():
    # Initialize pygame screen
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    # Initialize game grid
    g = Grid(GRID_ROWS, GRID_COLS, WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN)
    # g.grid_base[0][0].value = 1
    # g.grid_base[1][1].value = 2
    # g.grid_base[2][2].value = 3
    # g.grid_base[3][3].value = 4
    # g.grid_base[4][4].value = 5
    g.print_grid_base()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Mouse hover effect
        g.reset_hover()
        mouse_pos = pygame.mouse.get_pos()
        x,y = mouse_pos
        g_col = x // (WINDOW_WIDTH // GRID_COLS)
        g_row = y // (WINDOW_HEIGHT // GRID_ROWS)
        g.grid_base[g_row][g_col].state = 1
        

        g.display()
        pygame.display.update()


def drawGrid():
    blockSize = 100
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)


if __name__ == '__main__':
    main()