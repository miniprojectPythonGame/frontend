import pygame

from src.globals.const_values import *
from src.components.ColorSchemes import ColorSchemes


class Measurements:
    # WINDOW PARAMETERS
    size_factor = SIZE_FACTOR
    window_width = SCREEN_WIDTH * size_factor
    window_height = SCREEN_HEIGHT * size_factor
    margin = round(SCREEN_WIDTH * SIZE_FACTOR * 0.12)

    # ACCOUNT PROPERTIES
    nickname_length = NICKNAME_LENGTH
    password_length = PASSWORD_LENGTH

    # LOGO PARAMETERS
    logo_size_factor = 0.15
    logo_width = 899 * logo_size_factor
    logo_height = 318 * logo_size_factor

    # FONTS: sizes
    title_font = TITLE_FONT
    header_primary_font = HEADER_PRIMARY_FONT
    header_secondary_font = HEADER_SECONDARY_FONT
    header_tertiary_font = HEADER_TERTIARY_FONT
    text_font = TEXT_FONT
    input_font = INPUT_FONT

    # FONTS: colors
    text_color = pygame.Color('gray26')
    white = pygame.Color('white')

    # ARROW BUTTONS SIZE:
    abt_size = 60

    # CharacterPreview sizes:
    main_size = 280
    main_bar_height = 30

    secondary_size = 180
    secondary_bar_height = 20

    # left -> right
    # LABEL: Page
    label_page = {
        'text': 'Choose character',
        'x': window_width - margin,
        'y': 20,
        'anchor': 'topright',
        'font': header_primary_font,
        'color': text_color,
    }

    # CHARACTER PREVIEW: Character 1
    cp_character_1 = {
        'x': round(window_width/2) - (main_size/2),
        'y': round(window_height/2) - ((main_size + main_bar_height)/2) - 20,
        'width': main_size,
        'height': main_size,
        'bar_width': main_size - 100,
        'bar_height': main_bar_height,
        'font': header_tertiary_font,
    }

    # CHARACTER PREVIEW: Character 2
    cp_character_2 = {
        'x': ((round(window_width/2) - (secondary_size/2) - margin) - secondary_size)/2 + margin,
        'y': round(window_height/2) - ((secondary_size + secondary_bar_height)/2) - 20,
        'width': secondary_size,
        'height': secondary_size,
        'bar_width': secondary_size - 64,
        'bar_height': secondary_bar_height,
        'font': text_font,
    }

    # CHARACTER PREVIEW: Character 3 - create new
    cp_character_3 = {
        'x': window_width - ((round(window_width/2) - (secondary_size/2) - margin) - secondary_size)/2 - (secondary_size + margin),
        'y': round(window_height/2) - ((secondary_size + secondary_bar_height)/2) - 20,
        'width': secondary_size,
        'height': secondary_size,
        'bar_width': secondary_size - 64,
        'bar_height': secondary_bar_height,
        'font': text_font,
    }

    # BUTTON: Previous
    bt_prev = {
        "color": ColorSchemes(white, white, white, white),
        "x": round(margin/2),
        "y": round(window_height/2) - (abt_size/2),
        "width": abt_size,
        "height": abt_size,
        "text": '',
        "font": input_font,
        "path": '../images/icons/left.png',
    }

    # BUTTON: Next
    bt_next = {
        "color": ColorSchemes(white, white, white, white),
        "x": window_width - (round(margin/2) + abt_size),
        "y": round(window_height/2) - (abt_size/2),
        "width": abt_size,
        "height": abt_size,
        "text": '',
        "font": input_font,
        "path": '../images/icons/right.png',
    }