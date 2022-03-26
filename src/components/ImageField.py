import pygame


class ImageField:
    def __init__(self, x, y, width, height, path, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(path).convert_alpha()
        self.scale(width, height)

    def scale(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
