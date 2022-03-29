import pygame

from .ImageField import ImageField

from src.globals.const_values import *


def setPath(path):
    if path is None:
        return '../images/icons/add_item.png'
    else:
        return path


class ItemBox:
    def __init__(self, x, y, width, height, screen, color=pygame.Color('#555555'),
                 path=None, border=3, offset=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen
        self.path = path
        self.border = border
        self.offset = offset
        self.image = ImageField(x + offset, y + offset,
                                width - 2 * offset, height - 2 * offset,
                                setPath(path), screen)
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, self.border)
        self.image.draw()
