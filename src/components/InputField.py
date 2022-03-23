import pygame

class InputField:
    def __init__(self, x, y, width, height, border, colors,
                 screen, placeholder='None', max_length=10, isPassword=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.border = border
        self.font = pygame.font.Font(None, height)
        self.color_active = colors.active
        self.color_inactive = colors.inactive
        self.color_text = colors.text_color
        self.active = False
        self.color = self.color_inactive
        self.screen = screen
        self.placeholder = placeholder
        self.text = ''
        self.visibleText = placeholder
        self.isPassword = isPassword
        self.max_length = max_length
        self.isEmpty = True
        self.text_surface = self.font.render(self.visibleText, True, colors.text_color)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, 2)
        self.text_surface = self.font.render(self.visibleText, True, self.color_text)
        self.screen.blit(self.text_surface, (self.rect.x + 10, self.rect.y + 10))

    def appendText(self, character):
        if self.isEmpty:
            self.text = ''
            self.visibleText = ''
            self.isEmpty = False

        if len(self.text) < self.max_length:
            if self.isPassword:
                self.text += character
                self.visibleText += '*'
            else:
                self.text += character
                self.visibleText = self.text

    def subtractText(self):
        self.text = self.text[:-1]
        self.visibleText = self.visibleText[:-1]

        if len(self.text) == 0:
            self.isEmpty = True
            self.visibleText = self.placeholder

    def activate(self):
        self.active = True
        self.color = self.color_active

    def deactivate(self):
        self.active = False
        self.color = self.color_inactive