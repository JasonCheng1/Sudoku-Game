WIDTH = 600
HEIGHT = 600

# Color
WHITE = (255, 255, 255)  # RGB
BLACK = (0, 0, 0)
BLUE = (0, 76, 153)
LOCKEDCELLCOLOR = (189, 189, 189)
LIGHTBLUE = (52, 177, 235)
# Boards
testBoard1 = [[0 for x in range(9)] for x in range(9)]
testBoard2 = [
    [8, 0, 9, 2, 0, 0, 0, 0, 0],
    [2, 0, 0, 9, 8, 0, 1, 6, 0],
    [0, 3, 0, 0, 0, 7, 0, 0, 8],
    [0, 0, 8, 6, 0, 0, 5, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 3, 0, 0, 8, 4, 0, 0],
    [3, 0, 0, 4, 0, 0, 0, 5, 0],
    [0, 4, 5, 0, 3, 2, 0, 0, 6],
    [0, 0, 0, 0, 0, 6, 2, 0, 5]]


# Postions
gridPos = (75, 100)
cellSize = 50
gridSize = cellSize * 9
