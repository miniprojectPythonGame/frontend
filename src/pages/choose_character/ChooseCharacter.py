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
from src.globals.mock_data import createNew as createNew


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
        self.rect = pygame.Rect(x, y, width, height + 2 * bar_height)
        self.image = ImageField(x, y, width, height, imagePath, screen)
        self.rect_border = pygame.Rect(x, y, width, height)

        self.rect_name = pygame.Rect(x + round((width - bar_width) / 2),
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
                         (
                             self.x + (self.width - self.bar_width) / 2 + (
                                         self.bar_width - self.text_name.get_width()) / 2,
                             self.y + self.height - self.bar_height - 8 + (
                                     self.bar_height - self.text_name.get_height()) / 2))

        if self.class_name != '':
            pygame.draw.rect(self.screen, pygame.Color('gray14'), self.rect_class, 0)
            self.screen.blit(self.text_class,
                             (self.x + (self.width - self.text_class.get_width()) / 2,
                              self.y + self.height + (self.bar_height - self.text_class.get_height()) / 2))

            pygame.draw.rect(self.screen, pygame.Color('gray26'), self.rect_level, 0)
            self.screen.blit(self.text_level,
                             (self.x + (self.width - self.text_level.get_width()) / 2,
                              self.y + self.height + self.bar_height + (
                                      self.bar_height - self.text_level.get_height()) / 2))


class CharacterSlider:
    def __init__(self, characters, screen):
        self.characters = characters
        self.curr_index = None
        self.curr_main = None
        self.curr_left = None
        self.curr_right = None
        self.screen = screen
        self.initiateIndex()
        self.loadVisible()

    def initiateIndex(self):
        if len(self.characters) < 1:
            print("[ChooseCharacter > CharacterSlider > initiateIndex]: Error")

        if len(self.characters) == 1:
            self.curr_index = 0

        if len(self.characters) > 1:
            self.curr_index = 1

    def loadVisible(self):
        self.curr_main = CharacterPreview(meas.cp_main['x'], meas.cp_main['y'],
                                          meas.cp_main['width'], meas.cp_main['height'],
                                          meas.cp_main['bar_width'], meas.cp_main['bar_height'],
                                          self.characters[self.curr_index]['name'],
                                          self.characters[self.curr_index]['spec'],
                                          self.characters[self.curr_index]['level'],
                                          self.characters[self.curr_index]['img'],
                                          self.screen, meas.cp_main['font'])

        if self.curr_index - 1 >= 0:
            self.curr_left = CharacterPreview(meas.cp_left['x'], meas.cp_left['y'],
                                              meas.cp_left['width'], meas.cp_left['height'],
                                              meas.cp_left['bar_width'], meas.cp_left['bar_height'],
                                              self.characters[self.curr_index - 1]['name'],
                                              self.characters[self.curr_index - 1]['spec'],
                                              self.characters[self.curr_index - 1]['level'],
                                              self.characters[self.curr_index - 1]['img'],
                                              self.screen, meas.cp_left['font'])
        else:
            self.curr_left = None

        if self.curr_index + 1 < len(self.characters):
            self.curr_right = CharacterPreview(meas.cp_right['x'], meas.cp_right['y'],
                                               meas.cp_right['width'], meas.cp_right['height'],
                                               meas.cp_right['bar_width'], meas.cp_right['bar_height'],
                                               self.characters[self.curr_index + 1]['name'],
                                               self.characters[self.curr_index + 1]['spec'],
                                               self.characters[self.curr_index + 1]['level'],
                                               self.characters[self.curr_index + 1]['img'],
                                               self.screen, meas.cp_right['font'])
        else:
            self.curr_right = None

    def draw(self):
        self.curr_main.draw()
        if self.curr_left:
            self.curr_left.draw()
        if self.curr_right:
            self.curr_right.draw()

    def swipeLeft(self):
        print('Prev')
        if self.curr_index > 0:
            self.curr_index -= 1
            self.loadVisible()

    def swipeRight(self):
        print('Next')
        if self.curr_index < len(self.characters) - 1:
            self.curr_index += 1
            self.loadVisible()


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

        pygame.display.update()
        mainClock.tick(60)
