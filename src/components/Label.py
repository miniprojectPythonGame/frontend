import pygame

class Label:
    def __init__(self, text, font, color, surface, x ,y, anchor="topleft"):
        self.x = x
        self.y = y
        self.surface = surface
        self.text = text
        self.text_obj = font.render(text, 1, color)
        self.rect = self.text_obj.get_rect()
        self.setAnchor(anchor, x, y)

    def setAnchor(self, anchor, x, y):
        if anchor == 'topleft':
            self.rect.topleft = (x,y)

        elif anchor == 'topright':
            self.rect.topright = (x,y)

        else:
            print("Error")

    def draw(self):
        self.surface.blit(self.text_obj, self.rect)