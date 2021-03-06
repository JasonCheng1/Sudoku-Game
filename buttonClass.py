import pygame


class Button:  # Class to create buttons for the board
    def __init__(self, x, y, width, height, text=None, color=(73, 73, 73), highlightedColor=(189, 189, 189), function=None, params=None):
        self.image = pygame.Surface((width, height))
        self.pos = (x, y)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.txt = text
        self.color = color
        self.highlightedColor = highlightedColor
        self.function = function
        self.params = params
        self.highlighted = False

    def update(self, mouse):
        if self.rect.collidepoint(mouse):
            self.highlighted = True
        else:
            self.highlighted = False

    def draw(self, window):
        self.image.fill(
            self.highlightedColor if self.highlighted else self.color)
        window.blit(self.image, self.pos)
