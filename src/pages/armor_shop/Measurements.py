import pygame

from src.globals.const_values import *
from src.globals.mock_data import armor_shop, character_2
from src.components.ColorSchemes import ColorSchemes


class Measurements:
    # WINDOW PARAMETERS
    size_factor = SIZE_FACTOR
    window_width = SCREEN_WIDTH * size_factor
    window_height = SCREEN_HEIGHT * size_factor
    margin = round(SCREEN_WIDTH * SIZE_FACTOR * 0.12 * 0.5)

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
    label_padding = 35
    class_button_size = 60
    default_color = ColorSchemes()

    stock = armor_shop
    bt_return = BT_RETURN

    # LABEL: Page
    label_page = {
        'text': 'Armor shop',
        'x': margin,
        'y': 20,
        'anchor': 'topleft',
        'font': header_primary_font,
        'color': text_color,
    }

    # CHARACTER_EQUIPMENT: -//-
    ce_characterEqPreview = {
        "x": window_width - 510 - margin,
        "y": margin - 30,
        "font": header_tertiary_font,
        "colors": default_color,
        "character_ref": character_2,
    }

    # ITEM_GRID: shop offer
    ig_items = {
        "x": margin,
        "y": margin,
        "item_size": 80,
        "item_padding": 10,
        "cols": 4,
        "amount": 24,
    }