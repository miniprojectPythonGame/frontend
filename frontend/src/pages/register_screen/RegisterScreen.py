import pygame
import sys
from pygame.locals import *

from frontend.src.components.InputField import InputField
from frontend.src.components.ImageField import ImageField
from frontend.src.components.Label import Label
from frontend.src.components.MultilineText import MultilineText
from frontend.src.components.Button import Button

from .Measurements import Measurements as meas


def RegisterScreen(screen, mainClock):

    # Function to validate input on Login
    def validate():
        if len(input_nickname.text) < 8:
            return False
        if len(input_password.text) < 8:
            return False
        return True

    isRunning = True
    image = ImageField(meas.graphic['x'], meas.graphic['y'],
                       meas.graphic['width'], meas.graphic['height'],
                       '../images/pages/register_screen/image_1.png', screen)

    logo = ImageField(meas.logo['x'], meas.logo['y'],
                       meas.logo['width'], meas.logo['height'],
                       '../images/logo_100x37.png', screen)

    label_register = Label(meas.label_login['text'], meas.title_font, meas.text_color, screen,
                        meas.label_login['x'], meas.label_login['y'], meas.label_login['anchor'])

    mt_description = MultilineText(meas.mt_desc['text'], meas.text_font, meas.text_color,
                                   screen, meas.mt_desc['x'], meas.mt_desc['y'],
                                   meas.mt_desc['line_height'], meas.mt_desc['anchor'])

    input_nickname = InputField(meas.input_nick['x'], meas.input_nick['y'],
                                meas.input_nick['width'], meas.input_nick['height'],
                                meas.input_nick['border'], meas.input_nick['color'],
                                screen, 'Nickname', meas.nickname_length)

    input_email = InputField(meas.input_email['x'], meas.input_email['y'],
                                meas.input_email['width'], meas.input_email['height'],
                                meas.input_email['border'], meas.input_email['color'],
                                screen, 'Email', meas.password_length)

    input_password = InputField(meas.input_pass['x'], meas.input_pass['y'],
                                meas.input_pass['width'], meas.input_pass['height'],
                                meas.input_pass['border'], meas.input_pass['color'],
                                screen, 'Password', 17, isPassword=True)

    bt_register = Button(meas.bt_login['color'], meas.bt_login['x'], meas.bt_login['y'],
                      meas.bt_login['width'], meas.bt_login['height'], screen,
                      meas.bt_login['text'], meas.input_font)

    bt_signin = Button(meas.bt_signup['color'], meas.bt_signup['x'], meas.bt_signup['y'],
                       meas.bt_signup['width'], meas.bt_signup['height'], screen,
                       meas.bt_signup['text'], meas.header_tertiary_font, border=2)

    label_signin = Label(meas.label_signup['text'], meas.header_tertiary_font, meas.text_color, screen,
                         meas.label_signup['x'], meas.label_signup['y'], meas.label_signup['anchor'])

    while isRunning:
        screen.fill((255, 255, 255))

        logo.draw()
        label_register.draw()
        mt_description.draw()
        input_nickname.draw()
        input_password.draw()
        bt_register.draw()
        input_email.draw()
        label_signin.draw()
        bt_signin.draw()
        image.draw()

        mx, my = pygame.mouse.get_pos()

        # HOVERS
        if bt_register.rect.collidepoint((mx, my)):
            bt_register.onHoverOn()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            bt_register.onHoverOff()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if bt_signin.rect.collidepoint((mx, my)):
            bt_signin.onHoverOn()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            bt_signin.onHoverOff()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # EVENTS
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                # Key processing for 'Nickname' input
                if input_nickname.active:
                    if event.key == K_BACKSPACE:
                        input_nickname.subtractText()
                    elif event.key == K_TAB:
                        input_nickname.deactivate()
                        input_email.activate()
                    else:
                        input_nickname.appendText(event.unicode)

                # Key processing for 'Email' input
                if input_email.active:
                    if event.key == K_BACKSPACE:
                        input_email.subtractText()
                    elif event.key == K_TAB:
                        input_email.deactivate()
                        input_password.activate()
                    else:
                        input_email.appendText(event.unicode)

                # Key processing for 'Password' input
                if input_password.active:
                    if event.key == K_BACKSPACE:
                        input_password.subtractText()
                    elif event.key == K_TAB:
                        input_password.deactivate()
                    else:
                        input_password.appendText(event.unicode)
            if event.type == MOUSEBUTTONDOWN:
                # if event.button == 1:
                #     click = True

                # 'Nickname' input
                if input_nickname.rect.collidepoint(event.pos):
                    input_nickname.activate()
                else:
                    input_nickname.deactivate()

                # 'Email' input
                if input_email.rect.collidepoint(event.pos):
                    input_email.activate()
                else:
                    input_email.deactivate()

                # 'Password' input
                if input_password.rect.collidepoint(event.pos):
                    input_password.activate()
                else:
                    input_password.deactivate()

                # 'Login' button
                if bt_register.rect.collidepoint(event.pos):
                    print("Register: ", input_nickname.text, input_email.text, input_password.text)

                    # Tutaj będzie wysyłanie requesta w celu zarejestrowania
                    if validate():
                        pass

                # 'Sign in' button
                if bt_signin.rect.collidepoint(event.pos):
                    print("Redirect-> Login")
                    isRunning = False

        pygame.display.update()
        mainClock.tick(60)
