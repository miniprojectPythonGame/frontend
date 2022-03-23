import pygame, sys
from pygame.locals import *
from src.pages.login_screen.LoginScreen import LoginScreen
from src.pages.register_screen.RegisterScreen import RegisterScreen

from globals.const_values import *

def getWindowSize():
    return SCREEN_WIDTH * SIZE_FACTOR, SCREEN_HEIGHT * SIZE_FACTOR

# Pygame initials
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Heroic: Login screen")
programIcon = pygame.image.load('../images/icons/armor.png')
pygame.display.set_icon(programIcon)
screen = pygame.display.set_mode(getWindowSize(), 0, 32)
base_font = pygame.font.Font(None, 32)

# font = pygame.font.SysFont('calibri', 32)

# def map():
#     running = True
#     while running:
#         screen.fill((0,0,0))
#         draw_text('map', font, (255, 255, 255), screen, 20, 20)
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     running = False
#
#         pygame.display.update()
#         mainClock.tick(60)
#
# def options():
#     running = True
#     while running:
#         screen.fill((0,0,0))
#         draw_text('options', font, (255, 255, 255), screen, 20, 20)
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     running = False
#
#         pygame.display.update()
#         mainClock.tick(60)

if __name__ == "__main__":
    LoginScreen(screen, mainClock)