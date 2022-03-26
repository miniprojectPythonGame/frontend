import pygame

from .ImageField import ImageField

class Button():
    def __init__(self, color, x, y, width, height, screen,
                 text, font, border=0, path=None):
        self.colorSchemes = color
        self.color = color.inactive
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.text = text
        self.font = font
        self.image = self.makeImage(path)
        self.rect = pygame.Rect(x, y, width, height)
        self.border = border


    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, self.border)

        if self.text != '':
            if self.border == 0:
                text = self.font.render(self.text, 1, self.colorSchemes.text_secondary_color)
            else:
                text = self.font.render(self.text, 1, self.colorSchemes.text_color)
            self.screen.blit(text,
                     (self.x + (self.width / 2 - text.get_width() / 2),
                      self.y + (self.height / 2 - text.get_height() / 2) + self.height*0.06))

        if self.image:
            self.image.draw()

    def makeImage(self, path):
        if path:
            return ImageField(self.x, self.y, self.width, self.height, path, self.screen)
        else:
            return None

    def onHoverOn(self):
        self.color = self.colorSchemes.active

    def onHoverOff(self):
        self.color = self.colorSchemes.inactive
