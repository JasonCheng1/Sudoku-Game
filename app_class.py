import pygame, sys
from settings import *

class App:
    def __init__(self):
        pygame.init()
        self.running = True
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        self.grid = testBoard
        self.selected = None
        self.mousePos = None
        
    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()

    def events(self):#ui portion
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = self.mouseOnGrid() #return true if mouse is on grid else false
                if selected:
                    self.selected = selected
                else:
                    print("not on board")
                    self.selected = None

    def update(self):
        self.mousePos = pygame.mouse.get_pos()

    def draw(self):
        self.window.fill(WHITE)
        if self.selected:
            self.drawSelection(self.window, self.selected)
        self.drawGrid(self.window)
        pygame.display.update()
    
    def drawSelection(self, window, pos):
        pygame.draw.rect(window, LIGHTBLUE, (gridPos[0]+pos[0]*cellSize, gridPos[1]+pos[1]*cellSize, cellSize, cellSize))

    def drawGrid(self, window):
         pygame.draw.rect(window, BLACK, (gridPos[0], gridPos[1], WIDTH-150, HEIGHT-150), 2)
         for x in range(9):
             if x % 3 == 0 and x != 0:
                pygame.draw.line(window, BLUE, (gridPos[0]+(x*cellSize), gridPos[1]), (gridPos[0]+(x*cellSize), gridPos[1]  + 450), 2)
                pygame.draw.line(window, BLUE, (gridPos[0], gridPos[1]+(x*cellSize)), (gridPos[0]+ 450, gridPos[1]+(x*cellSize)), 2)
             else:
                pygame.draw.line(window, BLACK, (gridPos[0]+(x*cellSize), gridPos[1]), (gridPos[0]+(x*cellSize), gridPos[1]  + 450))
                pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1]+(x*cellSize)), (gridPos[0]+ 450, gridPos[1]+(x*cellSize)))

    def mouseOnGrid(self):
        if self.mousePos[0] < gridPos[0] or self.mousePos[1] < gridPos[1]:#left or above
            return False
        if self.mousePos[0] > gridPos[0] + gridSize or self.mousePos[1] > gridPos[1] + gridSize:#right or below
            return False
        return ((self.mousePos[0]-gridPos[0])//cellSize, (self.mousePos[1]-gridPos[1])//cellSize)