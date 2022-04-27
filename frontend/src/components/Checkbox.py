import pygame

class Checkbox():
    def __init__(self, color, x, y, width, height, surface, border):
        self.colorSchemes = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = surface
        self.border = border
        self.rect = pygame.Rect(x, y, width, height)
        self.isSelected = False

    def draw(self):
        if self.isSelected:
            pygame.draw.rect(self.surface, self.colorSchemes.active, self.rect, 0)
        else:
            pygame.draw.rect(self.surface, self.colorSchemes.inactive, self.rect, self.border)

    def select(self):
        self.isSelected = True

    def deselect(self):
        self.isSelected = False