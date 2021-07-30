from dijkstras import dijkstra
import pygame, sys
from grid import Grid
from colors import Color

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
GRID_ROWS = 10
GRID_COLS = 10

def main():
    # Initialize pygame systems
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(Color.WHITE)


    # Initialize game grid
    g = Grid(GRID_ROWS, GRID_COLS, WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN)
    # g.grid_base[0][0].value = 2
    # g.grid_base[GRID_ROWS-1][GRID_COLS-1].value = 3
    start = g.grid_base[0][0]
    end = g.grid_base[GRID_ROWS-1][GRID_COLS-1]
    # g.print_grid_base()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    try:
                        dijkstra(g, start, end)
                    except Exception as e: 
                        print(e)

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
            pygame.draw.rect(SCREEN, Color.BLACK, rect, 1)


if __name__ == '__main__':
    main()
