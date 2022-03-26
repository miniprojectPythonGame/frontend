import pygame
import sys
from pygame.locals import *

from src.components.InputField import InputField
from src.components.ImageField import ImageField
from src.components.Label import Label
from src.components.MultilineText import MultilineText
from src.components.Button import Button
from src.components.Checkbox import Checkbox

from .Measurements import Measurements as meas
from src.globals.mock_data import character_1 as chara_1
from src.globals.mock_data import character_2 as chara_2


class CharacterPreview:
    def __init__(self, x, y, width, height, bar_width, bar_height,
                 name, class_name, level, imagePath, screen, font):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bar_width = bar_width
        self.bar_height = bar_height
        self.name = name
        self.class_name = class_name
        self.level = level
        self.screen = screen
        self.font = font
        self.rect = pygame.Rect(x, y, width, height + 2*bar_height)
        self.image = ImageField(x, y, width, height, imagePath, screen)
        self.rect_border = pygame.Rect(x, y, width, height)

        self.rect_name = pygame.Rect(x + round((width-bar_width)/2),
                                     y + height - bar_height - 10,
                                     bar_width, bar_height)
        self.text_name = self.font.render(self.name, 1, pygame.Color('white'))

        self.rect_class = pygame.Rect(x,
                                      y + height,
                                      width, bar_height)
        self.text_class = self.font.render(self.class_name, 1, pygame.Color('white'))

        self.rect_level = pygame.Rect(x,
                                      y + height + bar_height,
                                      width, bar_height)
        self.text_level = self.font.render('Level ' + str(self.level), 1, pygame.Color('white'))

    def draw(self):
        self.image.draw()
        pygame.draw.rect(self.screen, pygame.Color('gray14'), self.rect_border, 3)

        pygame.draw.rect(self.screen, pygame.Color('gray14'), self.rect_name, 0, 7)
        self.screen.blit(self.text_name,
                         (self.x + (self.width - self.bar_width)/2 + (self.bar_width - self.text_name.get_width())/2,
                          self.y + self.height - self.bar_height - 8 + (self.bar_height - self.text_name.get_height())/2))

        if self.class_name != '':
            pygame.draw.rect(self.screen, pygame.Color('gray14'), self.rect_class, 0)
            self.screen.blit(self.text_class,
                             (self.x + (self.width - self.text_class.get_width())/2,
                              self.y + self.height + (self.bar_height - self.text_class.get_height())/2))

            pygame.draw.rect(self.screen, pygame.Color('gray26'), self.rect_level, 0)
            self.screen.blit(self.text_level,
                             (self.x + (self.width - self.text_level.get_width()) / 2,
                              self.y + self.height + self.bar_height + (self.bar_height - self.text_level.get_height())/2))


def ChooseCharacter(screen, mainClock):
    print(meas.window_width, meas.cp_character_1['x'])
    print(meas.window_height, meas.cp_character_1['y'])
    label_page = Label(meas.label_page['text'], meas.label_page['font'], meas.label_page['color'], screen,
                       meas.label_page['x'], meas.label_page['y'], meas.label_page['anchor'])

    character_1 = CharacterPreview(meas.cp_character_1['x'], meas.cp_character_1['y'],
                                   meas.cp_character_1['width'], meas.cp_character_1['height'],
                                   meas.cp_character_1['bar_width'], meas.cp_character_1['bar_height'],
                                   chara_1['name'], chara_1['spec'], chara_1['level'],
                                   chara_1['img'], screen, meas.cp_character_1['font'])

    character_2 = CharacterPreview(meas.cp_character_2['x'], meas.cp_character_2['y'],
                                   meas.cp_character_2['width'], meas.cp_character_2['height'],
                                   meas.cp_character_2['bar_width'], meas.cp_character_2['bar_height'],
                                   chara_2['name'], chara_2['spec'], chara_2['level'],
                                   chara_2['img'], screen, meas.cp_character_2['font'])

    character_3 = CharacterPreview(meas.cp_character_3['x'], meas.cp_character_3['y'],
                                   meas.cp_character_3['width'], meas.cp_character_3['height'],
                                   meas.cp_character_3['bar_width'], meas.cp_character_3['bar_height'],
                                   'Create', '', '',
                                   '../images/characters/create_new.png', screen, meas.cp_character_3['font'])

    bt_prev = Button(meas.bt_prev['color'], meas.bt_prev['x'], meas.bt_prev['y'],
                      meas.bt_prev['width'], meas.bt_prev['height'], screen,
                      meas.bt_prev['text'], meas.bt_prev['font'], path=meas.bt_prev['path'])

    bt_next = Button(meas.bt_next['color'], meas.bt_next['x'], meas.bt_next['y'],
                      meas.bt_next['width'], meas.bt_next['height'], screen,
                      meas.bt_next['text'], meas.bt_next['font'], path=meas.bt_next['path'])


    while True:
        screen.fill((255, 255, 255))

        label_page.draw()
        character_1.draw()
        character_2.draw()
        character_3.draw()

        bt_prev.draw()
        bt_next.draw()

        mx, my = pygame.mouse.get_pos()

        # HOVERS
        # Button login: hover
        if character_1.rect.collidepoint((mx, my)):
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
                    print('Prev')

                if bt_next.rect.collidepoint(event.pos):
                    print('Next')



        pygame.display.update()
        mainClock.tick(60)
