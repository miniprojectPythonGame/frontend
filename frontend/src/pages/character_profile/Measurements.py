from frontend.src.globals.const_values import *
from frontend.src.components.ColorSchemes import ColorSchemes

from frontend.src.globals.mock_data import character_2


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
    bar_colorScheme = ColorSchemes()

    bt_return = BT_RETURN

    # LABEL: Page
    label_page = {
        'text': 'Character profile',
        'x': window_width - margin,
        'y': 20,
        'anchor': 'topright',
        'font': header_primary_font,
        'color': text_color,
    }

    # CHARACTER_EQUIPMENT: -//-
    ce_characterEqPreview = {
        "x": margin,
        "y": margin - 30,
        "font": header_tertiary_font,
        "colors": bar_colorScheme,
        "character_ref": character_2,
    }

    # ITEM_GRID: backpack
    ig_backpack = {
        "x": margin,
        "y": margin - 30,
        "font": header_tertiary_font,
        "colors": bar_colorScheme,
        "backpack_ref": character_2['backpack'],
    }