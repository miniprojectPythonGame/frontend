import pygame
import sys
from pygame.locals import *

from src.components.Navbar import Navbar
from src.components.Button import Button
from src.components.ImageField import ImageField
from .Measurements import Measurements as meas

from src.pages.character_profile.CharacterProfile import CharacterProfile
from src.pages.settings.Settings import Settings
from src.pages.armor_shop.ArmorShop import ArmorShop


def CityMap(screen, mainClock):

    showHand = False

    img_map = ImageField(meas.img_map['x'], meas.img_map['y'],
                         meas.img_map['width'], meas.img_map['height'],
                         meas.img_map['img_path'], screen)

    bt_marketplace = Button(meas.default_color, 220, 140, 100, 30, screen,
                            text='Marketplace', font=meas.text_font, border_radius=5)

    bt_arena = Button(meas.default_color, 300, 200, 80, 30, screen,
                      text='Arena', font=meas.text_font, border_radius=5)

    bt_weaponShop = Button(meas.default_color, 150, 250, 110, 30, screen,
                           text='Weapon Shop', font=meas.text_font, border_radius=5)

    bt_magicShop = Button(meas.default_color, 400, 350, 100, 30, screen,
                          text='Magic Shop', font=meas.text_font, border_radius=5)

    bt_armorShop = Button(meas.default_color, 500, 450, 100, 30, screen,
                          text='Armor Shop', font=meas.text_font, border_radius=5)

    bt_tavern = Button(meas.default_color, 600, 200, 80, 30, screen,
                       text='Tavern', font=meas.text_font, border_radius=5)

    displayedContent = [
        img_map,
        bt_marketplace, bt_arena, bt_weaponShop, bt_magicShop, bt_armorShop, bt_tavern
    ]

    navbar = Navbar(screen)

    while True:
        screen.fill((255, 255, 255))
        if showHand:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for elem in displayedContent:
            elem.draw()

        navbar.draw()

        mx, my = pygame.mouse.get_pos()

        # Button login hover
        if bt_marketplace.rect.collidepoint((mx, my)):
            bt_marketplace.onHoverOn()
            showHand = True
        elif bt_arena.rect.collidepoint((mx, my)):
            bt_arena.onHoverOn()
            showHand = True
        elif bt_weaponShop.rect.collidepoint((mx, my)):
            bt_weaponShop.onHoverOn()
            showHand = True
        elif bt_magicShop.rect.collidepoint((mx, my)):
            bt_magicShop.onHoverOn()
            showHand = True
        elif bt_armorShop.rect.collidepoint((mx, my)):
            bt_armorShop.onHoverOn()
            showHand = True
        elif bt_tavern.rect.collidepoint((mx, my)):
            bt_tavern.onHoverOn()
            showHand = True
        else:
            bt_marketplace.onHoverOff()
            bt_arena.onHoverOff()
            bt_weaponShop.onHoverOff()
            bt_magicShop.onHoverOff()
            bt_armorShop.onHoverOff()
            bt_tavern.onHoverOff()
            showHand = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                # LEFT CLICK
                if event.button == 1:
                    # HANDLE NAVBAR BUTTONS
                    # CHARACTER PROFILE
                    if navbar.bt_profile.rect.collidepoint(event.pos):
                        print("Redirecting: CityMap.py -> Character Profile.py")
                        CharacterProfile(screen, mainClock)

                    # SETTINGS
                    if navbar.bt_settings.rect.collidepoint(event.pos):
                        print("Redirecting: CityMap.py -> Settings.py")
                        Settings(screen, mainClock)

                    # HANDLE CITY PLACES
                    if bt_armorShop.rect.collidepoint(event.pos):
                        print("Redirecting: CityMap.py -> ArmorShop.py")
                        ArmorShop(screen, mainClock)

                # RIGHT CLICK

        pygame.display.update()
        mainClock.tick(60)
