import pygame
import sys
from pygame.locals import *

from src.components.Label import Label
from src.components.ImageField import ImageField
from src.components.InputField import InputField
from src.components.Button import Button
from src.pages.choose_character.CharacterPreview import CharacterPreview

from .Measurements import Measurements as meas
from src.globals.mock_data import warrior_avatars, mage_avatars, archer_avatars

def CreateCharacter(screen, mainClock):

    def generateAvatarsOfCurrentClass(currentClass):
        temp = []
        if currentClass == 'warrior':
            for i in range(len(warrior_avatars)):
                temp.append(ImageField(meas.images[i]['x'], meas.images[i]['y'],
                                         meas.images[i]['width'], meas.images[i]['height'],
                                         warrior_avatars[i]['rect'], screen))

        if currentClass == 'mage':
            for i in range(len(warrior_avatars)):
                temp.append(ImageField(meas.images[i]['x'], meas.images[i]['y'],
                                         meas.images[i]['width'], meas.images[i]['height'],
                                         mage_avatars[i]['rect'], screen))

        if currentClass == 'archer':
            for i in range(len(warrior_avatars)):
                temp.append(ImageField(meas.images[i]['x'], meas.images[i]['y'],
                                         meas.images[i]['width'], meas.images[i]['height'],
                                         archer_avatars[i]['rect'], screen))
        return temp

    def reloadPreviewBars(name, className):
        temp_name = Label(name, meas.label_curr_name['font'],
                                meas.label_curr_name['color'], screen,
                                meas.label_curr_name['x'], meas.label_curr_name['y'], meas.label_curr_name['anchor'])

        temp_class = Label(className.capitalize(), meas.label_curr_class['font'],
                                 meas.label_curr_class['color'], screen,
                                 meas.label_curr_class['x'], meas.label_curr_class['y'],
                                 meas.label_curr_class['anchor'])
        return temp_name, temp_class

    curr_active = 'warrior'

    label_page = Label(meas.label_page['text'], meas.label_page['font'], meas.label_page['color'], screen,
                       meas.label_page['x'], meas.label_page['y'], meas.label_page['anchor'])

    img_avatarPreview = ImageField(meas.img_avatarPreview['x'], meas.img_avatarPreview['y'],
                                   meas.img_avatarPreview['width'], meas.img_avatarPreview['height'],
                                   meas.img_avatarPreview['path'], screen)

    cos = CharacterPreview(meas.img_avatarPreview['x'], meas.img_avatarPreview['y'],
                           meas.img_avatarPreview['width'], meas.img_avatarPreview['height'],
                           meas.img_avatarPreview['width']-100, meas.property_bar_height, "None",
                           curr_active.capitalize(), 1, meas.img_avatarPreview['path'],
                           screen, meas.header_secondary_font)

    # NAME SECTION
    label_name = Label(meas.label_name['text'], meas.label_name['font'], meas.label_name['color'], screen,
                       meas.label_name['x'], meas.label_name['y'], meas.label_name['anchor'])

    input_name = InputField(meas.input_name['x'], meas.input_name['y'],
                            meas.input_name['width'], meas.input_name['height'],
                            meas.input_name['border'], meas.input_name['color'],
                            screen, meas.input_name['placeholder'], meas.nickname_length)

    # CLASS SECTION
    label_class = Label(meas.label_class['text'], meas.label_class['font'], meas.label_class['color'], screen,
                        meas.label_class['x'], meas.label_class['y'], meas.label_class['anchor'])

    bt_warrior_active = Button(meas.bt_class_active['color'],
                        meas.bt_warrior['x'], meas.bt_warrior['y'],
                        meas.bt_warrior['width'], meas.bt_warrior['height'], screen,
                        meas.bt_warrior['text'],
                        path=meas.bt_warrior['path_white'],
                        image_ofset=meas.bt_class_active['image_offset'],
                        border_radius=meas.bt_class_active['border_radius'])

    bt_warrior_inactive = Button(meas.bt_class_inactive['color'],
                        meas.bt_warrior['x'], meas.bt_warrior['y'],
                        meas.bt_warrior['width'], meas.bt_warrior['height'], screen,
                        meas.bt_warrior['text'],
                        path=meas.bt_warrior['path_gray'],
                        image_ofset=meas.bt_class_inactive['image_offset'],
                        border_radius=meas.bt_class_inactive['border_radius'])

    bt_mage_active = Button(meas.bt_class_active['color'],
                     meas.bt_mage['x'], meas.bt_mage['y'],
                     meas.bt_mage['width'], meas.bt_mage['height'], screen,
                     meas.bt_mage['text'],
                     path=meas.bt_mage['path_white'],
                     image_ofset=meas.bt_class_active['image_offset'],
                     border_radius=meas.bt_class_active['border_radius'])

    bt_mage_inactive = Button(meas.bt_class_inactive['color'],
                     meas.bt_mage['x'], meas.bt_mage['y'],
                     meas.bt_mage['width'], meas.bt_mage['height'], screen,
                     meas.bt_mage['text'],
                     path=meas.bt_mage['path_gray'],
                     image_ofset=meas.bt_class_inactive['image_offset'],
                     border_radius=meas.bt_class_inactive['border_radius'])

    bt_archer_active = Button(meas.bt_class_active['color'],
                       meas.bt_archer['x'], meas.bt_archer['y'],
                       meas.bt_archer['width'], meas.bt_archer['height'], screen,
                       meas.bt_archer['text'],
                       path=meas.bt_archer['path_white'],
                       image_ofset=meas.bt_class_active['image_offset'],
                       border_radius=meas.bt_class_active['border_radius'])

    bt_archer_inactive = Button(meas.bt_class_inactive['color'],
                       meas.bt_archer['x'], meas.bt_archer['y'],
                       meas.bt_archer['width'], meas.bt_archer['height'], screen,
                       meas.bt_archer['text'],
                       path=meas.bt_archer['path_gray'],
                       image_ofset=meas.bt_class_inactive['image_offset'],
                       border_radius=meas.bt_class_inactive['border_radius'])

    # AVATARS SECTION
    label_avatar = Label(meas.label_avatar['text'], meas.label_avatar['font'], meas.label_avatar['color'], screen,
                         meas.label_avatar['x'], meas.label_avatar['y'], meas.label_avatar['anchor'])

    # PREVIEW BARS SECTION
    label_curr_name, label_curr_class = reloadPreviewBars(input_name.text, curr_active)
    # label_curr_name = Label(meas.label_curr_name['text'], meas.label_curr_name['font'], meas.label_curr_name['color'], screen,
    #                    meas.label_curr_name['x'], meas.label_curr_name['y'], meas.label_curr_name['anchor'])
    #
    # label_curr_class = Label(curr_active.capitalize(), meas.label_curr_class['font'], meas.label_curr_class['color'], screen,
    #                    meas.label_curr_class['x'], meas.label_curr_class['y'], meas.label_curr_class['anchor'])

    images = generateAvatarsOfCurrentClass(curr_active)

    while True:
        screen.fill((255, 255, 255))

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        label_page.draw()

        # img_avatarPreview.draw()
        cos.draw()

        label_curr_name, label_curr_class = reloadPreviewBars(input_name.text, curr_active)
        label_curr_name.draw()
        label_curr_class.draw()

        label_name.draw()
        input_name.draw()

        label_class.draw()
        if curr_active == 'warrior':
            bt_warrior_active.draw()
            bt_mage_inactive.draw()
            bt_archer_inactive.draw()

        if curr_active == 'mage':
            bt_warrior_inactive.draw()
            bt_mage_active.draw()
            bt_archer_inactive.draw()

        if curr_active == 'archer':
            bt_warrior_inactive.draw()
            bt_mage_inactive.draw()
            bt_archer_active.draw()

        label_avatar.draw()
        images = generateAvatarsOfCurrentClass(curr_active)
        for image in images:
            image.draw()

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                # Input name
                if input_name.active:
                    if event.key == K_BACKSPACE:
                        input_name.subtractText()
                    else:
                        input_name.appendText(event.unicode)

            if event.type == MOUSEBUTTONDOWN:
                # 'Name' input activate
                if input_name.rect.collidepoint(event.pos):
                    input_name.activate()
                else:
                    input_name.deactivate()

                # Pick 'warrior' class
                if bt_warrior_inactive.rect.collidepoint(event.pos):
                    curr_active = 'warrior'
                    print(curr_active)

                # Pick 'mage' class
                if bt_mage_inactive.rect.collidepoint(event.pos):
                    curr_active = 'mage'
                    print(curr_active)

                # Pick 'archer' class
                if bt_archer_inactive.rect.collidepoint(event.pos):
                    curr_active = 'archer'
                    print(curr_active)


        pygame.display.update()
        mainClock.tick(60)
