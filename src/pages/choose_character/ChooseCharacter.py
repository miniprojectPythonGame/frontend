import pygame
import sys
from pygame.locals import *

from src.components.Label import Label
from src.components.Button import Button

from src.components.CharacterSlider import CharacterSlider
from .Measurements import Measurements as meas
from src.globals.mock_data import character_1 as chara_1
from src.globals.mock_data import character_2 as chara_2
from src.globals.mock_data import createNew as createNew

from src.pages.create_character.CreateCharacter import CreateCharacter
from src.pages.city_map.CityMap import CityMap


def ChooseCharacter(screen, mainClock):
    label_page = Label(meas.label_page['text'], meas.label_page['font'], meas.label_page['color'], screen,
                       meas.label_page['x'], meas.label_page['y'], meas.label_page['anchor'])

    characters = CharacterSlider([chara_1, chara_2, createNew], screen)

    bt_prev = Button(meas.bt_prev['color'], meas.bt_prev['x'], meas.bt_prev['y'],
                     meas.bt_prev['width'], meas.bt_prev['height'], screen,
                     meas.bt_prev['text'], meas.bt_prev['font'], path=meas.bt_prev['path'])

    bt_next = Button(meas.bt_next['color'], meas.bt_next['x'], meas.bt_next['y'],
                     meas.bt_next['width'], meas.bt_next['height'], screen,
                     meas.bt_next['text'], meas.bt_next['font'], path=meas.bt_next['path'])

    while True:
        screen.fill((255, 255, 255))

        label_page.draw()
        characters.draw()

        bt_prev.draw()
        bt_next.draw()

        mx, my = pygame.mouse.get_pos()

        # HOVERS
        # Button login: hover
        if characters.curr_main.rect.collidepoint((mx, my)):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                # 'Previous' button
                if bt_prev.rect.collidepoint(event.pos):
                    characters.swipeLeft()

                # 'Next' button
                if bt_next.rect.collidepoint(event.pos):
                    characters.swipeRight()

                if characters.curr_main.rect.collidepoint(event.pos):
                    if characters.curr_main.class_name == '':
                        CreateCharacter(screen, mainClock)
                    else:
                        CityMap(screen, mainClock)

        pygame.display.update()
        mainClock.tick(60)
