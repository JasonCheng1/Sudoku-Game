import pygame
import sys
from settings import *
from buttonClass import *


class App:
    def __init__(self):
        pygame.init()
        self.running = True
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.grid = testBoard2
        self.selected = None
        self.mousePos = None
        self.state = "playing"
        self.playingButtons = []
        self.menuButtons = []
        self.endButtons = []
        self.lockedCells = []
        self.font = pygame.font.SysFont("arial", cellSize//2)
        self.load()
        self.loadButtons()

    def run(self):
        while self.running:
            if self.state == "playing":
                self.playing_events()
                self.playing_update()
                self.playing_draw()
        pygame.quit()
        sys.exit()
    """Playing State Code"""

    def playing_events(self):  # ui portion
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # User Clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = self.mouseOnGrid()  # return true if mouse is on grid else false
                if selected:
                    self.selected = selected
                else:
                    print("not on board")
                    self.selected = None
            # User Types a Key
            if event.type == pygame.KEYDOWN:
                if self.selected and self.selected not in self.lockedCells:
                    if self.isInt(event.unicode):
                        self.grid[self.selected[1]][self.selected[0]] = int(
                            event.unicode)

    def playing_update(self):
        self.mousePos = pygame.mouse.get_pos()
        for button in self.playingButtons:
            button.update(self.mousePos)

    def playing_draw(self):
        self.window.fill(WHITE)
        for button in self.playingButtons:
            button.draw(self.window)
        if self.selected:
            self.drawSelection(self.window, self.selected)
        self.shadeLockedCells(self.window, self.lockedCells)
        self.drawNumbers(self.window)
        self.drawGrid(self.window)
        pygame.display.update()

    """Helper Function"""

    def shadeLockedCells(self, window, locked):
        for cell in locked:
            pygame.draw.rect(window, LOCKEDCELLCOLOR, ((
                cell[0]*cellSize) + gridPos[0], (cell[1]*cellSize) + gridPos[1], cellSize, cellSize))

    def drawNumbers(self, window):
        for yidx, row in enumerate(self.grid):
            for xidx, num in enumerate(row):
                if num != 0:
                    pos = [(xidx * cellSize) + gridPos[0],
                           (yidx * cellSize) + gridPos[1]]
                    self.textToScreen(window, str(num), pos)

    def drawSelection(self, window, pos):
        pygame.draw.rect(
            window, LIGHTBLUE, (gridPos[0]+pos[0]*cellSize, gridPos[1]+pos[1]*cellSize, cellSize, cellSize))

    def drawGrid(self, window):
        pygame.draw.rect(
            window, BLACK, (gridPos[0], gridPos[1], WIDTH-150, HEIGHT-150), 2)
        for x in range(9):
            boundary = x % 3 == 0 and x != 0
            # if x % 3 == 0 and x != 0:
            pygame.draw.line(window, BLUE if boundary else BLACK, (gridPos[0]+(
                x*cellSize), gridPos[1]), (gridPos[0]+(x*cellSize), gridPos[1] + 450), 2 if boundary else 1)
            pygame.draw.line(window, BLUE if boundary else BLACK, (gridPos[0], gridPos[1]+(
                x*cellSize)), (gridPos[0] + 450, gridPos[1]+(x*cellSize)), 2 if boundary else 1)
            # else:
            #     pygame.draw.line(window, BLACK, (gridPos[0]+(x*cellSize), gridPos[1]), (gridPos[0]+(x*cellSize), gridPos[1] + 450))
            #     pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1]+(x*cellSize)), (gridPos[0] + 450, gridPos[1]+(x*cellSize)))

    def mouseOnGrid(self):
        if self.mousePos[0] < gridPos[0] or self.mousePos[1] < gridPos[1]:  # left or above
            return False
        if self.mousePos[0] > gridPos[0] + gridSize or self.mousePos[1] > gridPos[1] + gridSize:  # right or below
            return False
        return ((self.mousePos[0]-gridPos[0])//cellSize, (self.mousePos[1]-gridPos[1])//cellSize)

    def loadButtons(self):
        self.playingButtons.append(Button(20, 40, 100, 40))

    def textToScreen(self, window, text, pos):
        font = self.font.render(text, False, BLACK)
        fontWidth = font.get_width()
        fontHeight = font.get_height()
        pos[0] += (cellSize-fontWidth)//2
        pos[1] += (cellSize-fontHeight)//2
        window.blit(font, pos)

    def load(self):
        self.loadButtons()
        # Setting Locked Cells from Original Board
        for yidx, row in enumerate(self.grid):
            for xidx, num in enumerate(row):
                if num != 0:
                    self.lockedCells.append([xidx, yidx])

    def isInt(self, string):
        try:
            int(string)
            return True
        except error:
            return False
