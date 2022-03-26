import pygame
import sys
from pygame.locals import *

from src.components.Label import Label
from src.components.ImageField import ImageField
from src.components.InputField import InputField
from src.components.Button import Button

from .Measurements import Measurements as meas

def CreateCharacter(screen, mainClock):
    label_page = Label(meas.label_page['text'], meas.label_page['font'], meas.label_page['color'], screen,
                       meas.label_page['x'], meas.label_page['y'], meas.label_page['anchor'])

    img_avatarPreview = ImageField(meas.img_avatarPreview['x'], meas.img_avatarPreview['y'],
                                   meas.img_avatarPreview['width'], meas.img_avatarPreview['height'],
                                   '../images/characters/mage_1.png', screen)

    # NAME SECTION
    label_name = Label(meas.label_name['text'], meas.label_name['font'], meas.label_name['color'], screen,
                       meas.label_name['x'], meas.label_name['y'], meas.label_name['anchor'])

    input_name = InputField(meas.input_name['x'], meas.input_name['y'],
                            meas.input_name['width'], meas.input_name['height'],
                            meas.input_name['border'], meas.input_name['color'],
                            screen, 'Nickname', meas.nickname_length)

    # CLASS SECTION
    label_class = Label(meas.label_class['text'], meas.label_class['font'], meas.label_class['color'], screen,
                        meas.label_class['x'], meas.label_class['y'], meas.label_class['anchor'])

    bt_warrior = Button(meas.bt_class_active['color'],
                        meas.bt_warrior['x'], meas.bt_warrior['y'],
                        meas.bt_warrior['width'], meas.bt_warrior['height'], screen,
                        meas.bt_warrior['text'],
                        path=meas.bt_warrior['path_white'],
                        image_ofset=meas.bt_class_active['image_offset'],
                        border_radius=meas.bt_class_active['border_radius'])

    bt_mage = Button(meas.bt_class_inactive['color'],
                        meas.bt_mage['x'], meas.bt_mage['y'],
                        meas.bt_mage['width'], meas.bt_mage['height'], screen,
                        meas.bt_mage['text'],
                        path=meas.bt_mage['path_gray'],
                        image_ofset=meas.bt_class_inactive['image_offset'],
                        border_radius=meas.bt_class_inactive['border_radius'])

    bt_archer = Button(meas.bt_class_inactive['color'],
                        meas.bt_archer['x'], meas.bt_archer['y'],
                        meas.bt_archer['width'], meas.bt_archer['height'], screen,
                        meas.bt_archer['text'],
                        path=meas.bt_archer['path_gray'],
                        image_ofset=meas.bt_class_inactive['image_offset'],
                        border_radius=meas.bt_class_inactive['border_radius'])

    # AVATARS SECTION
    label_avatar = Label(meas.label_avatar['text'], meas.label_avatar['font'], meas.label_avatar['color'], screen,
                         meas.label_avatar['x'], meas.label_avatar['y'], meas.label_avatar['anchor'])

    while True:
        screen.fill((255, 255, 255))

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        label_page.draw()

        img_avatarPreview.draw()

        label_name.draw()
        input_name.draw()

        label_class.draw()
        bt_warrior.draw()
        bt_mage.draw()
        bt_archer.draw()

        label_avatar.draw()

        mx, my = pygame.mouse.get_pos()

        # HOVERS
        # Class Button: warrior
        if bt_warrior.rect.collidepoint((mx, my)):
            bt_warrior.onHoverOn()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            bt_warrior.onHoverOff()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # Class Button: mage
        if bt_mage.rect.collidepoint((mx, my)):
            bt_mage.onHoverOn()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            bt_mage.onHoverOff()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # Class Button: archer
        if bt_archer.rect.collidepoint((mx, my)):
            bt_archer.onHoverOn()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            bt_archer.onHoverOff()
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
                pass

        pygame.display.update()
        mainClock.tick(60)
