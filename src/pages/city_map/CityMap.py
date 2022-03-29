import pygame
import sys
from pygame.locals import *

from src.components.Navbar import Navbar
from .Measurements import Measurements as meas

from src.pages.character_profile.CharacterProfile import CharacterProfile
from src.pages.settings.Settings import Settings

def CityMap(screen, mainClock):

    navbar = Navbar(screen)

    while True:
        screen.fill((255, 255, 255))
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        navbar.draw()

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                # HANDLE NAVBAR BUTTONS
                # CHARACTER PROFILE
                if navbar.bt_profile.rect.collidepoint(event.pos):
                    print("Redirecting: CityMap.py -> Character Profile.py")
                    CharacterProfile(screen, mainClock)

                # SETTINGS
                if navbar.bt_settings.rect.collidepoint(event.pos):
                    print("Redirecting: CityMap.py -> Settings.py")
                    Settings(screen, mainClock)


        pygame.display.update()
        mainClock.tick(60)
