import pygame
import sys
from pygame.locals import *

from src.components.Label import Label
from src.components.Button import Button
from src.components.CharacterEquipment import CharacterEquipment
from src.components.ItemGrid import ItemGrid

from .Measurements import Measurements as meas


def CharacterProfile(screen, mainClock):
    running = True

    label_page = Label(meas.label_page['text'], meas.label_page['font'], meas.label_page['color'],
                       screen, meas.label_page['x'], meas.label_page['y'], meas.label_page['anchor'])

    bt_return = Button(meas.bt_return['color'], meas.bt_return['x'], meas.bt_return['y'],
                       meas.bt_return['width'], meas.bt_return['height'], screen,
                       path=meas.bt_return['path'])

    ce_characterEqPreview = CharacterEquipment(meas.ce_characterEqPreview['x'],
                                               meas.ce_characterEqPreview['y'],
                                               meas.ce_characterEqPreview['font'],
                                               meas.ce_characterEqPreview['colors'],
                                               meas.ce_characterEqPreview['character_ref'],
                                               screen)

    ig_backpack = ItemGrid(meas.window_width - 350 - meas.margin, meas.margin,
                           80, 10, 4, 24, screen, meas.ig_backpack['backpack_ref'])

    while running:
        screen.fill((255, 255, 255))
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        label_page.draw()
        bt_return.draw()
        ce_characterEqPreview.draw()
        ig_backpack.draw()

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
                # HANDLE RETURN BUTTON
                if bt_return.rect.collidepoint(event.pos):
                    running = False
                    print("Redirecting: CharacterProfile.py -> CityMap.py")

        pygame.display.update()
        mainClock.tick(60)
