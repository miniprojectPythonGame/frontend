import pygame

class ColorSchemes:
    def __init__(self,  active='lightskyblue3', inactive='gray26',
                        text_color='gray26', text_secondary_color='gray98'):
        self.active = pygame.Color(active)
        self.inactive = pygame.Color(inactive)
        self.text_color = pygame.Color(text_color)
        self.text_secondary_color = pygame.Color(text_secondary_color)
        self.white = pygame.Color('white')
        self.black = pygame.Color('black')