import pygame

class ImageField:
    def __init__(self, x, y, width, height, path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(path).convert_alpha()
        self.scale(width, height)

    def scale(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))